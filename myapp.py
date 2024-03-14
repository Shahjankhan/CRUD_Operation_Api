import requests
import json
URL='http://127.0.0.1:8000/student_Api/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id} 
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

# get_data(1)  

def post_data():
    name=input('Enter your name: ')
    city=input('Enter your city: ')
    roll=int(input('Enter your roll: '))
    data={
        'name':name,
        'city':city,
        'roll':roll
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

# post_data() 
      

def update_data():
    id=int(input('Enter the id:  '))
    name=input('Enter your name: ')
    city=input('Enter your city: ')
    roll=int(input('Enter your roll: '))
    data={
        'id':id,
        'name':name,
        'city':city,
        'roll':roll
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# update_data()  

def delete_data():
    id=int(input('Enter the id , you want to delete the object : '))
    data={'id':id} 
    json_data=json.dumps(data)
    r=requests.delete(url=URL, data= json_data)
    data=r.json()
    print(data)

delete_data()             
