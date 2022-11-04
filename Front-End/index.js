import  express  from "express";
import router from "./routes/index.js";

const app =express();

app.use(express.json())

const port = process.env.PORT || 3000;

app.set('view engine','pug')
//Agregar raouter
app.use('/',router);

app.use(express.static('public'))

app.listen(port, ()=>{
        console.log(`El servidor corre en el puerto ${port}`)
})

