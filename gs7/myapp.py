import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
#to get data(read)
def get_data(id=None):
    data = {}
    if id is not None:
      data = {'id': id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data=json_data)
    data = req.json()
    print(data)

# get_data() -we have to call the function to execute it.

#to post data(create)
def post_data():
   data = {
      'name': 'Rinisha',
      'roll': 133,
      'city': 'Bhaktapur'
   }
   json_data = json.dumps(data)
   res = requests.post(url=URL, data= json_data)
   newdata = res.json()
   print(newdata)

post_data()

#to update data(Put, Patch)
def update_data():
    data = {
      'id': 4,
      'name': 'Rojan Prajapati',
      'city': 'Bhaktapur, Chyamasingh',
   }
    json_data = json.dumps(data)
    res = requests.put(url= URL, data= json_data)
    newdata = res.json()
    print(newdata)

# update_data()

#to delete data(delete)
def delete_data():
    data = { 'id': 10 }
    json_data = json.dumps(data)
    res = requests.delete(url= URL, data= json_data)
    newdata = res.json()
    print(newdata)

# delete_data()