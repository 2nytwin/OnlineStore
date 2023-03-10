from flask import Flask, render_template
from flask import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://shop.db'
db = SQLAlchemy


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, primary_key=True)
    price = 0
    isActive = 0
    amount = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
