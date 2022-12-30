
import Enviarmail from "../helpers/mail.js";
import ansible from "./Ansible.js";
import now from "./Now.js";
import shel from "./shell.js";


const API = (req,res) =>{
    const eliminar = ['-','T',':']
    function removecharcter(x,b){
        while(x.indexOf(b)!= -1){
            x= x.replace(b,'')
        }    
        return x  
    }
    const {Controladores} = req.body
    for(let i=0;i<Controladores.length;i++){
        eliminar.forEach(element => Controladores[i].fecha=removecharcter(Controladores[i].fecha,element));
        console.log(Controladores[i])
        if (Controladores[i].fecha!= 'Now'){
            shel(Controladores[i]);
        }else{
            setTimeout(() => {
                ansible(Controladores[i]);
            }, 5000);
            now(Controladores[i])
        }
        console.log(Controladores[i].email)
        Enviarmail(Controladores[i])
    }    
    res.json({msg:`We have received the controller(s), you will receive an email(s) to the email(s) you registered with the installation status`})   

   

}
export default API;

