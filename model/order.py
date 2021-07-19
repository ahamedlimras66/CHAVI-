from flask import render_template

class Order:
    def orderPage(self):
        return render_template("order.html")