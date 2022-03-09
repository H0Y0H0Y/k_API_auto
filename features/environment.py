import json
import requests

def after_all(context):
    url = "http://216.10.245.166/Library/DeleteBook.php"
    data = json.dumps({"ID": "bcd23482274"})
    r = requests.post(url=url, data=data)
