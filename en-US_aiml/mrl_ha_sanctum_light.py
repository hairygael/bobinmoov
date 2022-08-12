import urllib2

data = '{"entity_id": "light.sanctum"}'
url = 'http://192.168.30.177:8123/api/services/light/toggle'
req = urllib2.Request(url, data, {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4ZTRiNjVmZmQ4ZTQ0ZTVhYjAwMzVjZTBlYzMyNTczZiIsImlhdCI6MTY2MDE5NDQyNiwiZXhwIjoxOTc1NTU0NDI2fQ.yGCl59nDJyVkVQXc44cRdkPVjSYVv97n_3t9wTeLDLI'})
f = urllib2.urlopen(req)
print(f.read())