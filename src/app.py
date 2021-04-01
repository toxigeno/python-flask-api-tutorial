from flask import Flask, jsonify, request, json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data #lo que se mete por fuera
    decoded_object = json.loads(request_body) #convertimos a objeto
    print("Incoming request with the following body", request_body)
    todos.append(decoded_object) #agrega, similar al push
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)