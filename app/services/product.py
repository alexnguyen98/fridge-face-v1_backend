from flask import jsonify
import requests

# host = "https://corp.applifting.cz/api"
host = "https://staging.corp.applifting.cz/api"

class ProductService:
    def get_all_products(self, user):
        res = requests.get(host + "/v2/products", headers={'Authorization': user})
        if res.ok:
            return res.content, {'Content-type':'application/json'}

    def purchase_products(self, user, products):
        requests.post(host + "/v1/purchases", json=products, headers={'Authorization': user})
