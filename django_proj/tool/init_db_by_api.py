import requests
import json

list = [
    ("iPhone", "iPhone 11"),
    ("iPhone", "iPhone XS"),
    ("iPhone", "iPhone XR"),
    ("iPhone", "iPhone X"),
    ("iPhone", "iPhone 8"),
    ("iPhone", "iPhone 7"),
    ("Xperia", "Xperia 5"),
    ("Xperia", "Xperia 1"),
    ("Xperia", "Xperia XZ3"),
    ("Xperia", "Xperia XZ2"),
    ("Xperia", "Xperia XZ1"),
    ("Galaxy", "Galaxy S10"),
    ("Galaxy", "Galaxy S9"),
    ("Galaxy", "Galaxy Feel2"),
    ("Galaxy", "Galaxy A7"),
    ("Galaxy", "Galaxy A30"),
    ("HUAWEI", "HUAWEI P30 Pro"),
    ("HUAWEI", "HUAWEI P30"),
    ("HUAWEI", "HUAWEI P20"),
    ("HUAWEI", "HUAWEI nova lite3"),
    ("HUAWEI", "HUAWEI Mate 20 Pro"),
    ("AQUOS", "AQUOS R3"),
    ("AQUOS", "AQUOS R2"),
    ("AQUOS", "AQUOS sense3"),
    ("AQUOS", "AQUOS sense2"),
    ("AQUOS", "AQUOS zero2"),
    ("ZenFone", "ZenFone 6"),
    ("ZenFone", "ZenFone 5"),
    ("ZenFone", "ZenFone 5Z"),
    ("ZenFone", "ZenFone Max Pro (M2)"),
    ("ZenFone", "ZenFone Zoom")
]

series_id_map = {
    "iPhone": 1,
    "Xperia": 2,
    "Galaxy": 3,
    "HUAWEI": 4,
    "AQUOS": 5,
    "ZenFone": 6
}

url = "http://localhost:8000/api/devices/"
headers = { "Content-Type": "application/json" }

for series, device in list:
    obj = { "name": device, "series": series_id_map[series] }
    json_str = json.dumps(obj).encode("utf-8")
    response = requests.post(url, json_str, headers=headers)
    print(response)
    print(json_str)
