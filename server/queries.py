queries ={
    "createTask": "INSERT INTO taskList(vsTask, bStatus, dtCreatedOn) VALUES(%s,%s,%s)",
    #############################################################################################
    "getTodoList": "SELECT pklTaskId AS taskId, \
                    vsTask AS Task, \
                    bstatus AS Status \
                    FROM taskList;",
    #############################################################################################
    "markToDoComplete": "UPDATE taskList \
                        SET bStatus = 1 \
                        WHERE pklTaskId = %s",
    #############################################################################################
    "deleteTodo":"DELETE FROM taskList \
                WHERE pklTaskId = %s"
}