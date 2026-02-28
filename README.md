# Campus Academic Announcement Platform

AI-powered campus academic assistant using **Django + PostgreSQL (pgvector) + SmolLM (Ollama)**.

---

## 🚀 Full Setup Instructions

### 1. Clone the Repository

# 1. Clone the Repository
git clone https://github.com/afidhu/django_chatboot02.git
cd project-name

# 2. Create Virtual Environment
python -m venv venv

# Windows activate
venv\Scripts\activate

# Mac/Linux activate
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Setup Database
# - Ensure PostgreSQL is installed and running
# - Create a database named campus_academic_db
# - Update settings.py with your database credentials

# 5. Run Migrations
python manage.py makemigrations
python manage.py migrate

# 6. Start Django Server
python manage.py runserver

# 7. Start SmolLM API locally
ollama serve

# 8. Test model generation (stream mode)
ollama generate smollm2:1.7b "Hello, AI assistant!" --stream
