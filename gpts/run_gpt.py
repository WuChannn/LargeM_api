import requests
import simplejson


def run(input_str, app_id, app_key, access_token):

    url = "YOUR_URL"
    data = {
        "type": "microsoft",
        "model": "gpt-4",
        "max_tokens": 1024,
        "temperature": 1,
        "top_p": 1,
        "input": input_str
    }

    headers = {'Content-type': 'application/json','X-C-AppId':app_id,"X-C-ApiKey":app_key,"Token":access_token}
    params = {'session_id': '88888','user_id':"66666"}
    response = requests.post(url, json=data, headers=headers, params=params)

    return simplejson.loads(response.text)
