from flask import Flask, url_for
from route.home import home
from route.order import order

app = Flask(__name__)

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(order, url_prefix="/order")


if __name__ == "__main__":
    app.run(debug=True)