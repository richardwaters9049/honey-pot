from flask import Flask, request, render_template
import logging

# Setup logging to a file
logging.basicConfig(
    filename="honeypot.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

app = Flask(__name__)


@app.route("/")
def home():
    # Serve the landing page
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
        return "Login unsuccessful. Your attempt has been logged.", 403
    # Serve the login page
    return render_template("login.html")


@app.route("/admin")
def admin():
    logging.info(f"Attempt to access /admin from: {request.remote_addr}")
    return "Forbidden. This attempt has been logged.", 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
