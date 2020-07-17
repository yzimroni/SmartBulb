import json
import lakeside

secrets = {}
with open("secrets.json") as f:
    secrets = json.load(f)

# TODO add device details cache
devices = lakeside.get_devices(secrets["username"], secrets["password"])
d = devices[0]
print("Bulb info: %s" % str(d))
bulb = lakeside.bulb(d["address"], d["code"], d["type"])
bulb.connect()

if bulb.get_status().bulbinfo.packet.bulbstate.power == 0:
    print("Toggling bulb on")
    bulb.set_power(power=1)
else:
    print("Toggling bulb off")
    bulb.set_power(power=0)
