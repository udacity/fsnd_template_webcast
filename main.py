from flask import Flask
app = Flask(__name__, template_folder='jeffs_templates')

from flask import render_template


@app.route('/')
def main_page():
    return render_template('base.html')


@app.route('/order')
def order_page():
    our_fruits = ['Apple', 'Banana', 'Orange', 'Grape', 'Lemon']
    return render_template('order.html', foods=our_fruits)


@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
