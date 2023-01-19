import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

cred = credentials.Certificate("storage/webshopatcsw-firebase-adminsdk-7hq91-69d17a22db.json")
firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

# # ------- Example 1 ------------
# # GET Data
#
# doc_ref_document = firestore_client.collection('data').document("UaRCPTkCJC7uXfsmxtmN")
# doc_ref_collection = firestore_client.collection('data')
#
# # document id:
# print(f"The document id is {doc_ref_document.id}")
#
# # snapshot of the document:
# doc = doc_ref_document.get()
# print(f"The document is {doc.to_dict()}")
#
# col = doc_ref_collection.get()
# print(f"The collection is {col}")
#
# # ------- Example 2 ------------
# # GET Data
#
# import google.cloud
#
# doc_ref = firestore_client.collection(u'data').limit(4)
#
# try:
#     docs = doc_ref.get()
#     for doc in docs:
#         print(u'Doc Data:{}'.format(doc.to_dict()))
# except google.cloud.exceptions.NotFound:
#     print(u'Missing data')
#
# # ------- Example 3 ------------
# # GET Data
#
# emp_ref = firestore_client.collection('data')
# docs = emp_ref.stream()
#
# for doc in docs:
#     print('{} => {} '.format(doc.id, doc.to_dict()))
#
# # ------- Example 4 ------------
# # ADD Data
#
# doc_ref = firestore_client.collection('data').document('emptwodoc')
# doc_ref.set({
#     'name':'John',
#     'lname':'Doe',
#     'email':'john@gmail.com',
#     'age':24
# })

# ------- Example 5 ------------
# ADD Data

import datetime

col_ref = firestore_client.collection('data') # col_ref is CollectionReference
results = col_ref.where('OrderId', '==', 'sE4LNMR5').get() # one way to query
#results = col_ref.order_by('ReleaseDate',direction='DESCENDING').limit(1).get() # another way - get the last document by date
for item in results:
    print(item.to_dict())
    print(item.id)

# Udpdate:
doc = col_ref.document(item.id) # doc is DocumentReference
field_updates = {"ProducedDate": datetime.datetime.now()}
doc.update(field_updates)



