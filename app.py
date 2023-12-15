from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    products = paknsave_search('eggs')
    return render_template('home.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
