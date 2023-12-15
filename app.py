from flask import Flask, render_template
from main import paknsave_search

app = Flask(__name__)

@app.route('/')
def home():
    products = paknsave_search('eggs')
    return render_template('home.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
