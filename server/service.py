from dbHelper import mysqlDb
from queries import queries
from datetime import datetime
################################################################################################
################################################################################################
def createTask(postParam):
    try:
        try:
            mysqlCon = mysqlDb.cursor(dictionary=True,buffered=False)
        except:
            return("ERROR IN DB CONNECTION")
        task = postParam.get('Task')
        taskStatus = postParam.get('Status')
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        mysqlCon.execute(queries['createTask'],(task,taskStatus,formatted_date))
        mysqlDb.commit()
        queryResult = getTodoListFromDB()
        return queryResult
    except Exception as e:
        raise ("INTERNAL SERVER ERROR (CT: " + str(e) + " )")
    finally:
        if(mysqlDb.is_connected()):
            # mysqlCon.close()
            print(mysqlDb.is_connected())
################################################################################################
################################################################################################
def markToDoComplete(postParam):
    try:
        try:
            mysqlCon = mysqlDb.cursor(dictionary=True,buffered=False)
        except:
            return("ERROR IN DB CONNECTION")
        taskId = postParam['todoObj']['taskId']
        mysqlCon.execute(queries['markToDoComplete'],(taskId,))
        mysqlDb.commit()

        queryResult = getTodoListFromDB()
        return queryResult
    except Exception as e:
        return("INTERNAL SERVER ERROR (GTLFD: " + str(e) + " )")
    finally:
        if(mysqlDb.is_connected()):
            mysqlCon.close()

        if(queryResult is not None):
            queryResult = None
################################################################################################
################################################################################################
def getTodoListFromDB():
    try:
        try:
            mysqlCon = mysqlDb.cursor(dictionary=True,buffered=False)
        except:
            return("ERROR IN DB CONNECTION")

        queryResult = mysqlCon.execute(queries['getTodoList'])
        queryResult = mysqlCon.fetchall()

        #Add Serial Numbers for tracking
        for (task,index) in zip(queryResult,range(0,len(queryResult))):
            task["SNo"] = index

        return queryResult
    except Exception as e:
        raise ("INTERNAL SERVER ERROR (GTLFD: " + str(e) + " )")
    finally:
        if(mysqlDb.is_connected()):
            mysqlCon.close()

        if(queryResult is not None):
            queryResult = None
################################################################################################
################################################################################################
def deleteTodo(postParam):
    try:
        try:
            mysqlCon = mysqlDb.cursor(dictionary=True,buffered=False)
        except:
            return("ERROR IN DB CONNECTION")
        taskId = postParam['todoObj']['taskId']
        mysqlCon.execute(queries['deleteTodo'],(taskId,))
        mysqlDb.commit()

        queryResult = getTodoListFromDB()
        return queryResult
    except Exception as e:
        return("INTERNAL SERVER ERROR (GTLFD: " + str(e) + " )")
    finally:
        if(mysqlDb.is_connected()):
            mysqlCon.close()

        if(queryResult is not None):
            queryResult = None
################################################################################################
################################################################################################