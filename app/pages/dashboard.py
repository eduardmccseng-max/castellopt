import reflex as rx
from app.state import AppState
from app import styles
from app.components.layout import app_layout


def stat_card(label: str, value: str) -> rx.Component:
    return rx.box(
        rx.text(label, font_size="12px", color=styles.TEXT_SECONDARY, margin_bottom="4px"),
        rx.text(value, font_size="22px", font_weight="500", color=styles.TEXT_PRIMARY),
        style=styles.stat_card_style,
    )


def dashboard_page() -> rx.Component:
    return app_layout(
        rx.box(
            rx.text("Dashboard", style=styles.page_title_style),
            rx.text("Overview of your castell and team", style=styles.page_sub_style),
            rx.hstack(
                stat_card("Castellers", "24"),
                stat_card("Positions filled", "18"),
                stat_card("Castell type", "4 de 8"),
                spacing="3",
                width="100%",
                margin_bottom="16px",
            ),
            rx.box(
                rx.text("Recent activity", style=styles.card_title_style),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell(rx.text("Action", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.column_header_cell(rx.text("User", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.column_header_cell(rx.text("Date", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.column_header_cell(rx.text("Status", font_size="12px", color=styles.TEXT_SECONDARY)),
                        )
                    ),
                    rx.table.body(
                        rx.table.row(
                            rx.table.cell(rx.text("CSV uploaded", font_size="12px")),
                            rx.table.cell(rx.text("you", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.text("Apr 12", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Done", **styles.badge_success))),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.text("Optimization run", font_size="12px")),
                            rx.table.cell(rx.text("you", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.text("Apr 11", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Done", **styles.badge_success))),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.text("3 castellers added", font_size="12px")),
                            rx.table.cell(rx.text("you", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.text("Apr 10", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Saved", **styles.badge_info))),
                        ),
                    ),
                    width="100%",
                ),
                style=styles.card_style,
            ),
            rx.hstack(
                rx.link(rx.button("Go to Upload CSV", style=styles.btn_primary), href="/upload"),
                rx.link(rx.button("View latest results", style=styles.btn_secondary), href="/results"),
                spacing="2",
            ),
            width="100%",
        ),
        "/dashboard",
    )
