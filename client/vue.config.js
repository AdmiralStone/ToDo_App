module.exports = {
        devServer: {
            proxy: {
                '/getTodo':{
                    target:'http://localhost:5000/',
                }
            }
    }
    
}