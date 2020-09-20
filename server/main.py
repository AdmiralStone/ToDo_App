from flask import Flask, jsonify, request
from flask_cors import CORS
import model
import service 


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
    resultObj = {}
    resultObj["data"] = service.getTodoListFromDB()
    resultObj["status"] = "success"
    return jsonify(resultObj)

@app.route('/markTodoComplete', methods=['POST'])
def markTodoComplete():
    try:
        resultObj = {}
        postParams = request.get_json()
        resultObj["data"] = service.markToDoComplete(postParams)
        resultObj["status"] = "success"
        resultObj["message"]= "Task Marked As Complete"
        return jsonify(resultObj)
    except Exception as e:
        resultObj["status"] = "error"
        resultObj["message"] = str(e)
        return jsonify({resultObj})

@app.route('/addTask', methods=['POST'])
def createTask():
    try:
        resultObj = {}
        postParams = request.get_json()
        resultObj["data"] = service.createTask(postParams)
        resultObj["status"] = "success"
        resultObj["message"]= "Task Marked As Complete"
        return jsonify(resultObj)
    except Exception as e:
        resultObj["status"] = "error"
        resultObj["message"] = str(e)
        return jsonify({resultObj})

@app.route('/deleteTodo', methods=["POST"])
def deleteTodo():
    try:
        resultObj ={}
        postParams = request.get_json()
        resultObj["data"] = service.deleteTodo(postParams)
        resultObj["status"] = "success"
        resultObj["message"]= "Task Marked As Complete"
        return jsonify(resultObj)
    except Exception as e:
        resultObj["status"] = "error"
        resultObj["message"] = str(e)
        return jsonify({resultObj})
    
if __name__ == '__main__':
    app.run()