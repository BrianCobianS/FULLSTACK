//Esta parte es la que manda llamar los archivos pug, es decir las vistas
const Indexuna = (req,res) =>{
    res.render('index',{
        pagina: 'index'
    });
}
const Parametroscontrollador = (req,res) =>{
    res.render('Controladores',{
        pagina: 'Esto es una variable usable en la vista'
    });
}


export {
    Indexuna,
    Parametroscontrollador
}