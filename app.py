# import os
<<<<<<< HEAD
# from datetime import datetime
# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
=======
# from datetime import datetime, date
# from flask import (
#     Flask,
#     render_template,
#     request,
#     redirect,
#     url_for,
#     flash,
#     session,
#     send_from_directory,
# )
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from werkzeug.utils import secure_filename

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
<<<<<<< HEAD
# app.config["SECRET_KEY"] = "change-this-in-production"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "property_app.db")
=======
# # SECURITY: use env var or random key (no hardcoded secret)
# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", os.urandom(24))
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
#     BASE_DIR, "property_app.db"
# )
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# UPLOAD_FOLDER = os.path.join("static", "uploads")
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# db = SQLAlchemy(app)

<<<<<<< HEAD
=======
# # ================================================================
# #                           MODELS
# # ================================================================

>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)


# class Property(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
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


=======

#     # Public-facing data
#     title = db.Column(db.String(150), nullable=False)
#     description = db.Column(db.Text, nullable=False)

#     # Full private address
#     address = db.Column(db.String(255), nullable=False)

#     city = db.Column(db.String(100), nullable=False)
#     short_address = db.Column(db.String(255))  # public-friendly location text

#     monthly_rent = db.Column(db.Float, nullable=False)
#     status = db.Column(db.String(50), default="Available")  # Available / Booked / etc.

#     image_filename = db.Column(db.String(255))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     # Visibility + contact
#     is_public = db.Column(db.Boolean, default=True)
#     contact_phone = db.Column(db.String(50))
#     contact_email = db.Column(db.String(120))

#     owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     owner = db.relationship("User", backref="properties")


# class Enquiry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     property_id = db.Column(db.Integer, db.ForeignKey("property.id"), nullable=False)

#     name = db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     phone = db.Column(db.String(50))
#     message = db.Column(db.Text)

#     status = db.Column(db.String(50), default="New")  # New / In Progress / Closed
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     property = db.relationship("Property", backref="enquiries")


# class Booking(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     property_id = db.Column(db.Integer, db.ForeignKey("property.id"), nullable=False)

#     guest_name = db.Column(db.String(120), nullable=False)
#     guest_email = db.Column(db.String(120), nullable=False)
#     guest_phone = db.Column(db.String(50))
#     move_in_date = db.Column(db.Date, nullable=False)

#     status = db.Column(
#         db.String(50), default="Confirmed"
#     )  # Pending / Confirmed / Cancelled / Completed
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     property = db.relationship("Property", backref="bookings")


# # ================================================================
# #                        HELPERS
# # ================================================================


>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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


<<<<<<< HEAD
# @app.route("/")
# def index():
#     user = current_user()
#     if not user:
#         return redirect(url_for("login"))
#     properties = Property.query.filter_by(owner_id=user.id).order_by(Property.created_at.desc()).all()
=======
# # ================================================================
# #                     PUBLIC PROPERTY PAGES
# # ================================================================


# @app.route("/properties")
# def public_properties():
#     """Public list of properties."""
#     props = (
#         Property.query
#         .filter(Property.status == "Available")
#         .order_by(Property.created_at.desc())
#         .all()
#     )
#     return render_template("public_list.html", properties=props)



# @app.route("/properties/<int:property_id>")
# def public_property_detail(property_id):
#     """Public property detail page (no login)."""
#     prop = Property.query.get_or_404(property_id)
#     if not prop.is_public:
#         flash("This property is not available for public viewing.", "warning")
#         return redirect(url_for("public_properties"))
#     return render_template("public_detail.html", prop=prop)


# @app.route("/properties/<int:property_id>/enquire", methods=["GET", "POST"])
# def public_enquire(property_id):
#     """Public enquiry form for a property."""
#     prop = Property.query.get_or_404(property_id)
#     if not prop.is_public:
#         flash("This property is not available for enquiries.", "warning")
#         return redirect(url_for("public_property_detail", property_id=property_id))

#     if request.method == "POST":
#         name = request.form.get("name", "").strip()
#         email = request.form.get("email", "").strip()
#         phone = request.form.get("phone", "").strip()
#         message = request.form.get("message", "").strip()

#         if not name or not email:
#             flash("Name and email are required to submit an enquiry.", "danger")
#             return redirect(url_for("public_enquire", property_id=property_id))

#         enquiry = Enquiry(
#             property_id=prop.id,
#             name=name,
#             email=email,
#             phone=phone,
#             message=message,
#         )
#         db.session.add(enquiry)
#         db.session.commit()

#         flash(
#             "Thank you! Your enquiry has been submitted. The owner will contact you soon.",
#             "success",
#         )
#         return redirect(url_for("public_property_detail", property_id=property_id))

#     return render_template("public_enquiry.html", prop=prop)


# # -------------------- PUBLIC BOOKING FLOW ------------------------


# @app.route("/properties/<int:property_id>/book", methods=["GET", "POST"])
# def public_book(property_id):
#     """Public booking form for a property."""
#     prop = Property.query.get_or_404(property_id)

#     if not prop.is_public:
#         flash("This property is not available for booking.", "warning")
#         return redirect(url_for("public_property_detail", property_id=property_id))

#     if prop.status != "Available":
#         flash("This property is not available anymore.", "danger")
#         return redirect(url_for("public_property_detail", property_id=property_id))

#     if request.method == "POST":
#         guest_name = request.form.get("guest_name", "").strip()
#         guest_email = request.form.get("guest_email", "").strip()
#         guest_phone = request.form.get("guest_phone", "").strip()
#         move_in_str = request.form.get("move_in_date", "").strip()

#         if not guest_name or not guest_email or not move_in_str:
#             flash("Name, email and move-in date are required.", "danger")
#             return redirect(url_for("public_book", property_id=property_id))

#         try:
#             move_in_date_val = datetime.strptime(move_in_str, "%Y-%m-%d").date()
#         except ValueError:
#             flash("Invalid move-in date format.", "danger")
#             return redirect(url_for("public_book", property_id=property_id))

#         booking = Booking(
#             property_id=prop.id,
#             guest_name=guest_name,
#             guest_email=guest_email,
#             guest_phone=guest_phone,
#             move_in_date=move_in_date_val,
#             status="Confirmed",
#         )

#         # mark property as booked
#         prop.status = "Booked"

#         db.session.add(booking)
#         db.session.commit()

#         flash("Your booking has been confirmed!", "success")
#         return redirect(url_for("booking_confirmation", booking_id=booking.id))

#     return render_template("booking_form.html", prop=prop)


# @app.route("/booking/<int:booking_id>/confirmation")
# def booking_confirmation(booking_id):
#     """Show confirmation with full address and contact."""
#     booking = Booking.query.get_or_404(booking_id)
#     prop = booking.property
#     return render_template("booking_confirmation.html", booking=booking, prop=prop)


# # ================================================================
# #                     OWNER DASHBOARD / AUTH
# # ================================================================


# @app.route("/")
# def index():
#     """Owner dashboard: requires login."""
#     user = current_user()
#     if not user:
#         return redirect(url_for("login"))

#     properties = (
#         Property.query.filter_by(owner_id=user.id)
#         .order_by(Property.created_at.desc())
#         .all()
#     )
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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
<<<<<<< HEAD
=======

>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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


<<<<<<< HEAD
# @app.route("/properties/new", methods=["GET", "POST"])
=======
# # ================================================================
# #                      OWNER PROPERTY CRUD
# # ================================================================


# @app.route("/dashboard/properties/new", methods=["GET", "POST"])
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
# def create_property():
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     if request.method == "POST":
#         title = request.form.get("title", "").strip()
#         description = request.form.get("description", "").strip()
#         address = request.form.get("address", "").strip()
<<<<<<< HEAD
#         city = request.form.get("city", "").strip()
#         monthly_rent = request.form.get("monthly_rent", "").strip()
#         status = request.form.get("status", "Available")

#         if not title or not description or not address or not city or not monthly_rent:
#             flash("All fields are required.", "danger")
=======
#         short_address = request.form.get("short_address", "").strip()
#         city = request.form.get("city", "").strip()
#         contact_phone = request.form.get("contact_phone", "").strip()
#         contact_email = request.form.get("contact_email", "").strip()
#         monthly_rent = request.form.get("monthly_rent", "").strip()
#         status = request.form.get("status", "Available")
#         is_public = request.form.get("is_public") == "on"

#         if not title or not description or not address or not city or not monthly_rent:
#             flash("Title, description, address, city and rent are required.", "danger")
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
#             return redirect(url_for("create_property"))

#         try:
#             monthly_rent_val = float(monthly_rent)
#             if monthly_rent_val <= 0:
#                 raise ValueError
#         except ValueError:
#             flash("Monthly rent must be a positive number.", "danger")
#             return redirect(url_for("create_property"))

<<<<<<< HEAD
=======
#         # Image upload
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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
<<<<<<< HEAD
=======
#             short_address=short_address,
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
#             city=city,
#             monthly_rent=monthly_rent_val,
#             status=status,
#             image_filename=image_filename,
<<<<<<< HEAD
#             owner_id=user.id,
#         )
=======
#             contact_phone=contact_phone,
#             contact_email=contact_email,
#             is_public=is_public,
#             owner_id=user.id,
#         )

>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
#         db.session.add(prop)
#         db.session.commit()
#         flash("Property created successfully.", "success")
#         return redirect(url_for("index"))

#     return render_template("property_form.html", mode="create")


<<<<<<< HEAD
# @app.route("/properties/<int:property_id>")
# def property_detail(property_id):
=======
# @app.route("/dashboard/properties/<int:property_id>")
# def property_detail(property_id):
#     """Owner-only property detail."""
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     prop = Property.query.get_or_404(property_id)
#     if prop.owner_id != user.id:
#         flash("You are not authorized to view this property.", "danger")
#         return redirect(url_for("index"))

#     return render_template("property_detail.html", prop=prop)


<<<<<<< HEAD
# @app.route("/properties/<int:property_id>/edit", methods=["GET", "POST"])
=======
# @app.route("/dashboard/properties/<int:property_id>/edit", methods=["GET", "POST"])
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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
<<<<<<< HEAD
#         city = request.form.get("city", "").strip()
#         monthly_rent = request.form.get("monthly_rent", "").strip()
#         status = request.form.get("status", "Available")

#         if not title or not description or not address or not city or not monthly_rent:
#             flash("All fields are required.", "danger")
=======
#         short_address = request.form.get("short_address", "").strip()
#         city = request.form.get("city", "").strip()
#         contact_phone = request.form.get("contact_phone", "").strip()
#         contact_email = request.form.get("contact_email", "").strip()
#         monthly_rent = request.form.get("monthly_rent", "").strip()
#         status = request.form.get("status", "Available")
#         is_public = request.form.get("is_public") == "on"

#         if not title or not description or not address or not city or not monthly_rent:
#             flash("Title, description, address, city and rent are required.", "danger")
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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
<<<<<<< HEAD
#                 flash("Invalid image file type. Allowed: png, jpg, jpeg, gif.", "danger")
=======
#                 flash(
#                     "Invalid image file type. Allowed: png, jpg, jpeg, gif.",
#                     "danger",
#                 )
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
#                 return redirect(url_for("edit_property", property_id=prop.id))

#         prop.title = title
#         prop.description = description
#         prop.address = address
<<<<<<< HEAD
#         prop.city = city
#         prop.monthly_rent = monthly_rent_val
#         prop.status = status
=======
#         prop.short_address = short_address
#         prop.city = city
#         prop.monthly_rent = monthly_rent_val
#         prop.status = status
#         prop.contact_phone = contact_phone
#         prop.contact_email = contact_email
#         prop.is_public = is_public
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)

#         db.session.commit()
#         flash("Property updated successfully.", "success")
#         return redirect(url_for("property_detail", property_id=prop.id))

#     return render_template("property_form.html", mode="edit", prop=prop)


<<<<<<< HEAD
# @app.route("/properties/<int:property_id>/delete", methods=["POST"])
=======
# @app.route("/dashboard/properties/<int:property_id>/delete", methods=["POST"])
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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


<<<<<<< HEAD
=======
# # ================================================================
# #                     OWNER ENQUIRY VIEW
# # ================================================================


# @app.route("/dashboard/enquiries")
# def owner_enquiries():
#     """View all enquiries for the logged-in owner's properties."""
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     enquiries = (
#         Enquiry.query.join(Property)
#         .filter(Property.owner_id == user.id)
#         .order_by(Enquiry.created_at.desc())
#         .all()
#     )
#     return render_template("owner_enquiries.html", enquiries=enquiries)


# @app.route("/dashboard/enquiries/<int:enquiry_id>/status", methods=["POST"])
# def update_enquiry_status(enquiry_id):
#     """Simple endpoint to update enquiry status."""
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     enquiry = Enquiry.query.get_or_404(enquiry_id)
#     if enquiry.property.owner_id != user.id:
#         flash("You are not authorized to update this enquiry.", "danger")
#         return redirect(url_for("owner_enquiries"))

#     new_status = request.form.get("status", "New")
#     enquiry.status = new_status
#     db.session.commit()
#     flash("Enquiry status updated.", "success")
#     return redirect(url_for("owner_enquiries"))


# # ================================================================
# #                     OWNER BOOKINGS VIEW
# # ================================================================


# @app.route("/dashboard/bookings")
# def owner_bookings():
#     """View all bookings for the logged-in owner's properties."""
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     bookings = (
#         Booking.query.join(Property)
#         .filter(Property.owner_id == user.id)
#         .order_by(Booking.created_at.desc())
#         .all()
#     )
#     return render_template("owner_bookings.html", bookings=bookings)


# @app.route("/dashboard/bookings/<int:booking_id>/status", methods=["POST"])
# def update_booking_status(booking_id):
#     """Update booking status and optionally free/lock the property."""
#     user = current_user()
#     if not user:
#         flash("Please log in first.", "warning")
#         return redirect(url_for("login"))

#     booking = Booking.query.get_or_404(booking_id)
#     if booking.property.owner_id != user.id:
#         flash("You are not authorized to update this booking.", "danger")
#         return redirect(url_for("owner_bookings"))

#     new_status = request.form.get("status", "Confirmed")
#     booking.status = new_status

#     # sync property status
#     if new_status in ("Cancelled", "Completed"):
#         booking.property.status = "Available"
#     else:
#         booking.property.status = "Booked"

#     db.session.commit()
#     flash("Booking status updated.", "success")
#     return redirect(url_for("owner_bookings"))


# # ================================================================
# #                     FILE SERVING / DB INIT
# # ================================================================


>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
# @app.route("/uploads/<filename>")
# def uploaded_file(filename):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# @app.cli.command("init-db")
# def init_db():
<<<<<<< HEAD
#     """Initialize the database tables."""
#     db.create_all()
#     print("Database tables created.")


=======
#     db.create_all()
#     print("Database tables created / updated.")


# # ================================================================
# #                         RUN (DEV)
# # ================================================================

>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
<<<<<<< HEAD
#     app.run(debug=True, host="0.0.0.0", port=5000)
import os
from datetime import datetime
=======
#     app.run(host="127.0.0.1", port=5000)
import os
from datetime import datetime, date
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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
<<<<<<< HEAD
# Use environment variable in production; fall back to a random value for dev
=======
# SECURITY: use env var or random key (no hardcoded secret)
>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", os.urandom(24))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    BASE_DIR, "property_app.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

UPLOAD_FOLDER = os.path.join("static", "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

db = SQLAlchemy(app)

# ================================================================
#                           MODELS
# ================================================================


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Public-facing data
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Full private address
    address = db.Column(db.String(255), nullable=False)

    city = db.Column(db.String(100), nullable=False)
    short_address = db.Column(db.String(255))  # public-friendly location text

    monthly_rent = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="Available")  # Available / Booked / etc.

    image_filename = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Visibility + contact (we keep the fields, but we DO NOT filter on them now)
    is_public = db.Column(db.Boolean, default=True)
    contact_phone = db.Column(db.String(50))
    contact_email = db.Column(db.String(120))

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    owner = db.relationship("User", backref="properties")


class Enquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey("property.id"), nullable=False)

    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(50))
    message = db.Column(db.Text)

    status = db.Column(db.String(50), default="New")  # New / In Progress / Closed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    property = db.relationship("Property", backref="enquiries")


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey("property.id"), nullable=False)

    guest_name = db.Column(db.String(120), nullable=False)
    guest_email = db.Column(db.String(120), nullable=False)
    guest_phone = db.Column(db.String(50))
    move_in_date = db.Column(db.Date, nullable=False)

    status = db.Column(
        db.String(50), default="Confirmed"
    )  # Pending / Confirmed / Cancelled / Completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    property = db.relationship("Property", backref="bookings")


# ================================================================
#                        HELPERS
# ================================================================


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


# ================================================================
#                     PUBLIC PROPERTY PAGES
# ================================================================


@app.route("/")
def home():
    """
    Public homepage: show ALL properties, no login required.
    """
    props = (
        Property.query
        .order_by(Property.created_at.desc())
        .all()
    )
    return render_template("public_list.html", properties=props)


@app.route("/properties")
def public_properties():
    """Public list of properties (same as home, different URL)."""
    props = (
        Property.query
        .order_by(Property.created_at.desc())
        .all()
    )
    return render_template("public_list.html", properties=props)


@app.route("/properties/<int:property_id>")
def public_property_detail(property_id):
    """Public property detail page (no login)."""
    prop = Property.query.get_or_404(property_id)
    # NO is_public check – show all existing properties
    return render_template("public_detail.html", prop=prop)


@app.route("/properties/<int:property_id>/enquire", methods=["GET", "POST"])
def public_enquire(property_id):
    """Public enquiry form for a property."""
    prop = Property.query.get_or_404(property_id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email:
            flash("Name and email are required to submit an enquiry.", "danger")
            return redirect(url_for("public_enquire", property_id=property_id))

        enquiry = Enquiry(
            property_id=prop.id,
            name=name,
            email=email,
            phone=phone,
            message=message,
        )
        db.session.add(enquiry)
        db.session.commit()

        flash(
            "Thank you! Your enquiry has been submitted. The owner will contact you soon.",
            "success",
        )
        return redirect(url_for("public_property_detail", property_id=property_id))

    return render_template("public_enquiry.html", prop=prop)


# -------------------- PUBLIC BOOKING FLOW ------------------------


@app.route("/properties/<int:property_id>/book", methods=["GET", "POST"])
def public_book(property_id):
    """Public booking form for a property."""
    prop = Property.query.get_or_404(property_id)

    # Even if status is not 'Available', we still give friendly message
    if prop.status != "Available":
        flash("This property is not available anymore.", "danger")
        return redirect(url_for("public_property_detail", property_id=property_id))

    if request.method == "POST":
        guest_name = request.form.get("guest_name", "").strip()
        guest_email = request.form.get("guest_email", "").strip()
        guest_phone = request.form.get("guest_phone", "").strip()
        move_in_str = request.form.get("move_in_date", "").strip()

        if not guest_name or not guest_email or not move_in_str:
            flash("Name, email and move-in date are required.", "danger")
            return redirect(url_for("public_book", property_id=property_id))

        try:
            move_in_date_val = datetime.strptime(move_in_str, "%Y-%m-%d").date()
        except ValueError:
            flash("Invalid move-in date format.", "danger")
            return redirect(url_for("public_book", property_id=property_id))

        booking = Booking(
            property_id=prop.id,
            guest_name=guest_name,
            guest_email=guest_email,
            guest_phone=guest_phone,
            move_in_date=move_in_date_val,
            status="Confirmed",
        )

        # mark property as booked
        prop.status = "Booked"

        db.session.add(booking)
        db.session.commit()

        flash("Your booking has been confirmed!", "success")
        return redirect(url_for("booking_confirmation", booking_id=booking.id))

    return render_template("booking_form.html", prop=prop)


@app.route("/booking/<int:booking_id>/confirmation")
def booking_confirmation(booking_id):
    """Show confirmation with full address and contact."""
    booking = Booking.query.get_or_404(booking_id)
    prop = booking.property
    return render_template("booking_confirmation.html", booking=booking, prop=prop)


# ================================================================
#                     OWNER DASHBOARD / AUTH
# ================================================================


@app.route("/dashboard")
def index():
    """
    Owner dashboard: requires login.
    NOTE: endpoint name is 'index' so url_for('index') -> /dashboard
    """
    user = current_user()
    if not user:
        return redirect(url_for("login"))
<<<<<<< HEAD
=======

>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)
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


# ================================================================
#                      OWNER PROPERTY CRUD
# ================================================================


@app.route("/dashboard/properties/new", methods=["GET", "POST"])
def create_property():
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        address = request.form.get("address", "").strip()
        short_address = request.form.get("short_address", "").strip()
        city = request.form.get("city", "").strip()
        contact_phone = request.form.get("contact_phone", "").strip()
        contact_email = request.form.get("contact_email", "").strip()
        monthly_rent = request.form.get("monthly_rent", "").strip()
        status = request.form.get("status", "Available")
        is_public = request.form.get("is_public") == "on"

        if not title or not description or not address or not city or not monthly_rent:
            flash("Title, description, address, city and rent are required.", "danger")
            return redirect(url_for("create_property"))

        try:
            monthly_rent_val = float(monthly_rent)
            if monthly_rent_val <= 0:
                raise ValueError
        except ValueError:
            flash("Monthly rent must be a positive number.", "danger")
            return redirect(url_for("create_property"))

        # Image upload
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
            short_address=short_address,
            city=city,
            monthly_rent=monthly_rent_val,
            status=status,
            image_filename=image_filename,
            contact_phone=contact_phone,
            contact_email=contact_email,
            is_public=is_public,
            owner_id=user.id,
        )

        db.session.add(prop)
        db.session.commit()
        flash("Property created successfully.", "success")
        return redirect(url_for("index"))

    return render_template("property_form.html", mode="create")


@app.route("/dashboard/properties/<int:property_id>")
def property_detail(property_id):
    """Owner-only property detail."""
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    prop = Property.query.get_or_404(property_id)
    if prop.owner_id != user.id:
        flash("You are not authorized to view this property.", "danger")
        return redirect(url_for("index"))

    return render_template("property_detail.html", prop=prop)


@app.route("/dashboard/properties/<int:property_id>/edit", methods=["GET", "POST"])
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
        short_address = request.form.get("short_address", "").strip()
        city = request.form.get("city", "").strip()
        contact_phone = request.form.get("contact_phone", "").strip()
        contact_email = request.form.get("contact_email", "").strip()
        monthly_rent = request.form.get("monthly_rent", "").strip()
        status = request.form.get("status", "Available")
        is_public = request.form.get("is_public") == "on"

        if not title or not description or not address or not city or not monthly_rent:
            flash("Title, description, address, city and rent are required.", "danger")
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
        prop.short_address = short_address
        prop.city = city
        prop.monthly_rent = monthly_rent_val
        prop.status = status
        prop.contact_phone = contact_phone
        prop.contact_email = contact_email
        prop.is_public = is_public

        db.session.commit()
        flash("Property updated successfully.", "success")
        return redirect(url_for("property_detail", property_id=prop.id))

    return render_template("property_form.html", mode="edit", prop=prop)


@app.route("/dashboard/properties/<int:property_id>/delete", methods=["POST"])
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


# ================================================================
#                     OWNER ENQUIRY VIEW
# ================================================================


@app.route("/dashboard/enquiries")
def owner_enquiries():
    """View all enquiries for the logged-in owner's properties."""
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    enquiries = (
        Enquiry.query.join(Property)
        .filter(Property.owner_id == user.id)
        .order_by(Enquiry.created_at.desc())
        .all()
    )
    return render_template("owner_enquiries.html", enquiries=enquiries)


@app.route("/dashboard/enquiries/<int:enquiry_id>/status", methods=["POST"])
def update_enquiry_status(enquiry_id):
    """Simple endpoint to update enquiry status."""
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    enquiry = Enquiry.query.get_or_404(enquiry_id)
    if enquiry.property.owner_id != user.id:
        flash("You are not authorized to update this enquiry.", "danger")
        return redirect(url_for("owner_enquiries"))

    new_status = request.form.get("status", "New")
    enquiry.status = new_status
    db.session.commit()
    flash("Enquiry status updated.", "success")
    return redirect(url_for("owner_enquiries"))


# ================================================================
#                     OWNER BOOKINGS VIEW
# ================================================================


@app.route("/dashboard/bookings")
def owner_bookings():
    """View all bookings for the logged-in owner's properties."""
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    bookings = (
        Booking.query.join(Property)
        .filter(Property.owner_id == user.id)
        .order_by(Booking.created_at.desc())
        .all()
    )
    return render_template("owner_bookings.html", bookings=bookings)


@app.route("/dashboard/bookings/<int:booking_id>/status", methods=["POST"])
def update_booking_status(booking_id):
    """Update booking status and optionally free/lock the property."""
    user = current_user()
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for("login"))

    booking = Booking.query.get_or_404(booking_id)
    if booking.property.owner_id != user.id:
        flash("You are not authorized to update this booking.", "danger")
        return redirect(url_for("owner_bookings"))

    new_status = request.form.get("status", "Confirmed")
    booking.status = new_status

    # sync property status
    if new_status in ("Cancelled", "Completed"):
        booking.property.status = "Available"
    else:
        booking.property.status = "Booked"

    db.session.commit()
    flash("Booking status updated.", "success")
    return redirect(url_for("owner_bookings"))


# ================================================================
#                     FILE SERVING / DB INIT
# ================================================================


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.cli.command("init-db")
def init_db():
<<<<<<< HEAD
    """Initialize the database tables."""
    with app.app_context():
        db.create_all()
        print("Database tables created.")
=======
    db.create_all()
    print("Database tables created / updated.")

>>>>>>> 3b969b7 (Added booking system: booking form, confirmation page, and updated app.py)

# ================================================================
#                         RUN (DEV)
# ================================================================


if __name__ == "__main__":
    # Ensure DB tables exist for local dev. Production uses gunicorn.
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=5000)
