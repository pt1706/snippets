import json
import requests
from datetime import date


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id=None):
        res = requests.get(f'{self.url}/web/user/get-status/{user_id}')
        json_data = json.loads(res.text)
        return json_data

    def get_user_last_action_time(self, user_id=None):
        json_data = self.__user_get_status(user_id)
        last_action_time = json_data['lastActionTime']
        time_diff = json_data['timeDiff']
        if last_action_time == 0:
            return date.fromtimestamp(time_diff)
        else:
            return date.fromtimestamp(last_action_time - time_diff)


src = SomeResourceClient('http://www.avito.ru')
print(src.get_user_last_action_time(177868588))
