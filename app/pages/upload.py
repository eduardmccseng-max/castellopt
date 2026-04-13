import reflex as rx
from app import styles
from app.components.layout import app_layout


def upload_page() -> rx.Component:
    return app_layout(
        rx.box(
            rx.text("Upload CSV", style=styles.page_title_style),
            rx.text("Import your castellers from a spreadsheet file", style=styles.page_sub_style),
            rx.box(
                rx.text("Select file", style=styles.card_title_style),
                rx.upload(
                    rx.vstack(
                        rx.text("⬆️", font_size="28px"),
                        rx.text("Drop your CSV here or click to browse",
                                font_size="14px", font_weight="500", color=styles.TEXT_PRIMARY),
                        rx.text("Supports .csv files — max 10 MB",
                                font_size="12px", color=styles.TEXT_SECONDARY),
                        spacing="1",
                        align_items="center",
                    ),
                    id="csv_upload",
                    accept={".csv": ["text/csv"]},
                    border=f"1.5px dashed {styles.BORDER_MID}",
                    border_radius="8px",
                    padding="32px",
                    text_align="center",
                    cursor="pointer",
                    width="100%",
                    _hover={"border_color": styles.PURPLE_MID, "background_color": styles.PURPLE_LIGHT},
                ),
                style=styles.card_style,
            ),
            rx.box(
                rx.text("Expected columns", style=styles.card_title_style),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell(rx.text("Column", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.column_header_cell(rx.text("Type", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.column_header_cell(rx.text("Required", font_size="12px", color=styles.TEXT_SECONDARY)),
                        )
                    ),
                    rx.table.body(
                        rx.table.row(
                            rx.table.cell(rx.text("name", font_size="12px", font_family="monospace")),
                            rx.table.cell(rx.text("text", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Yes", **styles.badge_warning))),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.text("height_cm", font_size="12px", font_family="monospace")),
                            rx.table.cell(rx.text("number", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Yes", **styles.badge_warning))),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.text("weight_kg", font_size="12px", font_family="monospace")),
                            rx.table.cell(rx.text("number", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Yes", **styles.badge_warning))),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.text("shirt_size", font_size="12px", font_family="monospace")),
                            rx.table.cell(rx.text("XS/S/M/L/XL", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Optional", **styles.badge_info))),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.text("preferred_position", font_size="12px", font_family="monospace")),
                            rx.table.cell(rx.text("text", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Optional", **styles.badge_info))),
                        ),
                        rx.table.row(
                            rx.table.cell(rx.text("experience_years", font_size="12px", font_family="monospace")),
                            rx.table.cell(rx.text("number", font_size="12px", color=styles.TEXT_SECONDARY)),
                            rx.table.cell(rx.box(rx.text("Optional", **styles.badge_info))),
                        ),
                    ),
                    width="100%",
                ),
                style=styles.card_style,
            ),
            rx.hstack(
                rx.button("Upload and validate", style=styles.btn_primary),
                rx.link(rx.button("Back to dashboard", style=styles.btn_secondary), href="/dashboard"),
                spacing="2",
            ),
            width="100%",
        ),
        "/upload",
    )
