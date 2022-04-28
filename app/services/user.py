import requests

host = "https://corp.applifting.cz/api"

class UserService:
    def get_info(self, user):
        res = requests.get(host + "/v1/user/me", headers={'Authorization': user})
        if res.ok:
            res = res.json()
            return { 'name': res['full_name'], 'nickname': res['nickname'] }