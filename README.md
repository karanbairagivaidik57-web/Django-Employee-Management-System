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
* **Add Employee:** Create new employee profiles.
* **Update/Delete:** Easily modify or remove records.
* **Search Functionality:** Filter employees by Name, Email, Phone, or Department.

### 🏢 Department Management
* **Organization:** Manage departments with auto-count of employees.
* **Seamless UI:** Dedicated views for department lists and edits.

---

## ✅ Real-World Validations
* **Data Integrity:** Name validation (alphabets only) & Mobile number validation (Indian format).
* **Business Logic:** Salary > 0, Unique Email check, and no future Hire Dates.
* **Safety:** Prevention of duplicate department entries.

---

## 🛠️ Tech Stack & Security
* **Backend:** Django (Python)
* **Database:** MySQL (Hosted on **Aiven Cloud**)
* **Security:** Environment variables (`python-dotenv`) to hide sensitive credentials.
* **Frontend:** Responsive HTML & CSS (Card layout for mobile).

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository
```bash
### 1️⃣ Clone the repository
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
