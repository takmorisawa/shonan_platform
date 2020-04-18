device_list = [
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

from rest_app.models import Series,Device

for series_name in series_id_map.keys():
    Series.objects.create(name=series_name)

for series_name, device_name in device_list:
    series=Series.objects.get(name=series_name)
    Device.objects.create(name=device_name,series=series)
