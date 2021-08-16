from mongo_connection import client

collection = client.get_database("Enviromental_Health_BCN")["Air_stations"]

# this code transforms columns with latitude and longuitude data into a geoJson format.

for document in collection.find():
    collection.update_one(
        {"_id": document["_id"]},
        {
            "$set": {
                "location": {
                    "type": "Point",
                    "coordinates": [document["Latitude"], document["Longitude"]],
                }
            },
            "$unset": {"$Latitude": "", "$Longitude": ""},
        },
    )
