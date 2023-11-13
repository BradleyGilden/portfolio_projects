#!/usr/bin/python3

"""
creates functions for crud operations

Author: Bradley Dillion Gilden
Date: 09-11-2023
"""
from modules.user import User
from pymongo.errors import BulkWriteError, WriteError  # noqa
from bson import ObjectId  # noqa

"""################################ CREATE ###############################"""


def doc_signup(collection, document: dict) -> str:
    """inserts document inside collection"""
    try:
        user = User(document["token"], document["login"])
        if user.test_credentials != 200:
            return "invalid_credentials"
        doc = collection.find_one({"username": document["username"]})
        if doc is None:
            doc_id = collection.insert_one(document).inserted_id
            return str(doc_id)
        else:
            return "occupied"
    except WriteError:
        return "WriteError"


# def insert_docs(collection, document_list: List[dict]):
#     """inseets multiple documents inside a collection"""
#     try:
#         collection.insert_many(document_list)
#         print("Succes!")
#     except BulkWriteError as e:
#         print(e)


# """################################ READ ###############################"""


# def find_all(collection, filters={}, columns={}):
#     """lists documents in a collection"""
#     for doc in collection.find(filters, columns):
#         printer.pprint(doc)


# def find_by_name(collection, name: str):
#     """Finds doc by name field, not accurate as it returns the first doc it
#     finds if there are duplicates"""

#     doc = collection.find_one({"name": name})
#     if doc is None:
#         print("Not found")
#     else:
#         printer.pprint(doc)


# def find_by_id(collection, id: str):
#     """Finds doc by id field"""

#     doc = collection.find_one({"_id": ObjectId(id)})
#     if doc is None:
#         print("Not found")
#     else:
#         printer.pprint(doc)


# def count(collection, filters={}):
#     """counts number of documents present depending on the filter"""
#     print(collection.count_documents(filters))


# def age_range(collection, min: int, max: int):
#     """returns docs within an age range"""
#     query = {
#         "$and": [{"age": {"$gte": min}}, {"age": {"$lte": max}}]
#     }

#     for doc in collection.find(query).sort("age"):
#         printer.pprint(doc)


# """################################ UPDATE ###############################"""


# def update_by_id(collection, id, set_dict: dict):
#     """update fields"""
#     collection.update_one({"_id": ObjectId(id)}, {"$set": set_dict})


# def rename_by_id(collection, id, rename_dict: dict):
#     """renames fields fields"""
#     collection.update_one({"_id": ObjectId(id)}, {"$rename": rename_dict})


# def replace_by_id(collection, id, doc):
#     """replaces doc at a specifc id"""
#     collection.replace_one({"_id": ObjectId(id)}, doc)


# """################################ Delete ###############################"""


# def delete_by_id(collection, id):
#     """deletes obj using it's id value"""
#     collection.delete_one({"_id": ObjectId(id)})
