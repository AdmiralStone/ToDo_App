module.exports = {
        devServer: {
            proxy: {
                '/getTodo':{
                    target:'http://localhost:5000/',
                },
                '/markTodoComplete':{
                    target:'http://localhost:5000/'
                },
                '/addTask':{
                    target:'http://localhost:5000/'
                }
            }
    }
    
}