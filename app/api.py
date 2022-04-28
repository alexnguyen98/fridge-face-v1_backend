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

@app.route('/test')
def imageTest2():
    try:
        userService.get_info("4facf1ac-35ac-43b2-aa00-bdc62cb4ef23")
    except Exception as e:
        print(e)

    return {}

@app.route('/user/list')
def get_usernames():
    try:
        return jsonify(users=db.get_avaiable_users())
    except Exception as e:
        print(e)
    
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

@app.route('/product/<barcode>')
def scan_product(barcode):
    if (not barcode):
        return "No barcode sent", 400

    return jsonify(
        id=1, 
        max=5, 
        img="https://storage.googleapis.com/images-sof-prd-9fa6b8b.sof.prd.v8.commerce.mi9cloud.com/product-images/zoom/00059600060211.jpg", 
        title="Pomranc mnam piti", 
        price=10, 
        description="Pomeranc neni ovoce, change my mind"
    )

@app.route('/product/list')
def get_products():
    if (not request.headers['token']):
        return "No user id sent", 400

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
    if (not request.headers['token']):
        return "No user id sent", 400

    products = request.get_json()
    user = request.headers['token']

    try:
        productService.purchase_products(user, products)
    except Exception as e:
        print(e)

    return {}
