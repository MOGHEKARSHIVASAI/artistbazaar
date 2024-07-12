from flask import Flask, render_template, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from db import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Import models after db has been initialized
from models import User, Product, Artist, Cart

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/artist/<int:artist_id>')
def artist_profile(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    return render_template('artist_profile.html', artist=artist)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Implement login logic here
        pass
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Implement registration logic here
        pass
    return render_template('register.html')

@app.route('/user_dashboard')
def user_dashboard():
    # Implement user dashboard logic here
    return render_template('user_dashboard.html')

@app.route('/cart')
def cart():
    # Implement cart logic here
    return render_template('cart.html')

@app.route('/payment')
def payment():
    # Implement payment logic here
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True,port=4999)



