from asyncio import events
from pymongo import MongoClient 

# create the cluster/client connection
client = MongoClient('link')

# create the database using the client cluster
eventdb = client['eventdb']

# create the collection addevent using the database
addEventCol = eventdb['addevent']

#to insert one the event 

# addEventCol.insert_one({
#     "eventname":"invertia",
#     "venue": "Bareilly",
#     "date": "21 Feb 2026",
# })



# to insert multiple events
addEventCol.insert_many([{
    "eventname":"invertia",
    "venue": "Bareilly",
    "date": "21 Feb 2026",
},

{
    "eventname":"AI Powered Portfolio",
    "venue": "Bareilly",
    "date": "6 Feb 2026",
}
])
