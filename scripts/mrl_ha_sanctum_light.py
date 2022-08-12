import urllib2

data = '{"entity_id": "light.sanctum"}'
url = 'http://{your_ip}:8123/api/services/light/toggle'
req = urllib2.Request(url, data, {'Authorization': 'Bearer {your_token}
f = urllib2.urlopen(req)
print(f.read())
