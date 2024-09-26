from flask import Flask, request, render_template, redirect, url_for, flash
import logging

# Setup logging to a file
logging.basicConfig(
    filename="honeypot.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Log the login attempt
        username = request.form.get("username")
        password = request.form.get("password")
        logging.info(
            f"Login attempt with username: {username} and password: {password} from {request.remote_addr}"
        )

        # Flash a message and return to the login page
        flash("Login unsuccessful..")
        flash("Your attempt has been logged!!")
        flash("Try again..")
        return redirect(url_for("login"))  # Redirect back to login page

    return render_template("login.html")


@app.route("/admin")
def admin():
    # Log the unauthorized access attempt
    logging.info(f"Unauthorized access attempt to /admin from: {request.remote_addr}")

    # Flash the forbidden message
    flash("Forbidden.")
    flash("This attempt has been logged.")

    # Render the admin page (which will show the message and redirect)
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
