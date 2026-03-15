# Parts Management Web App

A simple Parts Management System built with Flask, MySQL, and Docker. This project allows an admin to manage users, parts inventory, and perform role-based operations.

## Features
User Management
- Admin can create, delete, and update users
- Admin can reset passwords
- Role-based access: admin, editor, viewer
- Admin cannot delete their own account(prevention for accidental lock-out)

Parts Management
- Add, edit, delete parts(admin only)
- Editors can edit parts
- Viewers can only view parts
- Added editor and viewer role

Security
- Passwords are stored hashed using werkzeug.security.generate_password_hash 
- Role-based page access
- Session management with Flask session

## Tech Stack
- Backend: Flask
- Database: MySQL 8
- Containerization: Docker & Docker Compose
- Frontend: Bootstrap 5
- Password Security: Werkzeug hash (scrypt/pbkdf2)

## Project Structure

```text
computer-parts-service/
|-------app/                        # Flask app
|        |----app.py                # Flask app routes & logic
|        |----create_db.py
|        |----Dockerfile
|        |----pc_parts.db
|        |----templates/            # HTML templates
|              |----index.html
|              |----add_part.html
|              |----edit_part.html
|              |----users.html
|              |----edit_user.html
|-------nginx/                      # Nginx config
|        |----Dockerfile
|        |----nginx.conf
|-------docker-compose.yml          # Docker Compose file
|-------init.sql                    # Initial MySQL setup & hashed admin password
|-------README.md
|-------requirements.txt
```
## Requirements
- Docker
- Docker Compose
- Web browser (Chrome, Firefox, etc.)


## Security Notes
1.	Passwords are hashed in the database
2.	Changing the admin password does not require updating init.sql
3.	Sessions are protected with a secret key in app.py

## Usage
1.	Admin Panel
    •	Access via User Management button
    •	Add, edit, delete users
    •	Reset user passwords
2.	Parts Management
    •	Add, edit, delete parts (based on role)
    •	Filter and search parts by category or keyword
3.	Dark Theme
    •	Future improvement: Dark theme will sync across all pages

## Future Improvements
    •	Sync dark theme across User Management and Edit User pages
    •	Add activity logs for user actions
    •	Enhance form validations
    •	Add export/import for parts data (CSV/Excel)
    •	Add REST API endpoints

## Author
    •	Rommel Asis – Original Developer

## Setup Instruction
1. Clone the repository:
```
    bash
    git clone https://github.com/<your-username>/parts-management.git
    cd parts-management

 
2. Build the Docker containers:
```bash
 docker compose up --build

1.	Web app will be accessible at http://localhost:8080
2.	MySQL is available internally on port 3306, mapped to host 3307

3.	Initial Admin Account
    ⦁	Username: admin
    ⦁	Password: admin123 (hashed in init.sql)
    ⦁	Only the admin can create users and manage roles

4. Stop Containers:
    bash
    docker compose down
```
