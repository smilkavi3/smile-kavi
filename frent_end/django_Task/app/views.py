from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from bson import ObjectId
from django.views.decorators.csrf import csrf_exempt
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




#Activate Edit btn  find get specific data from mongo db:
@csrf_exempt
def getSpecificData(req):
  print(req.body,"request body") #what is contain the body:

  if req.method=="POST":

    try:
      data=json.loads(req.body)
      id=data.get("id")
      # newName=data.get("name")
      # newStatus=data.get("status")
      get_id=ObjectId(id) 
      if not data.get("id"):
        return JsonResponse({"Error":"Not data here inner if block throw"})
      
      newid=student.find_one({"_id":get_id})
      # newid=student.find_one({"_id":ObjectId(id)})
      newid["_id"] = str(newid["_id"])  # Convert ObjectId to string
      return JsonResponse({"datas": newid})
      

    except Exception as e:
      return JsonResponse({"Error":"Throw Error in Try block"})
  
  return JsonResponse({"Error":"The Request Method is not post Outer block if throw error"})


# complet find data in edit btn

# update data to mongo db modifiy data:
@csrf_exempt
def getUpdateData(req):
  print(req.body ,"reques from getupdate data   ")

  if req.method=="PUT":
    try:
      data=json.loads(req.body)
      print(data)
      print(data.get("name"),"id from update data")
    except Exception as e:
      return JsonResponse({"Error":"somthing problem in try"})
  
  return JsonResponse({"Error":"The Request method is not PUT"})







def datas(req):
  content={
    "name":"kavi"
  }
  return render(req,"index.html",content)