from app import app, api, mongo
from pymongo.collection import ReturnDocument
from flask_restful import reqparse, Resource
from concurrent.futures import ThreadPoolExecutor
from app.routes import to_day, get_last_collectionId



# Different collections in the Database
collectiondb = mongo.db.CollectionsDB
samplesdb = mongo.db.SamplesDB
#######################################################################
##################  DIFFERENT ENDPOINTS   ##############################

class CollectionsCRUD(Resource):
    # define schema
    parser = reqparse.RequestParser()
    parser.add_argument('disease_term', type=str, required=True, help="Enter Disease Term. Field cannot be left blank")
    parser.add_argument('title', type=str, required=True, help="Enter Title of the collection. Field cannot be left blank")
    
    def post(self):
        data = CollectionsCRUD.parser.parse_args()
        disease_term=data["disease_term"]
        title=data["title"]
        collection_id = str(get_last_collectionId()+1 )  # last collection id + 1

        # Insert into collectionDB in Database
        executor = ThreadPoolExecutor(max_workers=1)
        executor.submit(collectiondb.insert_one({collection_id:True ,"collection_id": collection_id, 'disease_term': disease_term,'title':title, "create_date": to_day()}))

        # return response to user
        message = f"Collection created successfully with Collection Id = {collection_id}"
        return {"status": True, "message": message,"data":None}, 200
    
    #API to retrieve all Sample collections in Database
    def get(self):
        result = collectiondb.find({},{"_id":0})
        alldata = [item for item in result]
        if alldata == []:
            return {"status": False, "message": "No tissue sample collection data yet.","data":None}, 400
        return {"status": True, "message": "Tissue sample Collections data retrieved.","count":len(alldata), "data":alldata}, 200
api.add_resource(CollectionsCRUD, '/api/v1/collection')


class ValidateCollectionId(Resource):
    def get(self, collection_id):
        # retrieve record associated with the collection Id
        collection_detail = collectiondb.find_one({collection_id:{"$exists": True}})
        if not collection_detail:
            return {"status": False, "message": "Invalid collection Id.","data":None}, 400
        disease_term = collection_detail["disease_term"]
        title = collection_detail["title"]
        # return response to user
        message = f"Collection Id = {collection_id} validated successfully."
        return {"status": True, "message": message,"data":{"collection_id":collection_id,"disease_term":disease_term, "title":title}}, 200
api.add_resource(ValidateCollectionId, '/api/v1/collection/<string:collection_id>')


class SamplesCRUD(Resource):
    # define schema
    parser = reqparse.RequestParser()
    parser.add_argument('donor_count', type=str, required=True, help="Enter Donor Count. Field cannot be left blank")
    parser.add_argument('material_type', type=str, required=True, help="Enter Material Type for the sample. Field cannot be left blank")
    
    def post(self, collection_id):
        data = SamplesCRUD.parser.parse_args()
        # retrieve record associated with the collection Id
        collection_detail = collectiondb.find_one({collection_id:{"$exists": True}})
        if not collection_detail:
            return {"status": False, "message": "Invalid collection Id.","data":None}, 400

        donor_count=data["donor_count"]
        material_type=data["material_type"]
        title = collection_detail["title"]
        # Insert into samplesDB in Database
        executor = ThreadPoolExecutor(max_workers=1)
        executor.submit(samplesdb.insert_one({collection_id: True,"collection_id": collection_id, 'title': title,'donor_count':donor_count, "material_type":material_type, "create_date": to_day(), "last_updated": to_day()}))

        # return response to user
        message = f"Sample details added successfully to Collection Id = {collection_id}"
        return {"status": True, "message": message,"data":None}, 200
    
    #API to retrieve all Sample collections in Database
    def get(self, collection_id):
        result = samplesdb.find({collection_id:{"$exists": True}},{"_id":0}).sort("last_updated", -1)
        alldata = [item for item in result]
        if alldata == []:
            return {"status": False, "message": "No tissue sample for this collection yet.","data":None}, 400
        return {"status": True, "message": "Tissue sample for the collection retrieved.","count":len(alldata), "data":alldata}, 200
api.add_resource(SamplesCRUD, '/api/v1/sample/<string:collection_id>')


class AllSamples(Resource):
    #API to retrieve all Sample collections in Database
    def get(self):
        result = samplesdb.find({},{"_id":0}).sort("create_date", -1)
        alldata = [item for item in result]
        if alldata == []:
            return {"status": False, "message": "No tissue sample data yet.","data":None}, 400
        return {"status": True, "message": "All tissue samples retrieved.","count":len(alldata), "data":alldata}, 200
api.add_resource(AllSamples, '/api/v1/sample/all')