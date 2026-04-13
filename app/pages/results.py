import reflex as rx
from app.state import AppState
from app import styles
from app.components.layout import app_layout

FORMATION = [
    {"floor": "Enxaneta",   "members": ["Laia"],                          "bg": styles.PURPLE_LIGHT, "fg": styles.PURPLE_DARK},
    {"floor": "Pom de dalt","members": ["Marc", "Anna"],                  "bg": styles.TEAL_LIGHT,   "fg": styles.TEAL_DARK},
    {"floor": "Quarts",     "members": ["Pere", "Joan", "Rosa", "Marta"], "bg": styles.CORAL_LIGHT,  "fg": styles.CORAL_DARK},
    {"floor": "Terços",     "members": ["Sergi", "Núria", "Jordi", "Mireia"], "bg": styles.BLUE_LIGHT, "fg": styles.BLUE_DARK},
    {"floor": "Pinya",      "members": ["Albert", "Carla", "Ferran", "Elena"], "bg": styles.PURPLE_LIGHT, "fg": styles.PURPLE_DARK},
]

MEMBERS = [
    ("Laia",   "Enxaneta",    "138 cm", "98"),
    ("Marc",   "Pom de dalt", "145 cm", "95"),
    ("Pere",   "Quarts",      "158 cm", "91"),
    ("Sergi",  "Terços",      "170 cm", "87"),
    ("Albert", "Pinya",       "182 cm", "96"),
]


def chip(name: str, bg: str, fg: str) -> rx.Component:
    return rx.box(
        rx.text(name, font_size="10px", font_weight="500"),
        background_color=bg, color=fg,
        border_radius="14px", padding="4px 10px", white_space="nowrap",
    )


def results_page() -> rx.Component:
    return app_layout(
        rx.box(
            rx.text("Results", style=styles.page_title_style),
            rx.text("Optimized castell formation", style=styles.page_sub_style),

            # Tab bar
            rx.hstack(
                rx.button(
                    "Visual",
                    on_click=lambda: AppState.set_results_tab("visual"),
                    font_size="13px", padding="8px 14px", border_radius="0",
                    background_color="transparent", border="none",
                    border_bottom=rx.cond(AppState.results_tab == "visual", f"2px solid {styles.PURPLE_MID}", "2px solid transparent"),
                    color=rx.cond(AppState.results_tab == "visual", styles.PURPLE_MID, styles.TEXT_SECONDARY),
                    font_weight=rx.cond(AppState.results_tab == "visual", "500", "400"),
                    cursor="pointer",
                ),
                rx.button(
                    "Member list",
                    on_click=lambda: AppState.set_results_tab("list"),
                    font_size="13px", padding="8px 14px", border_radius="0",
                    background_color="transparent", border="none",
                    border_bottom=rx.cond(AppState.results_tab == "list", f"2px solid {styles.PURPLE_MID}", "2px solid transparent"),
                    color=rx.cond(AppState.results_tab == "list", styles.PURPLE_MID, styles.TEXT_SECONDARY),
                    font_weight=rx.cond(AppState.results_tab == "list", "500", "400"),
                    cursor="pointer",
                ),
                spacing="0",
                border_bottom=f"0.5px solid {styles.BORDER}",
                margin_bottom="20px",
                width="100%",
            ),

            # Visual tab
            rx.cond(
                AppState.results_tab == "visual",
                rx.box(
                    rx.text("4 de 8 — optimized formation", style=styles.card_title_style),
                    rx.text("Top → bottom", font_size="11px", color=styles.TEXT_SECONDARY, text_align="center", margin_bottom="12px"),
                    rx.vstack(
                        *[
                            rx.hstack(
                                rx.text(row["floor"], font_size="10px", color=styles.TEXT_SECONDARY, width="72px", text_align="right"),
                                rx.hstack(*[chip(m, row["bg"], row["fg"]) for m in row["members"]], spacing="1", flex_wrap="wrap"),
                                spacing="2", align_items="center", justify_content="center", width="100%",
                            )
                            for row in FORMATION
                        ],
                        spacing="2", align_items="center", width="100%",
                    ),
                    rx.center(rx.box(rx.text("Score: 94 / 100", **styles.badge_success), margin_top="16px")),
                    style=styles.card_style,
                ),

                # Member list tab
                rx.box(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell(rx.text("Name", font_size="12px", color=styles.TEXT_SECONDARY)),
                                rx.table.column_header_cell(rx.text("Position", font_size="12px", color=styles.TEXT_SECONDARY)),
                                rx.table.column_header_cell(rx.text("Height", font_size="12px", color=styles.TEXT_SECONDARY)),
                                rx.table.column_header_cell(rx.text("Score", font_size="12px", color=styles.TEXT_SECONDARY)),
                            )
                        ),
                        rx.table.body(
                            *[
                                rx.table.row(
                                    rx.table.cell(rx.text(n, font_size="12px")),
                                    rx.table.cell(rx.text(p, font_size="12px", color=styles.TEXT_SECONDARY)),
                                    rx.table.cell(rx.text(h, font_size="12px", color=styles.TEXT_SECONDARY)),
                                    rx.table.cell(rx.box(rx.text(s, **(styles.badge_success if int(s) >= 90 else styles.badge_info)))),
                                )
                                for n, p, h, s in MEMBERS
                            ]
                        ),
                        width="100%",
                    ),
                    style=styles.card_style,
                ),
            ),

            rx.hstack(
                rx.button("Run optimizer (coming soon)", style={**styles.btn_primary, "opacity": "0.6", "cursor": "not-allowed"}),
                rx.button("Export as PDF", style=styles.btn_secondary),
                spacing="2", margin_top="4px",
            ),
            width="100%",
        ),
        "/results",
    )
