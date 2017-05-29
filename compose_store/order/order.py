from flask import Flask, jsonify, request
import requests

app = Flask("order")


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/place_order', methods=['POST'])
def place_order():
    return process_order(request.form['customerid'],
                         request.form['productid'])


def process_order(customer_id, product_id):
    customer_req = requests.get('http://customer:5000/customer/{}'.format(
        customer_id))
    product_req = requests.get('http://product:5000/product/{}'.format(
        product_id))
    customer = customer_req.json()
    product = product_req.json()
    response = customer.copy()
    response.update(product)
    print(response)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
