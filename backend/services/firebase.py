import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Leer la clave desde variable de entorno
firebase_key_json = os.getenv("FIREBASE_KEY")

if not firebase_key_json:
    raise Exception("FIREBASE_KEY environment variable not found")

# Convertir string JSON a dict
firebase_key_dict = json.loads(firebase_key_json)

# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_key_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# -----------------------------
# FUNCIONES QUE USAN TUS ROUTERS
# -----------------------------

def save_lead(data: dict):
    doc_ref = db.collection("leads").document()
    doc_ref.set(data)
    return True

def get_leads():
    docs = db.collection("leads").stream()
    leads = []
    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        leads.append(item)
    return leads

def update_lead(lead_id: str, data: dict):
    db.collection("leads").document(lead_id).update(data)
    return True
