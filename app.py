from flask import Flask, jsonify, render_template, request, url_for
from extensions import db
from config import Config
from models import Product

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized"}), 401

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/get_products', methods=['GET'], strict_slashes=False)
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)
    
    products = Product.query.paginate(page=page, per_page=per_page)

    product_list = []
    for product in products.items:
        product_dict = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'image_url': product.image_url,
            'price': product.price
        }
        product_list.append(product_dict)

    next_page = url_for('get_products', page=products.next_num) if products.has_next else None
    prev_page = url_for('get_products', page=products.prev_num) if products.has_prev else None

    return render_template('views.html', products=product_list, next_page=next_page, prev_page=prev_page)

@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": "Forbidden"}), 403

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == "__main__":
    app.run()