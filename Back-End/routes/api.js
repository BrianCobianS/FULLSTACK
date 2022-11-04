import  express  from "express";
import API from '../controllers/scripts.js'


const router = express.Router()
//Aqui a tra vez del router se llama a las variables importadas del controlador que indican la vista en pug
router.post('/',API)

export default router;