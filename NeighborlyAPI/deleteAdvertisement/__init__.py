import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborlyappcosmosdb:dWQvJdA4Xq1d6jk1Pu6BGnKEoKaztZPy8mOQOKlh3NPVxvGIcxCq9NkH1PzXuBIb82FZzwBNH0DQ6Xq3wGiJ9Q==@neighborlyappcosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlyappcosmosdb@"
            client = pymongo.MongoClient(url)
            database = client['MongoDB']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
