
import time
import json
from hashlib import sha1
import requests


def get_access_token(app_id, app_key):
    """
    Get the access token for the given app ID and app key.

    Args:
        app_id (str): The ID of the application.
        app_key (str): The key of the application.

    Returns:
        str: The access token.

    """

    host = "YOUR_HOST"

    secret_key = "YOUR_SECRET_KEY"

    # 当前时间戳
    t = int(time.time())

    # 拼接签名串: t为客户端的时间戳，aid为app_id，akey为api_key，skey为secret_key
    need_sign_str = f"t={t}&aid={app_id}&akey={app_key}&skey={secret_key}"

    sign = sha1(need_sign_str.encode("utf8")).hexdigest()

    header = {'Content-Type': 'application/json; charset=UTF-8'}

    request_data = {"aid": app_id,
                    "akey": app_key,
                    "sign": sign,
                    "t": t}

    r = requests.post(host, headers=header, data=json.dumps(request_data))
    token_data = json.loads(r.text)
    access_token = ""
    if token_data.get("status") == 0:
        access_token = token_data["data"].get("access_token")

    return access_token
