import os
import re
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from config import Config
import data
import db

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

app = Flask(__name__)
app.config.from_object(Config)

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

PRODUCT_IMAGE_DIR = os.path.join(app.root_path, "static", "images", "products")
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".avif")


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


def product_image(slug):
    """Return the static path of a real product photo if one has been
    dropped into static/images/products/<slug>.(jpg|jpeg|png|webp), else None.
    Checked on every render so newly added images show up without a restart.
    """
    for ext in IMAGE_EXTENSIONS:
        if os.path.exists(os.path.join(PRODUCT_IMAGE_DIR, slug + ext)):
            return f"images/products/{slug}{ext}"
    return None


app.jinja_env.globals["product_image"] = product_image


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("customer_id"):
            flash("Please log in to continue.", "error")
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


@app.context_processor
def inject_globals():
    return {
        "company": data.COMPANY_INFO,
        "nav_categories": data.CATEGORIES,
        "current_customer_name": None if Config.STATIC_BUILD else session.get("customer_name"),
        "static_build": Config.STATIC_BUILD,
    }


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="GIO Electronics | Electronic Components Manufacturer",
        description="GIO Electronics provides precision electronic components, custom manufacturing, PCB assembly, testing, and engineering solutions for modern industries.",
        products=data.PRODUCTS[:6],
        trust_indicators=data.TRUST_INDICATORS,
        why_gio=data.WHY_GIO[:3],
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About Us | GIO Electronics",
        description="Learn about GIO Electronics, an electronics manufacturing and engineering company delivering reliable components and custom manufacturing solutions.",
        why_gio=data.WHY_GIO,
    )


@app.route("/products")
def products():
    category = request.args.get("category")
    if category:
        product_list = data.get_products_by_category(category)
    else:
        product_list = data.PRODUCTS
    return render_template(
        "products.html",
        title="Products | GIO Electronics",
        description="Explore GIO Electronics' range of electronic components across mobile, computing, consumer, appliance, and industrial categories.",
        products=product_list,
        categories=data.CATEGORIES,
        active_category=category,
    )


@app.route("/products/<slug>")
def product_detail(slug):
    product = data.get_product_by_slug(slug)
    if not product:
        return render_template("404.html", title="Product Not Found | GIO Electronics"), 404
    related = data.get_related_products(product)
    return render_template(
        "product_detail.html",
        title=f"{product['name']} | GIO Electronics",
        description=product["description"],
        product=product,
        related_products=related,
    )


@app.route("/services")
def services():
    return render_template(
        "services.html",
        title="Engineering & Manufacturing Services | GIO Electronics",
        description="GIO Electronics offers custom manufacturing, PCB assembly, prototype development, testing, and engineering services for businesses.",
        services=data.SERVICES,
    )


@app.route("/manufacturing")
def manufacturing():
    return render_template(
        "manufacturing.html",
        title="Manufacturing Process | GIO Electronics",
        description="From requirement to delivery, explore GIO Electronics' structured manufacturing process for electronic components.",
        steps=data.PROCESS_STEPS,
    )


@app.route("/quality")
def quality():
    return render_template(
        "quality.html",
        title="Quality | GIO Electronics",
        description="Quality is built into every stage of GIO Electronics' manufacturing process, from material inspection to final packaging.",
        quality_points=data.QUALITY_POINTS,
        trust_cards=data.QUALITY_TRUST_CARDS,
    )


@app.route("/industries")
def industries():
    return render_template(
        "industries.html",
        title="Industries We Serve | GIO Electronics",
        description="GIO Electronics serves mobile, computing, consumer electronics, appliance, industrial, automotive, telecom, and IoT industries.",
        industries=data.INDUSTRIES,
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        title="Contact Us | GIO Electronics",
        description="Get in touch with GIO Electronics for enquiries about electronic component manufacturing and engineering services.",
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if session.get("customer_id"):
        return redirect(url_for("account"))

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        company_name = request.form.get("company_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        errors = []
        if not full_name:
            errors.append("Full name is required.")
        if not company_name:
            errors.append("Company name is required.")
        if not EMAIL_RE.match(email):
            errors.append("Please enter a valid email address.")
        if len(password) < 8:
            errors.append("Password must be at least 8 characters.")
        if password != confirm_password:
            errors.append("Passwords do not match.")

        if not errors:
            new_id = db.create_customer({
                "full_name": full_name,
                "company_name": company_name,
                "email": email,
                "phone": phone,
                "password_hash": generate_password_hash(password),
            })
            if new_id is None:
                errors.append("An account with this email already exists. Try logging in instead.")

        if errors:
            for err in errors:
                flash(err, "error")
            return render_template(
                "signup.html",
                title="Create an Account | GIO Electronics",
                description="Create a GIO Electronics account to track your quote requests.",
                form_data=request.form,
            ), 400

        session["customer_id"] = new_id
        session["customer_name"] = full_name
        flash("Account created. Welcome to GIO Electronics.", "success")
        return redirect(url_for("account"))

    return render_template(
        "signup.html",
        title="Create an Account | GIO Electronics",
        description="Create a GIO Electronics account to track your quote requests.",
        form_data={},
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("customer_id"):
        return redirect(url_for("account"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        next_url = request.form.get("next") or url_for("account")

        customer = db.get_customer_by_email(email)
        if not customer or not check_password_hash(customer["password_hash"], password):
            flash("Incorrect email or password.", "error")
            return render_template(
                "login.html",
                title="Log In | GIO Electronics",
                description="Log in to your GIO Electronics account.",
                form_data=request.form,
                next=next_url,
            ), 400

        session["customer_id"] = customer["id"]
        session["customer_name"] = customer["full_name"]
        flash(f"Welcome back, {customer['full_name']}.", "success")
        return redirect(next_url)

    return render_template(
        "login.html",
        title="Log In | GIO Electronics",
        description="Log in to your GIO Electronics account.",
        form_data={},
        next=request.args.get("next", ""),
    )


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    customer = db.get_customer_by_id(session["customer_id"])
    enquiries = db.list_enquiries_for_customer(session["customer_id"])
    return render_template(
        "account.html",
        title="My Account | GIO Electronics",
        description="View your GIO Electronics account and submitted quote requests.",
        customer=customer,
        enquiries=enquiries,
    )


@app.route("/request-quote", methods=["GET", "POST"])
def request_quote():
    if request.method == "POST":
        name = request.form.get("full_name", "").strip()
        company_name = request.form.get("company_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        product_service = request.form.get("product_service", "").strip()
        quantity = request.form.get("quantity", "").strip()
        message = request.form.get("message", "").strip()

        errors = []
        if not name:
            errors.append("Full name is required.")
        if not company_name:
            errors.append("Company name is required.")
        if not email:
            errors.append("Email is required.")
        if not phone:
            errors.append("Phone number is required.")
        if not message:
            errors.append("Please describe your requirement.")

        attachment_name = ""
        file = request.files.get("attachment")
        if file and file.filename:
            if allowed_file(file.filename):
                attachment_name = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], attachment_name))
            else:
                errors.append("Attachment must be a PDF, image, DWG/DXF, or ZIP file.")

        if errors:
            for err in errors:
                flash(err, "error")
            return render_template(
                "quote.html",
                title="Request a Quote | GIO Electronics",
                description="Request a quote from GIO Electronics for electronic component manufacturing and engineering services.",
                products=data.PRODUCTS,
                form_data=request.form,
            ), 400

        try:
            db.save_enquiry({
                "customer_id": session.get("customer_id"),
                "name": name,
                "company_name": company_name,
                "email": email,
                "phone": phone,
                "product_service": product_service,
                "quantity": quantity,
                "message": message,
                "attachment": attachment_name,
            })
        except Exception:
            app.logger.exception("Failed to save enquiry to MySQL")
            flash("We couldn't submit your request right now. Please try again shortly.", "error")
            return render_template(
                "quote.html",
                title="Request a Quote | GIO Electronics",
                description="Request a quote from GIO Electronics for electronic component manufacturing and engineering services.",
                products=data.PRODUCTS,
                form_data=request.form,
            ), 500

        flash("Your quote request has been submitted. Our team will get back to you shortly.", "success")
        return redirect(url_for("request_quote"))

    preselected = request.args.get("product", "")
    form_data = {}
    if session.get("customer_id"):
        customer = db.get_customer_by_id(session["customer_id"])
        if customer:
            form_data = {
                "full_name": customer["full_name"],
                "company_name": customer["company_name"],
                "email": customer["email"],
                "phone": customer["phone"] or "",
            }

    return render_template(
        "quote.html",
        title="Request a Quote | GIO Electronics",
        description="Request a quote from GIO Electronics for electronic component manufacturing and engineering services.",
        products=data.PRODUCTS,
        preselected=preselected,
        form_data=form_data,
    )


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", title="Page Not Found | GIO Electronics"), 404


if __name__ == "__main__":
    app.run(debug=True)
