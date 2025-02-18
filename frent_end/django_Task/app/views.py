from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://killerkavi:tCzBHEOfhlZQXjUc@cluster0.mmtxa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client["college"]
student=db["student"]


detail={
  "name":"person5",
  "status":"pending"
}

# student.insert_one(detail)

# Create your views here.
def home(req):
 return render(req,"hello")



def getTask(req):
  print(req.body)
  # status=req.GET.get("status","pending")#if you want set default value of status 
  
  
  try:
    status=req.GET.get("status")
    if  status=="":
      return JsonResponse({"Error":"status is required"})
    
    collection_data=list(student.find({"status":status}))
    for i in collection_data:
      i["_id"]=str(i["_id"])
      print(i["_id"])
    return JsonResponse({"student":collection_data})
      
  except Exception as e:
    return JsonResponse({"Error":"failed to fetch"})






def datas(req):
  content={
    "name":"kavi"
  }
  return render(req,"index.html",content)