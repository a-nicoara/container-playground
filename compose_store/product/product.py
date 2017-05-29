from flask import Flask
from flask_restful import Api, Resource


class Product:
    def __init__(self, productid, description, price):
        self.product_id = productid
        self.description = description
        self.price = price

    @property
    def get(self):
        return {'productid': self.product_id,
                'description': self.description,
                'price': self.price}


class Products(Resource):
    products = {
        1: Product(1, "Towel", 12.00),
        2: Product(2, "Glass", 6.00),
        3: Product(3, "Plate", 3.00)
    }

    def get(self, product_id):
        return self.products[product_id].get


def main():
    app = Flask("product")
    api = Api(app)
    api.add_resource(Products, '/product/<int:product_id>')
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    main()
