import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
import tempfile
from datetime import datetime

# Leer la clave desde variable de entorno
firebase_key_json = os.getenv("FIREBASE_KEY")

if not firebase_key_json:
    raise Exception("FIREBASE_KEY environment variable not found")

# Convertir string JSON a dict
firebase_key_dict = json.loads(firebase_key_json)

# Crear archivo temporal con la clave
with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
    temp_file.write(json.dumps(firebase_key_dict).encode("utf-8"))
    temp_path = temp_file.name

# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate(temp_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# -----------------------------
# FUNCIONES QUE USAN TUS ROUTERS
# -----------------------------

def save_lead(data: dict):
    try:
        clean_data = {
            "name": (data.get("name") or "").strip(),
            "email": (data.get("email") or "").lower().strip(),
            "phone": (data.get("phone") or "").strip(),
            "meta": (data.get("meta") or "").strip(),
            "status": (data.get("status") or "nuevo").strip(),
            "source": (data.get("source") or "manual").strip(),
            "created_at": datetime.utcnow().isoformat()
        }

        # Validación mínima obligatoria
        if not clean_data["name"]:
            raise ValueError("Missing name")
        if not clean_data["email"]:
            raise ValueError("Missing email")
        if not clean_data["phone"]:
            raise ValueError("Missing phone")

        doc_ref = db.collection("leads").document()
        doc_ref.set(clean_data)

        return True

    except Exception as e:
        print("🔥 ERROR FIREBASE:", e)
        raise e

        # Validación mínima obligatoria
        if not clean_data["name"]:
            raise ValueError("Missing name")
        if not clean_data["email"]:
            raise ValueError("Missing email")
        if not clean_data["phone"]:
            raise ValueError("Missing phone")

        doc_ref = db.collection("leads").document()
        doc_ref.set(clean_data)

        return True

    except Exception as e:
        print("🔥 ERROR FIREBASE:", e)
        raise e


def get_leads():
    docs = db.collection("leads").stream()
    leads = []
    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        leads.append(item)
    return leads


def update_lead(lead_id: str, data: dict):
    try:
        clean_data = {k: v for k, v in data.items() if v is not None}
        db.collection("leads").document(lead_id).update(clean_data)
        return True
    except Exception as e:
        print("🔥 ERROR UPDATE FIREBASE:", e)
        raise e
