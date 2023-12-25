# 📚 DRFBookshelf - Library Management System

Welcome to DRFBookshelf, a sophisticated Library Management System developed using the Django REST Framework (DRF). This project harnesses the power of DRF to create a dynamic and efficient Web API for seamless library resource management. Tailored to the needs of both library staff and users, DRFBookshelf provides a comprehensive administrative panel for professional library management.

## Project Overview 🎯

### Prerequisites 📦

- Python 3.x
- Django
- Django REST Framework

### Quick Start 🚀

1. **🖇️ Clone the Repository:**

   ```bash
   git clone https://github.com/FMashi/DRFBookshelf.git
   cd DRFBookshelf
   ```

2. **🛠️ Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **♻️ Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Change Directory to 'app':**

   ```bash
   cd app
   ```

5. **⚙️ Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **👤 Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **🪄 Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

8. **✨ Access the Admin Panel:**
   - Open your browser and go to [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Project Structure 🏷️

```plaintext
📁 app/
|-- 📁 app/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   `-- wsgi.py
|-- 📁 authentication/
|   |-- 📁 migrations/
|   |   `-- ...
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- 📁 book/
|   |-- 📁 migrations/
|   |   `-- ...
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- manage.py

```
