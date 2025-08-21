from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB (later will to change Atlas)
db = client["acidtrace"] 
transactions_collection = db["transactions"]


def save_source(source_code, amount):
    transactions_collection.insert_one({
        "type": "source",
        "source_code": source_code,
        "amount": amount
    })


def save_transaction(vendor_code, source_code, amount, leaf=False):
    transactions_collection.insert_one({
        "type": "transaction",
        "vendor_code": vendor_code,
        "source_code": source_code,
        "amount": amount,
        "leaf": leaf
    })


def get_all_transactions():
    return list(transactions_collection.find({}, {"_id": 0}))
