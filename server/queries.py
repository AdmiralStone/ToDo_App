queries ={
    "createTask": "INSERT INTO taskList(vsTask, bStatus, dtCreatedOn) VALUES(%s,%s,%s)",
    "getTodoList": "SELECT pklTaskId AS taskId,\
                    vsTask AS Task,\
                    bstatus AS Status\
                    FROM taskList"
}