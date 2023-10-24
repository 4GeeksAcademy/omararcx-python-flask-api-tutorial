from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    
]
@app.route('/health-check', methods= ['GET'])
def health_check():
    return 'ok'


@app.route('/todos', methods= ['GET'])
def hello_world():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    new_todos = list(filter(lambda item: item.get('position') == position, todos))
    return jsonify(new_todos)
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3245, debug=True)