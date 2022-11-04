import  express  from "express";
import router from "./routes/api.js";
import cors from 'cors';

const app =express();
app.use(cors())
app.use(express.json())

const port = process.env.PORT || 4000;

const allowedOrigins = ['http://localhost:3000/'];

const options = {
  origin: allowedOrigins
};

// Then pass these options to cors:
app.use(cors(options));

app.use('/',router);

app.use(express.static('public'))

app.listen(port, ()=>{
        console.log(`El servidor corre en el puerto ${port}`)
})

