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
    }
}