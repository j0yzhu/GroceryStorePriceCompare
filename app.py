from flask import Flask, render_template, request
from main import paknsave_search, countdown_search, newworld_search

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_term = request.form['search_term']
    else:
        search_term = None

    countdown_products = countdown_search(search_term)
    newworld_products = newworld_search(search_term)
    paknsave_products = paknsave_search(search_term)

    return render_template('home.html',
                           search_term=search_term,
                           countdown_products=countdown_products,
                           newworld_products=newworld_products,
                           paknsave_products=paknsave_products)

if __name__ == '__main__':
    app.run(debug=True)
