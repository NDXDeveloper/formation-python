# ============================================================================
#   Section 11.3 : Flask - Micro-framework leger
#   Description : Application Flask complete - routes, parametres,
#                 methodes HTTP, sessions, messages flash, gestion erreurs
#   Fichier source : 03-flask-micro-framework.md
# ============================================================================

"""Application Flask avec routes, sessions et gestion d'erreurs."""

from flask import Flask, jsonify, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'cle-secrete-pour-les-sessions'


# --- Routes simples ---

@app.route('/')
def home():
    return "Page d'accueil"


@app.route('/about')
def about():
    return "A propos de nous"


@app.route('/contact')
def contact():
    return "Contactez-nous"


# --- Routes avec parametres ---

@app.route('/user/<username>')
def show_user(username):
    return f"Profil de l'utilisateur : {username}"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Vous lisez l'article numero {post_id}"


@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return f"Article {post_id} de {username}"


# --- url_for ---

@app.route('/liens')
def liens():
    profile_url = url_for('show_user', username='alice')
    post_url = url_for('show_post', post_id=42)
    return f"Profil: {profile_url}, Article: {post_url}"


# --- Methodes HTTP et formulaires ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        session['username'] = username
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    return "Formulaire de connexion"


@app.route('/dashboard')
def dashboard():
    if session.get('logged_in'):
        return f"Tableau de bord de {session['username']}"
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('home'))


# --- Objet request ---

@app.route('/test-request')
def test_request():
    search = request.args.get('search', 'aucun')
    method = request.method
    user_agent = request.headers.get('User-Agent', 'inconnu')[:30]
    return jsonify({
        "search": search,
        "method": method,
        "user_agent": user_agent
    })


# --- Gestion des erreurs ---

@app.errorhandler(404)
def page_not_found(e):
    if request.path.startswith('/api/'):
        return jsonify({"error": "Ressource non trouvee"}), 404
    return "Page non trouvee (404)", 404


@app.errorhandler(500)
def internal_error(e):
    return "Erreur interne (500)", 500


# --- Tests avec test_client ---
if __name__ == "__main__":
    with app.test_client() as client:
        print("=== Routes simples ===")
        r = client.get('/')
        print(f"  GET / : {r.status_code} - {r.data.decode()}")
        r = client.get('/about')
        print(f"  GET /about : {r.status_code} - {r.data.decode()}")
        r = client.get('/contact')
        print(f"  GET /contact : {r.status_code} - {r.data.decode()}")

        print("\n=== Routes avec parametres ===")
        r = client.get('/user/alice')
        print(f"  GET /user/alice : {r.data.decode()}")
        r = client.get('/post/42')
        print(f"  GET /post/42 : {r.data.decode()}")
        r = client.get('/user/bob/post/7')
        print(f"  GET /user/bob/post/7 : {r.data.decode()}")

        print("\n=== url_for ===")
        r = client.get('/liens')
        print(f"  GET /liens : {r.data.decode()}")

        print("\n=== Sessions (login/dashboard/logout) ===")
        r = client.get('/login')
        print(f"  GET /login : {r.data.decode()}")
        r = client.post('/login', data={'username': 'alice'}, follow_redirects=True)
        print(f"  POST /login (alice) -> dashboard : {r.data.decode()}")
        r = client.get('/dashboard')
        print(f"  GET /dashboard : {r.data.decode()}")
        r = client.get('/logout', follow_redirects=True)
        print(f"  GET /logout -> home : {r.data.decode()}")
        r = client.get('/dashboard', follow_redirects=True)
        print(f"  GET /dashboard (deconnecte) -> login : {r.data.decode()}")

        print("\n=== Objet request ===")
        r = client.get('/test-request?search=python')
        print(f"  GET /test-request?search=python : {r.json}")

        print("\n=== Gestion des erreurs ===")
        r = client.get('/page-inexistante')
        print(f"  GET /page-inexistante : {r.status_code} - {r.data.decode()}")
        r = client.get('/api/ressource-inexistante')
        print(f"  GET /api/... (404 JSON) : {r.status_code} - {r.json}")
