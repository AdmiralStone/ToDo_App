from dbHelper import mysqlDb
from queries import queries
from datetime import datetime

def createTask(postParam):
    try:
        try:
            mysqlCon = mysqlDb.cursor(mysqlDb.cursors.DictCursor)
        except:
            return("ERROR IN DB CONNECTION")
        task = postParam.get('Task')
        taskStatus = postParam.get('Status')
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        mysqlCon.execute(queries['createTask'],(task,taskStatus,formatted_date))
        mysqlDb.commit()
        return 'success'
    except Exception as e:
        return("INTERNAL SERVER ERROR (CT: " + str(e) + " )")
    finally:
        if(mysqlDb.is_connected()):
            mysqlCon.close()

def getTodoListFromDB():
    try:
        try:
            mysqlCon = mysqlDb.cursor(dictionary=True)
        except:
            return("ERROR IN DB CONNECTION")

        queryResult = mysqlCon.execute(queries['getTodoList'])
        queryResult = mysqlCon.fetchall()
        for x in queryResult:
            print(x)
        return queryResult
    except Exception as e:
        return("INTERNAL SERVER ERROR (GTLFD: " + str(e) + " )")
    finally:
        if(mysqlDb.is_connected()):
            mysqlCon.close()