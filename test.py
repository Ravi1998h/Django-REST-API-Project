import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id=None):
    data={} #we need all records
    if id is not None:
        data={'id':id} #we need a particular record
    response=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())
def create_resource():
    new_emp={'eno':1001,'ename':'Ravi','esal':'80000','eaddr':'Bengalore'}
    response=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(response.status_code)
    print(response.json())

def update_resource(id):
    new_data={'id':id,'eno':1001,'ename':'amit','esal':'50000','eaddr':'Naragund'}
    response=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(response.status_code)
    print(response.json())

def delete_resource(id):
    data={'id':id}
    response=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())

print("Enter 1-->get record 2---> Create a record 3-->update a record 4--->Delate a record")
print("Enter your choice")
ch=int(input())
if ch==1:
    get_resource(7)
elif ch==2:
    create_resource()
elif ch==3:
    id=int(input("Enter Record id:"))
    update_resource(id)
elif ch==4:
    id=input("Enter Record id:")
    delete_resource(id)
