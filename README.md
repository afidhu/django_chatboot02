# Campus Academic Announcement Platform

AI-powered campus academic assistant using **Django + PostgreSQL (pgvector) + SmolLM (Ollama)**.

---

## 🚀 Full Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/project-name.git
cd project-name

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
