from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

@app.route('/')
def home():
    return jsonify({"message": "Todo SaaS API"})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "Task required"}), 400
    todo = {"id": len(todos) + 1, "task": data['task'], "done": False}
    todos.append(todo)
    return jsonify(todo), 201

if __name__ == '__main__':
    app.run(debug=True)