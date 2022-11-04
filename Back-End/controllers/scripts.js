//Esta parte es la que manda llamar los archivos pug, es decir las vistas
import inventory from "./Setinventory.js";
import ansible from "./Ansible.js";


const API = (req,res) =>{
    // console.log(req)
    // console.log(req.body)
    res.json({msg: 'Recibiendo Controladores'})
    const {Controladores} = req.body
    // console.log(Controladores)
    for(let i=0;i<Controladores.length;i++){
        console.log(Controladores[i])
        inventory(Controladores[i])
        ansible(Controladores[i])
    }
}

export default API;