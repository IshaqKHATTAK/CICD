from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Add your routes and functionality for the Flask app
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add-user', methods=['POST'])
def add_user():
    email = request.form['email']
    new_user = User(email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('show_users.html', users=all_users)
