from config import CORP_SERVER
import requests

class UserService:
    def get_info(self, user):
        res = requests.get(CORP_SERVER + "/v1/user/me", headers={'Authorization': user})
        if res.ok:
            res = res.json()
            return { 'name': res['first_name'] + " " + res['last_name'], 'nickname': res['nickname'] }

    def get_balance(self, user):
        res = requests.get(CORP_SERVER + "/v1/user/balance", headers={'Authorization': user})
        if res.ok:
            return res.content, {'Content-type':'application/json'}