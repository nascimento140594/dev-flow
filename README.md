# 🚀 DevFlow

DevFlow is a web application built with Django for managing software development workflows and IT teams.

The platform allows project managers and team members to organize tasks, assign workers, manage teams, and track task progress through a simple and intuitive interface.

---

# ✨ Features

### Task Management

* Create tasks
* View task details
* Update tasks
* Delete tasks
* Set priorities
* Track task status
* Manage deadlines

### Team Management

* Manage development teams
* Manage workers
* Assign workers to teams
* Assign workers to tasks

### Task Classification

* Create task types
* Organize tasks by category

### Administration

* Django Admin Panel
* Bootstrap-based interface
* Responsive design

---

# 🛠 Technologies Used

* Python 3
* Django
* SQLite
* Bootstrap 5
* HTML5
* CSS3

---

# 🗄 Database Structure

The application is composed of four main entities:

* Team
* Worker
* TaskType
* Task

### Entity Relationship Diagram (ERD)

![Database Diagram](database-diagram.png)

### Relationships

* One Team can contain multiple Workers
* One Worker can belong to multiple Teams
* One TaskType can be associated with multiple Tasks
* One Task can be assigned to multiple Workers

---

# 📸 Application Screenshots

## Home Page

![Home](screenshots/home.png)

## Task List

![Task List](screenshots/task-list.png)

## Task Details

![Task Detail](screenshots/task-detail.png)

## Create Task

![Create Task](screenshots/task-create.png)

## Update Task

![Update Task](screenshots/task-update.png)

## Delete Task

![Delete Task](screenshots/task-delete.png)

## Django Admin Panel

![Admin](screenshots/admin.png)

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/nascimento140594/dev-flow.git
```

Navigate to the project directory:

```bash
cd dev-flow
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 📂 Project Structure

```text
dev-flow/
│
├── config/
├── tasks/
├── templates/
├── screenshots/
├── static/
│
├── README.md
├── database-diagram.png
├── manage.py
└── requirements.txt
```

---

# 👨‍💻 Author

Matheus Araujo Nascimento

GitHub:
https://github.com/nascimento140594

---

# 📌 Portfolio Project

This project was developed as part of a Django Portfolio Project and demonstrates:

* Django Models
* Generic Class-Based Views
* CRUD Operations
* Django Templates
* Bootstrap Integration
* Database Modeling
* Git & GitHub Workflow
* Project Documentation
