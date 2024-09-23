from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contact.db"
app.config["SECRET_KEY"] = "secret_key_here"  # Add a secret key for CSRF protection
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False, unique=True)
  message = db.Column(db.Text, nullable=False)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
  name = request.form["name"]
  email = request.form["email"]
  message = request.form["message"]
  contact = Contact(name=name, email=email, message=message)
  db.session.add(contact)
  db.session.commit()
  return "Message sent successfully!"

if __name__ == "__main__":
  db.create_all()  # Create the database tables
  app.run(debug=True)  # Start the Flask development server