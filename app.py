from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['online_store']
products_collection = db['products']

@app.route('/products', methods=['GET'])
def get_products():
    products = list(products_collection.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products)

@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products_collection.find_one({'_id': ObjectId(product_id)})
    product['_id'] = str(product['_id'])
    return jsonify(product)

@app.route('/product', methods=['POST'])
def add_product():
    product = request.json
    products_collection.insert_one(product)
    return 'Product added', 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
