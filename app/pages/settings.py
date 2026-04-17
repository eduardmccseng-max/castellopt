import reflex as rx
from app.state import AppState
from app import styles
from app.components.layout import app_layout


def toggle(is_on: rx.Var, on_click) -> rx.Component:
    return rx.box(
        rx.box(
            width="14px", height="14px", border_radius="50%", background_color="white",
            position="absolute", top="3px",
            right=rx.cond(is_on, "3px", "unset"),
            left=rx.cond(is_on, "unset", "3px"),
        ),
        width="36px", height="20px", border_radius="10px",
        background_color=rx.cond(is_on, styles.PURPLE_MID, styles.BORDER_MID),
        position="relative", cursor="pointer", on_click=on_click, flex_shrink="0",
    )


def setting_row(label: str, desc: str, is_on: rx.Var, on_click) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(label, font_size="13px", color=styles.TEXT_PRIMARY),
            rx.text(desc, font_size="11px", color=styles.TEXT_SECONDARY),
            spacing="0", align_items="flex_start",
        ),
        rx.spacer(),
        toggle(is_on, on_click),
        width="100%", align_items="center",
        padding="12px 0",
        border_bottom=f"0.5px solid {styles.BORDER}",
    )


def settings_page() -> rx.Component:
    return app_layout(
        rx.box(
            rx.text("Preferències", style=styles.page_title_style),
            rx.text("Configura les preferències del teu compte i de l'optimització.", style=styles.page_sub_style),
            rx.box(
                rx.text("Preferències d'optimització", style=styles.card_title_style),
                setting_row("Prioritza la puntuació de seguretat", "Prefereix estabilitat de pesos sobre alçades",
                            AppState.prioritize_safety, AppState.toggle_safety),
                setting_row("Permet canvis de posicions", "L'optimitzador pot sobreescriure posicions.",
                            AppState.allow_swaps, AppState.toggle_swaps),
                setting_row("Pondera segons experiència", "Preferir castellers experimentats per a posicions crítiques.",
                            AppState.use_experience, AppState.toggle_experience),
                style=styles.card_style,
            ),
            rx.box(
                rx.text("Compte", style=styles.card_title_style),
                rx.grid(
                    rx.vstack(
                        rx.text("Nom", style=styles.label_style),
                        rx.input(placeholder="El teu nom", value=AppState.display_name,
                                 on_change=AppState.set_display_name, font_size="13px", width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    rx.vstack(
                        rx.text("Correu electrònic", style=styles.label_style),
                        rx.input(placeholder="you@colla.cat", type="email", value=AppState.email,
                                 on_change=AppState.set_email, font_size="13px", width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    columns="2", spacing="3", width="100%", margin_bottom="16px",
                ),
                rx.cond(
                    AppState.settings_saved != "",
                    rx.box(
                        rx.text(AppState.settings_saved, font_size="12px", color="#27500A"),
                        background_color="#EAF3DE", border_radius="8px",
                        padding="8px 12px", margin_bottom="12px",
                    ),
                ),
                rx.button("Save changes", on_click=AppState.save_settings, style=styles.btn_primary),
                style=styles.card_style,
            ),
            width="100%",
        ),
        "/settings",
    )
