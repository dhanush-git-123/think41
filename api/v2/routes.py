from flask import Blueprint, jsonify

v2_bp = Blueprint('v2', __name__)

@v2_bp.route('/products', methods=['GET'])
def get_products_v2():
    return jsonify({
        "products": [
            {"name": "Laptop", "price": 999},
            {"name": "Phone", "price": 499}
        ],
        "version": "v2"
    })
