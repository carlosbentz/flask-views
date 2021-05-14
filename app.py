from flask import Flask, request, jsonify
from environs import Env
from flask.json import jsonify
from komercio import lista_de_produtos

env = Env()
env.read_env()
app = Flask(__name__)
DEVELOPMENT_MODE = env('FLASK_ENV')
DEBUG = env('DEBUG')


@app.route('/products')
def list_products():
    page = request.args.get('page', type=int) or 1
    per_page = request.args.get('per_page', type=int) or 30
    actual_page = page * per_page
    previous_page = (page -1) * per_page

    if per_page > 29:
        return jsonify(lista_de_produtos)

    return jsonify([product for i, product in enumerate(lista_de_produtos) if i >= previous_page and i < actual_page])


@app.route('/products/<int:product_id>')
def get_product(product_id: int):
    product = [product for product in lista_de_produtos if product["id"] == product_id]

    if product:
        return product[0]

    return {"error": "Product not found"}, 404