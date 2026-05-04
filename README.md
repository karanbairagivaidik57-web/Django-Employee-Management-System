# 🚀 Employee Management System (Django)

[![Deployment Status](https://shields.io)](https://django-employee-management-system-apn0.onrender.com/)
[![Database](https://shields.io)](https://aiven.io)

A complete **Employee Management Web Application** built using Django with a MySQL cloud database. This project features real-world data validations, advanced search, and a clean, responsive UI.

---

## 📸 Screenshots


| 📊 Dashboard Overview | ➕ Add Employee Form |
|---|---|
| ![Dashboard](screenshots/dashboard.png) | ![Add Employee](screenshots/add_emp.png) |

| 🔍 Advanced Search & Filtering |
|---|---|
| ![Search](screenshots/search.png) |

---

## 🌐 🔗 Live Demo

👉 **Live Link:** [View Project Live](https://django-employee-management-system-apn0.onrender.com/)

---

## 📌 🔥 Key Features

### 👨‍💼 Employee Management
*   **Full CRUD Operations:** Seamlessly Add, Update, and Delete employee profiles.
*   **Django ModelForms:** Used for rapid development and automatic form generation.
*   **Advanced Search:** Built with **Django ORM Lookups** to filter by Name, Email, Phone, or Department.

### 🏢 Department Management
*   **Dynamic Organization:** Manage departments with **Auto-Count** logic for employee distribution.
*   **Relational Integrity:** Managed through Foreign Key relationships.

---

## 🛠️ Technical Highlights (The "Secret Sauce")

### ⚙️ Backend & ORM
*   **Complex Queries:** Leveraged Django ORM for efficient data retrieval without raw SQL.
*   **Cloud Database:** Production-ready MySQL hosting on **Aiven Cloud**.
*   **Migrations:** Full version control for database schema.

### 📝 Validations & Security
*   **Custom Business Logic:** Validations for Name (alphabets), Indian Mobile format, Salary (>0), and Unique Emails.
*   **Security First:** Environment variables (`python-dotenv`) to protect sensitive API/DB keys.
*   **Production Serving:** Integrated `WhiteNoise` for efficient static file management.

---

## 🏗️ Tech Stack
*   **Backend:** Django (Python)
*   **Database:** MySQL (Aiven)
*   **Frontend:** HTML5, CSS3 (Responsive Layout)
*   **Deployment:** Render

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/karanbairagivaidik57-web/Django-Employee-Management-System
cd Django-Employee-Management-System
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables
Create a `.env` file in the root directory and add your database details:
```text
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```

### 4️⃣ Run migrations & Start server
```bash
python manage.py migrate
python manage.py runserver
```

---

## 👨‍💻 Author
**Karan Bairagi**

---

## ⭐ Support
If you like this project, give it a ⭐ on GitHub!
