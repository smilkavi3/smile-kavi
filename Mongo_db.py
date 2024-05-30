
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://kaviyarasan:ZD5ArG6LQ7ugGgNb@cluster0.heojidf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    


# frist create database:

db=client["college"]
student=db

student=[
    {
    "name":"kaviyarasan",
    "course":"puthon full stack ",
    "adress":{
        "no:":"6, 3-cross prasanthi nagar",
        "area": "dharamapuri",
        "country":"india",
    }
},
{
    "name":"kavi",
    "course":"puthon full stack ",
    "adress":{
        "no:":"6, 3-cross prasanthi nagar",
        "area": "muthirayarpalayam",
        "country":"india",
    }
}]
print(student[1]["name"])