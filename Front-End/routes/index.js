import  express  from "express";
import {Indexuna, Parametroscontrollador} from '../Controllers/inicioUna.js'


const router = express.Router()
//Aqui a tra vez del router se llama a las variables importadas del controlador que indican la vista en pug
router.get('/', Indexuna);

router.get('/Controladores',Parametroscontrollador);


export default router;