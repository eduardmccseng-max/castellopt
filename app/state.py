#state.py
import reflex as rx
import sqlmodel
import hashlib


# ── BDDs ────────────────────────────────────────────────────────────

#Usuaris
class User(rx.Model, table=True):
    username: str = sqlmodel.Field(unique=True, index=True)
    password: str
    colla: str


# ── Helpers ───────────────────────────────────────────────────────────────────

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# ── App State ─────────────────────────────────────────────────────────────────

class AppState(rx.State):
    username: str = ""
    is_logged_in: bool = False

    login_username: str = ""
    login_password: str = ""
    login_error: str = ""

    casteller_name: str = ""
    casteller_height: str = ""
    casteller_weight: str = ""
    casteller_shirt: str = "M"
    casteller_position: str = "Pinya (base)"
    casteller_experience: str = ""
    casteller_notes: str = ""
    entry_success: str = ""

    prioritize_safety: bool = True
    allow_swaps: bool = True
    use_experience: bool = False
    display_name: str = ""
    email: str = ""
    settings_saved: str = ""

    results_tab: str = "visual"

    def do_login(self):
        username = self.login_username.strip()
        password = self.login_password.strip()

        if not username or not password:
            self.login_error = "Please enter both username and password."
            return

        with rx.session() as session:
            user = session.exec(
                sqlmodel.select(User).where(User.username == username)
            ).first()

        if user is None:
            self.login_error = "User not found."
            return

        if user.password != password:
            self.login_error = "Incorrect password."
            return

        self.username = username
        self.display_name = username
        self.is_logged_in = True
        self.login_error = ""
        return rx.redirect("/dashboard")

    def do_logout(self):
        self.is_logged_in = False
        self.username = ""
        self.login_username = ""
        self.login_password = ""
        return rx.redirect("/")

    def set_results_tab(self, tab: str):
        self.results_tab = tab

    def save_casteller(self):
        if not self.casteller_name.strip():
            self.entry_success = "error:Name is required."
            return
        self.entry_success = f"success:{self.casteller_name} saved successfully!"
        self.casteller_name = ""
        self.casteller_height = ""
        self.casteller_weight = ""
        self.casteller_shirt = "M"
        self.casteller_position = "Pinya (base)"
        self.casteller_experience = ""
        self.casteller_notes = ""

    def clear_form(self):
        self.casteller_name = ""
        self.casteller_height = ""
        self.casteller_weight = ""
        self.casteller_shirt = "M"
        self.casteller_position = "Pinya (base)"
        self.casteller_experience = ""
        self.casteller_notes = ""
        self.entry_success = ""

    def save_settings(self):
        self.settings_saved = "Settings saved!"

    def toggle_safety(self):
        self.prioritize_safety = not self.prioritize_safety

    def toggle_swaps(self):
        self.allow_swaps = not self.allow_swaps

    def toggle_experience(self):
        self.use_experience = not self.use_experience

    @rx.var
    def user_initials(self) -> str:
        if not self.username:
            return "?"
        parts = self.username.strip().split()
        if len(parts) >= 2:
            return (parts[0][0] + parts[1][0]).upper()
        return self.username[:2].upper()

    @rx.var
    def entry_is_error(self) -> bool:
        return self.entry_success.startswith("error:")

    @rx.var
    def entry_message(self) -> str:
        if ":" in self.entry_success:
            return self.entry_success.split(":", 1)[1]
        return self.entry_success