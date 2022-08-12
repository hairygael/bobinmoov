import urllib2

# original worky for 1 light
# data = '{"entity_id": "light.sanctum"}'
# url = 'http://{your_ip}:8123/api/services/light/toggle'
# req = urllib2.Request(url, data, {'Authorization': 'Bearer {your_token}'})
# f = urllib2.urlopen(req)
# print(f.read())


#define url and Bearer token
token = 'Bearer "your_token"'
turn_on = 'http://{your_ip}:8123/api/services/light/turn_on'
turn_on = 'http://{your_ip}:8123/api/services/light/turn_off'
toggle = 'http://{your_ip}:8123/api/services/light/toggle'


# define the lights
sanctum = light.sanctum
ceilingfanlights = light.ceiling_fan_lights
deskled = light.desk_led
bathroom = light.bathroom_lights
master = light.master_lights

# create a list of lights
lightList = {"sanctum", "ceilingfanlights", "deskled", "bathroom", "master"}

def turnOn(lights):
    try :
        # message if no light found
        if (lightList.get(lights) == None):
            print("No light with this name found")
            talkBlocking("Sorry, I didn't understand which light you wanted me to turn on")
        else:
            print("ok found the requested light")
            talkBlocking("Sure, light on")
            if (lightList.get(lights) == "sanctum"):
                turn_on(sanctum)
            if (lightList.get(lights) == "ceilingfanlights"):
                turn_on(ceilingfanlights)
            if (lightList.get(lights) == "deskled"):
                turn_on(ceilingfanlights)
            if (lightList.get(lights) == "bathroom"):
                turn_on(bathroom)
            if (lightList.get(lights) == "master"):
                turn_on(master)
    except:
        print("Something went wrong with ON")


def turnOff(lights):
    try :
        # message if no light found
        if (lightList.get(lights) == None):
            print("No light with this name found")
            talkBlocking("Sorry, I didn't understand which light you wanted me to turn off")
        else:
            print("ok found the requested light")
            talkBlocking("Ok,light off")
            if (lightList.get(lights) == "sanctum"):
                turn_off(sanctum)
            if (lightList.get(lights) == "ceilingfanlights"):
                turn_off(ceilingfanlights)
            if (lightList.get(lights) == "deskled"):
                turn_off(ceilingfanlights)
            if (lightList.get(lights) == "bathroom"):
                turn_off(bathroom)
            if (lightList.get(lights) == "master"):
                turn_off(master)
    except:
        print("Something went wrong with OFF")
