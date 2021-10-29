import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighborlyappcosmosdb:dWQvJdA4Xq1d6jk1Pu6BGnKEoKaztZPy8mOQOKlh3NPVxvGIcxCq9NkH1PzXuBIb82FZzwBNH0DQ6Xq3wGiJ9Q==@neighborlyappcosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlyappcosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['MongoDB']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

