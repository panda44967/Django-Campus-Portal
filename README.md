# Campus Portal & Voting System (Django Prototype)

This repository contains a backend web prototype designed to manage campus information and interactive voting events. It is structured into two independent Django modules to demonstrate different architectural patterns and data management strategies.

## Tech Stack
- **Backend:** Python 3.x, Django 5.0.0
- **Database:** SQLite (Django ORM)
- **Architecture:** MVT (Model-View-Template), Function-Based & Class-Based Views

---

## System Modules

### Module 1: Campus Info Dashboard (`campus_info`)
A content-delivery module focused on dynamic template rendering and context management without relying on custom database models.

* **Key Features:**
  * Dynamic routing with named URLs for clean navigation.
  * Utilizes Django's Class-Based Views (`TemplateView`) and function-based views.
  * Implements `get_context_data()` to dynamically inject backend logic into frontend templates.
  * Efficient template inheritance using a unified `base.html`.

### Module 2: Interactive Voting System (`campus_vote`)
A data-driven interactive module designed to manage voting events, built with relational database models.

* **Key Features:**
  * **Relational Database Design:** Includes `Question` and `Choice` models with Foreign Key relationships.
  * **Interactive Frontend:** Users can view nested choices and real-time voting statistics.
  * **Admin Panel Integration:** Fully configured Django Admin (`admin.py`) for easy content management and CRUD operations.
  * **Database Migrations:** Applied ORM migrations for schema stability.

---

## Quick Start / Setup

To run this project locally, follow these steps:

** Clone the repository and set up the environment:**
```bash
# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # For Windows users

# Install dependencies
pip install django==5.0.0

Run Module 1 (Information Dashboard):
cd campus_info
python manage.py runserver 8000
# Access at: [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/)

Run Module 2 (Voting System):
cd ../campus_vote
python manage.py runserver 8001
# Access at: [http://127.0.0.1:8001/](http://127.0.0.1:8001/)
# Admin Panel: [http://127.0.0.1:8001/admin/](http://127.0.0.1:8001/admin/) (Credentials: ntub / 123)

Testing
Both modules include unit tests to ensure application stability.
# Run tests for a specific module
python manage.py test
