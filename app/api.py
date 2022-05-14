from flask import request, jsonify
from app import app
from app.db import DB
from app.services.ml import MlService
from app.services.image import ImageService
from app.services.user import UserService
from app.services.product import ProductService

db = DB()
mlService = MlService()
imageService = ImageService()
userService = UserService()
productService = ProductService()

@app.route('/uploads/<path:path>')
def serve_image(path):
    try:
        return imageService.serve_img(path)
    except Exception as e:
        print(e)
    
    return {}

# NOTICE: For testing!
@app.route('/reset')
def reset():
    db.reset_db()
    return {}

@app.route('/user/register', methods = ["POST"])
def register_user():
    if ('file' not in request.files) or (not request.files['file']):
        return "No image sent", 400
    if ('user' not in request.form) or (not request.form['user']):
        return "No user set", 400

    file = request.files['file']
    user = request.form['user']
    img = None

    # if (not db.user_exist(user)):
    #     return "User doesnt exist", 403
    if (db.registered_exist(user)):
        return "User already registered", 403

    try:
        img = mlService.process_img(file)
        embedding = mlService.get_embedding(img)
        db.save_db(embedding, user)

        info = userService.get_info(user)

        imageService.save_img(img, info['nickname'])

        return jsonify(token=user, info=info)
    except Exception as e:
        print(e)

    return {}

@app.route('/user/login', methods = ["POST"])
def login_user():
    if 'user' not in request.files:
        return "No image sent", 400

    try:
        file = request.files['user']
        img = mlService.process_img(file)
        embedding = mlService.get_embedding(img)
        user = db.find_user(embedding)
        if (user):
            info = userService.get_info(user)

            return jsonify(token=user, info=info)
    except Exception as e:
        print(e)

    return {}

@app.route('/user/balance')
def get_balance():
    try:
        if (not request.headers.get('token')):
            return "No user id sent", 400
    except Exception as e:
        print(e)

    user = request.headers['token']

    try:
        balance = userService.get_balance(user)
        return balance
    except Exception as e:
        print(e)


@app.route('/product/list')
def get_products():
    try:
        if (not request.headers.get('token')):
            return "No user id sent", 400
    except Exception as e:
        print(e)

    user = request.headers['token']

    try:
        products = productService.get_all_products(user)
        return products
    except Exception as e:
        print(e)

    return {}

@app.route('/product/purchase', methods = ["POST"])
def purchase_products():
    if ('products' not in request.get_json()):
        return "No products purchased", 400
    if (not request.headers.get('token')):
        return "No user id sent", 400

    products = request.get_json()
    user = request.headers['token']

    try:
        productService.purchase_products(user, products)
    except Exception as e:
        print(e)

    return {}
