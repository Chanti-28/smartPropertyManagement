# import os
# from datetime import datetime
# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from werkzeug.utils import secure_filename

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "change-this-in-production"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "property_app.db")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# UPLOAD_FOLDER = os.path.join("static", "uploads")
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)


# class Property(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     address = db.Column(db.String(255), nullable=False)
#     city = db.Column(db.String(100), nullable=False)
#     monthly_rent = db.Column(db.Float, nullable=False)
#     status = db.Column(db.String(50), default="Available")
#     image_filename = db.Column(db.String(255))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#     owner = db.relationship("User", backref="properties")


# def allowed_file(filename: str) -> bool:
#     return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# def current_user():
#     uid = session.get("user_id")
#     if uid is None:
#         return None
#     return User.query.get(uid)


# @app.context_processor
# def inject_user():
#     return {"current_user": current_user()}


# @app.route("/")
# def index():
#     user = current_user()
#     if not user:
#         return redirect(url_for("login"))
#     properties = Property.query.filter_by(owner_id=user.id).order_by(Property.created_at.desc()).all()
#     return render_template("index.html", properties=properties)


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         username = request.form.get("username", "").strip()
#         password = request.form.get("password", "")
#         confirm = request.form.get("confirm", "")

#         if not username or not password:
#             flash("Username and password are required.", "danger")
#             return redirect(url_for("register"))

#         if password != confirm:
#             flash("Passwords do not match.", "danger")
#             return redirect(url_for("register"))

#         existing = User.query.filter_by(username=username).first()
#         if existing:
#             flash("Username already taken. Please choose another.", "warning")
#             return redirect(url_for("register"))

#         hashed = generate_password_hash(password)
#         user = User(username=username, password_hash=hashed)
#         db.session.add(user)
#         db.session.commit()
#         flash("Registration successful. Please log in.", "success")
#         return redirect(url_for("login"))

#     return render_template("register.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username", "").strip()
#         password = request.form.get("password", "")

#         user = User.query.filter_by(username=username).first()
#         if not user or not check_password_hash(user.password_hash, password):
#             flash("Invalid username or password.", "danger")
#             return redirect(url_for("login"))

#         session["user_id"] = user.id
#         flash(f"Welcome back, {user.username}!", "success")
#         return redirect(url_for("index"))

#     return render_template("login.html")


# @app.route("/logout")
# def logout():
#     session.clear()
#     flash("You have been logged out.", "info")
#     return redirect(url_for("login"))


# @app.route("/properties/new", methods=["GET", "POST"])
# def create_property():
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     if request.method == "POST":
#         title = request.form.get("title", "").strip()
#         description = request.form.get("description", "").strip()
#         address = request.form.get("address", "").strip()
#         city = request.form.get("city", "").strip()
#         monthly_rent = request.form.get("monthly_rent", "").strip()
#         status = request.form.get("status", "Available")

#         if not title or not description or not address or not city or not monthly_rent:
#             flash("All fields are required.", "danger")
#             return redirect(url_for("create_property"))

#         try:
#             monthly_rent_val = float(monthly_rent)
#             if monthly_rent_val <= 0:
#                 raise ValueError
#         except ValueError:
#             flash("Monthly rent must be a positive number.", "danger")
#             return redirect(url_for("create_property"))

#         image_file = request.files.get("image")
#         image_filename = None
#         if image_file and image_file.filename:
#             if allowed_file(image_file.filename):
#                 filename = secure_filename(image_file.filename)
#                 os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
#                 save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#                 image_file.save(save_path)
#                 image_filename = filename
#             else:
#                 flash("Invalid image file type. Allowed: png, jpg, jpeg, gif.", "danger")
#                 return redirect(url_for("create_property"))

#         prop = Property(
#             title=title,
#             description=description,
#             address=address,
#             city=city,
#             monthly_rent=monthly_rent_val,
#             status=status,
#             image_filename=image_filename,
#             owner_id=user.id,
#         )
#         db.session.add(prop)
#         db.session.commit()
#         flash("Property created successfully.", "success")
#         return redirect(url_for("index"))

#     return render_template("property_form.html", mode="create")


# @app.route("/properties/<int:property_id>")
# def property_detail(property_id):
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     prop = Property.query.get_or_404(property_id)
#     if prop.owner_id != user.id:
#         flash("You are not authorized to view this property.", "danger")
#         return redirect(url_for("index"))

#     return render_template("property_detail.html", prop=prop)


# @app.route("/properties/<int:property_id>/edit", methods=["GET", "POST"])
# def edit_property(property_id):
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     prop = Property.query.get_or_404(property_id)
#     if prop.owner_id != user.id:
#         flash("You are not authorized to edit this property.", "danger")
#         return redirect(url_for("index"))

#     if request.method == "POST":
#         title = request.form.get("title", "").strip()
#         description = request.form.get("description", "").strip()
#         address = request.form.get("address", "").strip()
#         city = request.form.get("city", "").strip()
#         monthly_rent = request.form.get("monthly_rent", "").strip()
#         status = request.form.get("status", "Available")

#         if not title or not description or not address or not city or not monthly_rent:
#             flash("All fields are required.", "danger")
#             return redirect(url_for("edit_property", property_id=prop.id))

#         try:
#             monthly_rent_val = float(monthly_rent)
#             if monthly_rent_val <= 0:
#                 raise ValueError
#         except ValueError:
#             flash("Monthly rent must be a positive number.", "danger")
#             return redirect(url_for("edit_property", property_id=prop.id))

#         image_file = request.files.get("image")
#         if image_file and image_file.filename:
#             if allowed_file(image_file.filename):
#                 filename = secure_filename(image_file.filename)
#                 os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
#                 save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#                 image_file.save(save_path)
#                 prop.image_filename = filename
#             else:
#                 flash("Invalid image file type. Allowed: png, jpg, jpeg, gif.", "danger")
#                 return redirect(url_for("edit_property", property_id=prop.id))

#         prop.title = title
#         prop.description = description
#         prop.address = address
#         prop.city = city
#         prop.monthly_rent = monthly_rent_val
#         prop.status = status

#         db.session.commit()
#         flash("Property updated successfully.", "success")
#         return redirect(url_for("property_detail", property_id=prop.id))

#     return render_template("property_form.html", mode="edit", prop=prop)


# @app.route("/properties/<int:property_id>/delete", methods=["POST"])
# def delete_property(property_id):
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     prop = Property.query.get_or_404(property_id)
#     if prop.owner_id != user.id:
#         flash("You are not authorized to delete this property.", "danger")
#         return redirect(url_for("index"))

#     db.session.delete(prop)
#     db.session.commit()
#     flash("Property deleted successfully.", "success")
#     return redirect(url_for("index"))


# @app.route("/uploads/<filename>")
# def uploaded_file(filename):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# @app.cli.command("init-db")
# def init_db():
#     """Initialize the database tables."""
#     db.create_all()
#     print("Database tables created.")



# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True, host="0.0.0.0", port=5000)
import os
from datetime import datetime
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    send_from_directory,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Use environment variable in production; fall back to a random value for dev
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", os.urandom(24))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    BASE_DIR, "property_app.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

UPLOAD_FOLDER = os.path.join("static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    monthly_rent = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="Available")
    image_filename = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    owner = db.relationship("User", backref="properties")


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def current_user():
    uid = session.get("user_id")
    if uid is None:
        return None
    return User.query.get(uid)


@app.context_processor
def inject_user():
    return {"current_user": current_user()}


@app.route("/")
def index():
    user = current_user()
    if not user:
        return redirect(url_for("login"))
    properties = (
        Property.query.filter_by(owner_id=user.id)
        .order_by(Property.created_at.desc())
        .all()
    )
    return render_template("index.html", properties=properties)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")

        if not username or not password:
            flash("Username and password are required.", "danger")
            return redirect(url_for("register"))

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("register"))

        existing = User.query.filter_by(username=username).first()
        if existing:
            flash("Username already taken. Please choose another.", "warning")
            return redirect(url_for("register"))

        hashed = generate_password_hash(password)
        user = User(username=username, password_hash=hashed)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid username or password.", "danger")
            return redirect(url_for("login"))

        session["user_id"] = user.id
        flash(f"Welcome back, {user.username}!", "success")
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


@app.route("/properties/new", methods=["GET", "POST"])
def create_property():
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        address = request.form.get("address", "").strip()
        city = request.form.get("city", "").strip()
        monthly_rent = request.form.get("monthly_rent", "").strip()
        status = request.form.get("status", "Available")

        if not title or not description or not address or not city or not monthly_rent:
            flash("All fields are required.", "danger")
            return redirect(url_for("create_property"))

        try:
            monthly_rent_val = float(monthly_rent)
            if monthly_rent_val <= 0:
                raise ValueError
        except ValueError:
            flash("Monthly rent must be a positive number.", "danger")
            return redirect(url_for("create_property"))

        image_file = request.files.get("image")
        image_filename = None
        if image_file and image_file.filename:
            if allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                image_file.save(save_path)
                image_filename = filename
            else:
                flash(
                    "Invalid image file type. Allowed: png, jpg, jpeg, gif.",
                    "danger",
                )
                return redirect(url_for("create_property"))

        prop = Property(
            title=title,
            description=description,
            address=address,
            city=city,
            monthly_rent=monthly_rent_val,
            status=status,
            image_filename=image_filename,
            owner_id=user.id,
        )
        db.session.add(prop)
        db.session.commit()
        flash("Property created successfully.", "success")
        return redirect(url_for("index"))

    return render_template("property_form.html", mode="create")


@app.route("/properties/<int:property_id>")
def property_detail(property_id):
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    prop = Property.query.get_or_404(property_id)
    if prop.owner_id != user.id:
        flash("You are not authorized to view this property.", "danger")
        return redirect(url_for("index"))

    return render_template("property_detail.html", prop=prop)


@app.route("/properties/<int:property_id>/edit", methods=["GET", "POST"])
def edit_property(property_id):
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    prop = Property.query.get_or_404(property_id)
    if prop.owner_id != user.id:
        flash("You are not authorized to edit this property.", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        address = request.form.get("address", "").strip()
        city = request.form.get("city", "").strip()
        monthly_rent = request.form.get("monthly_rent", "").strip()
        status = request.form.get("status", "Available")

        if not title or not description or not address or not city or not monthly_rent:
            flash("All fields are required.", "danger")
            return redirect(url_for("edit_property", property_id=prop.id))

        try:
            monthly_rent_val = float(monthly_rent)
            if monthly_rent_val <= 0:
                raise ValueError
        except ValueError:
            flash("Monthly rent must be a positive number.", "danger")
            return redirect(url_for("edit_property", property_id=prop.id))

        image_file = request.files.get("image")
        if image_file and image_file.filename:
            if allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                image_file.save(save_path)
                prop.image_filename = filename
            else:
                flash(
                    "Invalid image file type. Allowed: png, jpg, jpeg, gif.",
                    "danger",
                )
                return redirect(url_for("edit_property", property_id=prop.id))

        prop.title = title
        prop.description = description
        prop.address = address
        prop.city = city
        prop.monthly_rent = monthly_rent_val
        prop.status = status

        db.session.commit()
        flash("Property updated successfully.", "success")
        return redirect(url_for("property_detail", property_id=prop.id))

    return render_template("property_form.html", mode="edit", prop=prop)


@app.route("/properties/<int:property_id>/delete", methods=["POST"])
def delete_property(property_id):
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    prop = Property.query.get_or_404(property_id)
    if prop.owner_id != user.id:
        flash("You are not authorized to delete this property.", "danger")
        return redirect(url_for("index"))

    db.session.delete(prop)
    db.session.commit()
    flash("Property deleted successfully.", "success")
    return redirect(url_for("index"))


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.cli.command("init-db")
def init_db():
    """Initialize the database tables."""
    with app.app_context():
        db.create_all()
        print("Database tables created.")


if __name__ == "__main__":
    # Ensure DB tables exist for local dev. Production uses gunicorn.
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=5000)
