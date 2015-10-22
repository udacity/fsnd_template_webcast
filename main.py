from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Main Page'


@app.route('/order')
def order_page():
    return 'Order Page'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
