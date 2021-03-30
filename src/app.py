from flask import Flask
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    return '<h1>Hello!</h1>'

todos_data = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

def todos():
    todos_data = { "name": "Bobby", "lastname": "Rixer" }
    json_text = flask.jsonify(todos_data)
    return json_text


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)