import reflex as rx
from app.state import AppState
from app import styles
from app.components.layout import app_layout

SHIRT_SIZES = ["XS", "S", "M", "L", "XL"]
POSITIONS = [
    "Pinya (base)", "Baixos", "Segons",
    "Terços", "Quarts", "Pom de dalt", "Enxaneta",
]


def manual_entry_page() -> rx.Component:
    return app_layout(
        rx.box(
            rx.text("Manual entry", style=styles.page_title_style),
            rx.text("Add a casteller directly", style=styles.page_sub_style),
            rx.box(
                rx.text("Casteller details", style=styles.card_title_style),
                rx.grid(
                    rx.vstack(
                        rx.text("Full name", style=styles.label_style),
                        rx.input(placeholder="Maria García", value=AppState.casteller_name,
                                 on_change=AppState.set_casteller_name, font_size="13px", width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    rx.vstack(
                        rx.text("Height (cm)", style=styles.label_style),
                        rx.input(placeholder="165", type="number", value=AppState.casteller_height,
                                 on_change=AppState.set_casteller_height, font_size="13px", width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    columns="2", spacing="3", width="100%", margin_bottom="12px",
                ),
                rx.grid(
                    rx.vstack(
                        rx.text("Weight (kg)", style=styles.label_style),
                        rx.input(placeholder="60", type="number", value=AppState.casteller_weight,
                                 on_change=AppState.set_casteller_weight, font_size="13px", width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    rx.vstack(
                        rx.text("Shirt size", style=styles.label_style),
                        rx.select(SHIRT_SIZES, value=AppState.casteller_shirt,
                                  on_change=AppState.set_casteller_shirt, width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    columns="2", spacing="3", width="100%", margin_bottom="12px",
                ),
                rx.grid(
                    rx.vstack(
                        rx.text("Preferred position", style=styles.label_style),
                        rx.select(POSITIONS, value=AppState.casteller_position,
                                  on_change=AppState.set_casteller_position, width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    rx.vstack(
                        rx.text("Experience (years)", style=styles.label_style),
                        rx.input(placeholder="3", type="number", value=AppState.casteller_experience,
                                 on_change=AppState.set_casteller_experience, font_size="13px", width="100%"),
                        spacing="1", align_items="flex_start", width="100%",
                    ),
                    columns="2", spacing="3", width="100%", margin_bottom="12px",
                ),
                rx.vstack(
                    rx.text("Notes", style=styles.label_style),
                    rx.input(placeholder="Any injuries, availability constraints...",
                             value=AppState.casteller_notes, on_change=AppState.set_casteller_notes,
                             font_size="13px", width="100%"),
                    spacing="1", align_items="flex_start", width="100%", margin_bottom="12px",
                ),
                rx.cond(
                    AppState.entry_success != "",
                    rx.box(
                        rx.text(AppState.entry_message, font_size="12px",
                                color=rx.cond(AppState.entry_is_error, "red", "#27500A")),
                        background_color=rx.cond(AppState.entry_is_error, "#FCEBEB", "#EAF3DE"),
                        border_radius="8px", padding="8px 12px", margin_bottom="12px",
                    ),
                ),
                rx.hstack(
                    rx.button("Save casteller", on_click=AppState.save_casteller, style=styles.btn_primary),
                    rx.button("Clear form", on_click=AppState.clear_form, style=styles.btn_secondary),
                    spacing="2",
                ),
                style=styles.card_style,
            ),
            width="100%",
        ),
        "/manual",
    )
