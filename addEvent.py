from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

eventdb = client['eventdb']

addEventCol = eventdb['addevent']

#to insert one the event 

# addEventCol.insert_one({
#     "eventname":"invertia",
#     "venue": "Bareilly",
#     "date": "21 Feb 2026",
# })

#to insert multiple events
# addEventCol.insert_many([{
#     "eventname":"invertia",
#     "venue": "Bareilly",
#     "date": "21 Feb 2026",
# },

# {
#     "eventname":"AI Powered Portfolio",
#     "venue": "Bareilly",
#     "date": "6 Feb 2026",
# }
# ])

#to delete the single event
# addEventCol.delete_one({"eventname":"AI Powered Portfolio"})

# to update the event
# addEventCol.update_one({"date":"21 Feb 2026"},
#                        {"$set":{"date":"23 Feb 2026"},{"event":"TedX"}})
