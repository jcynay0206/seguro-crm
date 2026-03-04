import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("backend/firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_lead(data):
    return db.collection("seguro_prospects").add(data)

def get_leads():
    docs = db.collection("seguro_prospects").stream()
    return [doc.to_dict() | {"id": doc.id} for doc in docs]

def update_lead(lead_id, data):
    return db.collection("seguro_prospects").document(lead_id).update(data)
