# ============================================================================
#   Section 11.3 : Flask - Micro-framework leger
#   Description : API REST complete avec Flask - CRUD taches,
#                 jsonify, request.get_json, codes HTTP
#   Fichier source : 03-flask-micro-framework.md
# ============================================================================

"""API REST complete avec Flask - gestion de taches."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Donnees simulees
tasks = [
    {"id": 1, "title": "Apprendre Flask", "done": False},
    {"id": 2, "title": "Creer une API", "done": False}
]


# GET : Lire toutes les taches
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


# GET : Lire une tache specifique
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Tache non trouvee"}), 404


# POST : Creer une tache
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


# PUT : Mettre a jour une tache
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Tache non trouvee"}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['done'] = data.get('done', task['done'])
    return jsonify(task)


# DELETE : Supprimer une tache
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    original_len = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]
    if len(tasks) < original_len:
        return jsonify({"message": "Tache supprimee"}), 200
    return jsonify({"error": "Tache non trouvee"}), 404


# --- Gestion erreurs API ---
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Ressource non trouvee"}), 404


# --- Tests ---
if __name__ == "__main__":
    with app.test_client() as client:
        print("=== GET /api/tasks (liste initiale) ===")
        r = client.get('/api/tasks')
        print(f"  {r.status_code}: {r.json}")

        print("\n=== GET /api/tasks/1 ===")
        r = client.get('/api/tasks/1')
        print(f"  {r.status_code}: {r.json}")

        print("\n=== GET /api/tasks/999 (inexistant) ===")
        r = client.get('/api/tasks/999')
        print(f"  {r.status_code}: {r.json}")

        print("\n=== POST /api/tasks (creer) ===")
        r = client.post('/api/tasks', json={"title": "Tester l'API"})
        print(f"  {r.status_code}: {r.json}")

        print("\n=== GET /api/tasks (apres creation) ===")
        r = client.get('/api/tasks')
        print(f"  {r.status_code}: {len(r.json)} taches")
        for t in r.json:
            print(f"    id={t['id']}, title='{t['title']}', done={t['done']}")

        print("\n=== PUT /api/tasks/1 (marquer terminee) ===")
        r = client.put('/api/tasks/1', json={"done": True})
        print(f"  {r.status_code}: {r.json}")

        print("\n=== DELETE /api/tasks/2 ===")
        r = client.delete('/api/tasks/2')
        print(f"  {r.status_code}: {r.json}")

        print("\n=== GET /api/tasks (etat final) ===")
        r = client.get('/api/tasks')
        print(f"  {r.status_code}: {len(r.json)} taches restantes")
        for t in r.json:
            print(f"    id={t['id']}, title='{t['title']}', done={t['done']}")

        print("\n=== DELETE /api/tasks/999 (inexistant) ===")
        r = client.delete('/api/tasks/999')
        print(f"  {r.status_code}: {r.json}")
