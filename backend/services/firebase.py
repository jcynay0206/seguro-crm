import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# -----------------------------
# FUNCIONES QUE USAN TUS ROUTERS
# -----------------------------

def save_lead(data: dict):
    """Guarda un lead en Firestore."""
    doc_ref = db.collection("leads").document()
    doc_ref.set(data)
    return True


def get_leads():
    """Obtiene todos los leads."""
    docs = db.collection("leads").stream()
    leads = []
    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        leads.append(item)
    return leads


def update_lead(lead_id: str, data: dict):
    """Actualiza un lead existente."""
    db.collection("leads").document(lead_id).update(data)
    return True
