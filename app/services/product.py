from config import CORP_SERVER
import requests

class ProductService:
    def get_all_products(self, user):
        res = requests.get(CORP_SERVER + "/v2/products", headers={'Authorization': user})
        if res.ok:
            return res.content, {'Content-type':'application/json'}

    def purchase_products(self, user, products):
        requests.post(CORP_SERVER + "/v1/purchases", json=products, headers={'Authorization': user})
