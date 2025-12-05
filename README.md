# Smart Cloud Property Manager

A simple end-to-end **Smart Property Management** web application with:

- User **registration** and **login**
- Blue **cloud-themed UI**
- Full **CRUD operations** for properties
- **Image upload** support for property photos
- SQLite database (via SQLAlchemy)

Built with **Flask** so you can easily run it locally or deploy it to AWS (e.g. Elastic Beanstalk).

---

## 1. Features

- Register a new user account and log in securely (hashed passwords).
- Create, view, update, and delete properties.
- Each property has:
  - Title
  - Description
  - Address
  - City
  - Monthly rent (validated to be positive)
  - Status (Available / Occupied / Under Maintenance)
  - Optional image (stored under `static/uploads/`)
- Clean blue **cloud UI** using Bootstrap and custom CSS.

---

## 2. Project Structure

```text
cloud_property_app/
├── app.py
├── requirements.txt
├── README.md
├── property_app.db        # created at first run
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── property_form.html
│   └── property_detail.html
└── static/
    ├── css/
    │   └── style.css
    ├── uploads/
    └── img/
```

---

## 3. How to run locally

1. **Create and activate a virtual environment** (recommended):

```bash
cd cloud_property_app
python -m venv venv
source venv/bin/activate       # on macOS / Linux
# venv\Scripts\activate        # on Windows
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Initialize the database**:

```bash
flask --app app.py init-db
```

(or run the app once, which will also create tables automatically.)

4. **Run the development server**:

```bash
flask --app app.py run
```

By default the app runs on:

> http://127.0.0.1:5000/

5. **Register a new user**, then log in and start adding properties.

> Uploaded images will be stored in `static/uploads/`.

---

## 4. Environment variables (optional for production)

For local testing, `SECRET_KEY` and the SQLite URL are hardcoded in `app.py`.

For production / AWS:

- Set environment variable `SECRET_KEY` and read it in `app.py`.
- Update `SQLALCHEMY_DATABASE_URI` to point to your RDS instance if you use MySQL/PostgreSQL.

---

## 5. Notes for AWS Deployment (Elastic Beanstalk)

- Zip the project contents (including `app.py`, `requirements.txt`, `templates`, `static`).
- Create a **Python** web server environment in Elastic Beanstalk.
- Upload the ZIP as your application version.
- Make sure the `static/uploads` directory exists (EB will create it if included in the ZIP).

This project is a good base for demonstrating:

- Cloud-hosted property management
- CRUD operations
- Input validation and secure password storage
- A nice blue cloud-themed UI
