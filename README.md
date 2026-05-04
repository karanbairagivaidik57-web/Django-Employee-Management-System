# 🚀 Employee Management System (Django)

A complete **Employee Management Web Application** built using Django with MySQL database and a responsive UI. 
This project allows users to manage employees and departments efficiently with real-world validations and clean design.

---

## 🌐 🔗 Live Demo

👉 **Live Link:** [Click Here to View Live](https://onrender.com)  
*(Render par live hone ke baad yahan apna asli link daal dena)*

---

## 📌 🔥 Features

### 👨‍💼 Employee Management
* **Add Employee:** Create new employee profiles using **Django ModelForms**.
* **Update/Delete:** Perform full CRUD operations seamlessly.
* **Search Functionality:** Advanced filtering using **Django ORM Lookups** (Name, Email, Phone, or Department).

### 🏢 Department Management
* **Organization:** Manage departments with **Auto-Count** logic for employees in each department.
* **Seamless UI:** Dedicated views for department lists and edits.

---

## 🛠️ Technical Highlights (The "Secret Sauce")

### ⚙️ Database & ORM Power
* **Django ORM:** Used complex queries and lookups for efficient data retrieval without writing raw SQL.
* **Model Relationship:** Managed Foreign Key relationships between Employees and Departments.
* **Data Migration:** Leveraged Django Migrations for version control of the database schema.

### 📝 Form Handling & Validation
* **ModelForms:** Utilized `ModelForm` for rapid development and automatic form generation from models.
* **Custom Validations:** 
    *   **Data Integrity:** Name (alphabets only) & Mobile (Indian format).
    *   **Business Logic:** Salary > 0, Unique Email check, and no future Hire Dates.
    *   **Safety:** Prevention of duplicate department entries.

---

## 🏗️ Tech Stack & Security
* **Backend:** Django (Python)
* **Database:** MySQL (Hosted on **Aiven Cloud**)
* **Security:** Environment variables (`python-dotenv`) to hide sensitive credentials.
* **Frontend:** Responsive HTML & CSS (Card layout for mobile).

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
Create a `.env` file in the root directory (near `manage.py`) and add your database details:
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
