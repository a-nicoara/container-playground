from flask import Flask
from flask_restful import Api, Resource


class Customer:
    def __init__(self, customerid, name, address, email):
        self.customer_id = customerid
        self.name = name
        self.address = address
        self.email = email

    @property
    def get(self):
        return {'customerid': self.customer_id,
                'name': self.name,
                'address': self.address,
                'email': self.email}


class Customers(Resource):
    customers = {
        1: Customer(1, "Alice", "1234 Good St", "alice@wonderland.org"),
        2: Customer(2, "Bob", "1 Infinity Loop", "bob@apple.com"),
        3: Customer(3, "Eve", "1 Microsoft Way", "eve@microsoft.com")
    }

    def get(self, customer_id):
        return self.customers[customer_id].get


def main():
    app = Flask("customer")
    api = Api(app)
    api.add_resource(Customers, '/customer/<int:customer_id>')
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    main()
