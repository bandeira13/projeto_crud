from flask import Flask, request, jsonify , render_template
from database import get_connection
import database

app = Flask(__name__)
database.init_db()

@app.route('/')
def index():
     
     return render_template("index.html")


@app.post("/tarefas")
def criar_tarefa():
    data = request.json
    conn = get_connection()
    conn.execute("INSERT INTO tarefas (titulo) VALUES (?)", (data["titulo"],))
    conn.commit()
    return jsonify({"message": "Tarefa criada"}), 201

@app.get("/tarefas")
def listar_tarefas():
    conn = get_connection()
    tarefas = conn.execute("SELECT * FROM tarefas").fetchall()
    return jsonify([dict(t) for t in tarefas])

@app.put("/tarefas/<int:id>")
def atualizar_tarefa(id):
    conn = get_connection()
    conn.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id,))
    conn.commit()
    return jsonify({"message": "Tarefa concluída"})

@app.delete("/tarefas/<int:id>")
def apagar_tarefa(id):
    conn = get_connection()
    conn.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    return jsonify({"message": "Tarefa removida"})

if __name__ == '__main__':
    app.run(debug=True)