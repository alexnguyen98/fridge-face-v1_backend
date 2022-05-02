from config import CORP_SERVER
import requests

class UserService:
    def get_info(self, user):
        res = requests.get(CORP_SERVER + "/v1/user/me", headers={'Authorization': user})
        if res.ok:
            res = res.json()
            return { 'name': res['full_name'], 'nickname': res['nickname'] }