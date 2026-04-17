CastellOpt 🏰✨
CastellOpt és una aplicació web desenvolupada amb Reflex per a la gestió de colles castelleres i l'optimització de les estructures dels castells. L'eina permet gestionar la base de dades de castellers i, en el futur, calcular la posició òptima de cada membre segons les seves condicions físiques (alçada, pes) i experiència.

🚀 Característiques
Gestió de Castellers: Formulari d'entrada manual per registrar membres amb dades detallades (alçada, pes, talla de camisa, etc.).

Base de Dades Real: Integració amb SQLite mitjançant SQLModel per a una persistència de dades eficient.

Visualització de Pinya i Tronc: Vista visual de la formació del castell i llista detallada dels membres.

Autenticació: Sistema de login per a la gestió privada de cada colla.

Disseny Modern: Interfície neta i scannable utilitzant els components de Radix UI integrats en Reflex.

🛠️ Stack Tecnològic
Llenguatge: Python 3.12+

Framework Web: Reflex (Frontend & Backend en Python)

ORM: SQLModel (SQLAlchemy + Pydantic)

Base de dades: SQLite

Gestor de paquets: uv

📦 Instal·lació
Aquest projecte utilitza uv per a una gestió ràpida i eficient de l'entorn virtual i les dependències.

Clona el repositori:

Bash
git clone https://github.com/SergiBragos/castellopt.git
cd castellopt
Sincronitza l'entorn i instal·la dependències:

Bash
uv sync
Inicialitza Reflex (si és la primera vegada):

Bash
uv run reflex init
🏃 Execució
Per llançar l'aplicació en mode desenvolupament:

Bash
uv run reflex run
L'aplicació estarà disponible a http://localhost:3000.

📂 Estructura del Projecte
Plaintext
castellopt/
├── .web/               # Fitxers compilats de Next.js (ignorat per git)
├── alembic/            # Migracions de la base de dades
├── app/                # Codi font de l'aplicació
│   ├── components/     # Components UI reutilitzables (layout, nav, etc.)
│   ├── pages/          # Pàgines de l'app (login, dashboard, results, etc.)
│   ├── state.py        # Lògica d'estat i funcions de la base de dades
│   ├── models.py       # Definició de les taules SQLModel (User, Casteller)
│   └── styles.py       # Configuració de colors i estils constants
├── assets/             # Recursos estàtics (imatges, fonts)
├── rxconfig.py         # Configuració de Reflex
└── pyproject.toml      # Dependències i configuració del projecte (uv)

🚧 Roadmap

[ ] Afegir la data de naixement del casteller a la BDD

[ ] Algoritme d'optimització automàtica del tronc segons alçades.

[ ] Exportació de la formació en format PDF.

[ ] Gestió d'assistència als assajos.

[ ] Suport multi-colla avançat.

Desenvolupat amb ❤️ per a les colles castelleres.