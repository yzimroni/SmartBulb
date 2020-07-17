import json
import lakeside

secrets = {}
with open("secrets.json") as f:
    secrets = json.load(f)

devices = lakeside.get_devices(secrets["username"], secrets["password"])
d = devices[0]
bulb = lakeside.bulb(d["address"], d["code"], d["type"])
bulb.connect()

print(bulb.get_status())
