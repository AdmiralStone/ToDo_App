from dbHelper import mysqlDb
from queries import queries
from datetime import datetime

def createTask(postParam):
    try:
        task = postParam.get('Task')
        taskStatus = postParam.get('Status')
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        mysqlCon = mysqlDb.cursor()
        mysqlCon.execute(queries['createTask'],(task,taskStatus,formatted_date))
        mysqlDb.commit()
        return 'success'
    except Exception as e:
        return("INTERNAL SERVER ERROR (CT: " + str(e) + " )")
    finally:
        if(mysqlDb.is_connected()):
            mysqlCon.close()
    
