from flask import Flask, request
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola desde Flask desplegado con Terraform y Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

def test_db_connection():
    try:
        with psycopg2.connect(
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS"),
            host=os.environ.get("DB_HOST"),
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                result = cur.fetchone()
                return f"Connected to DB, test result: {result[0]}"
    except Exception as e:
        return f"DB connection failed: {e}"

@app.route("/")
def index():
    return test_db_connection()


def init_db():
    with psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        host=os.environ.get("DB_HOST"),
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                );
            """)
            conn.commit()

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/db-status")
def db_status():
    try:
        with psycopg2.connect(
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS"),
            host=os.environ.get("DB_HOST"),
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
        return {"db": "connected"}, 200
    except Exception as e:
        return {"db": "error", "message": str(e)}, 500

@app.route("/users")
def list_users():
    try:
        with psycopg2.connect(
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS"),
            host=os.environ.get("DB_HOST"),
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, email FROM users;")
                users = cur.fetchall()
        return {"users": [{"id": u[0], "name": u[1], "email": u[2]} for u in users]}, 200
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return {"error": "Name and email are required"}, 400

    try:
        with psycopg2.connect(
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS"),
            host=os.environ.get("DB_HOST"),
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
                conn.commit()
        return {"message": "User created"}, 201
    except Exception as e:
        return {"error": str(e)}, 500

