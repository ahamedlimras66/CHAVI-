from flask import Blueprint
from model.order import Order

order = Blueprint("order", __name__)

orderObj = Order()

order.add_url_rule("/", view_func=orderObj.orderPage, methods=['GET'])