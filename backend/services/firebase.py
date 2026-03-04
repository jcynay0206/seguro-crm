import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

firebase_key = os.getenv("FIREBASE_KEY")

if not firebase_admin._apps:
    cred = credentials.Certificate(json.loads(firebase_key))
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_lead(data):
    return db.collection("leads").add(data)

def get_leads():
    docs = db.collection("leads").stream()
    return [{**doc.to_dict(), "id": doc.id} for doc in docs]

def update_lead(lead_id, data):
    return db.collection("leads").document(lead_id).update(data)
