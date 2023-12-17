from flask import Flask, render_template, request
from main import paknsave_search, countdown_search, newworld_search

app = Flask(__name__)

def perform_search(search_term):
    countdown_products = countdown_search(search_term)
    newworld_products = newworld_search(search_term)
    paknsave_products = paknsave_search(search_term)
@app.route('/', methods=['GET'])
def home_get():
    search_term = request.args.get('search_term', default=None)
    countdown_products, newworld_products, paknsave_products = perform_search(search_term)


    return render_template('home.html',
                           search_term=search_term,
                           countdown_products=countdown_products,
                           newworld_products=newworld_products,
                           paknsave_products=paknsave_products)

@app.route('/', methods=['POST'])
def home_post():
    search_term = request.args.get('search_term')
    countdown_products, newworld_products, paknsave_products = perform_search(search_term)

    return render_template('home.html',
                           search_term=search_term,
                           countdown_products=countdown_products,
                           newworld_products=newworld_products,
                           paknsave_products=paknsave_products)

if __name__ == '__main__':
    app.run(debug=True)
