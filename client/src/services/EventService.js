import axios from "axios";

// const server = axios.create({
//     baseURL: `http://192.168.0.104`,
//     withCredentials: false,
//     headers:{
//         Accept:"application/json",
//         "Content-Type":"application/json"
//     },
//     timeout:10000
// });

export default{
    getToDoList(){
        return axios.get("http://localhost:8080/getTodo");
    },

    markToDoComplete(todoObj){
        return axios.post("http://localhost:8080/markTodoComplete", todoObj,
        {
            headers: {
              // 'application/json' is the modern content-type for JSON, but some
              // older servers may use 'text/json'.
              // See: http://bit.ly/text-json
              'content-type': 'application/json'
            }
          });
          
    // res.data.headers['Content-Type']; // text/json)
    }
}