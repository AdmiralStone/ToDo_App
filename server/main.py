from flask import Flask, jsonify, request
from flask_cors import CORS
import model

#configuration
DEBUG = True

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#enable CORS
CORS(app,resources={r'/*':{'origins':'*'}})

todoList = model.Todos

#test Route
@app.route('/ping',methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/getTodo',methods=['GET'])
def getTodo():
    return jsonify(todoList)

@app.route('/markTodoComplete', methods=['POST'])
def markTodoComplete():
    postPara_data = request.get_json()
    for task in todoList:
        if task['No'] == postPara_data.get('No'):
            task['Status'] = 1
    return jsonify(todoList)

if __name__ == '__main__':
    app.run()