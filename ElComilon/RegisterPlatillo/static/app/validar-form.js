function validarCamposVacios(){
    var nombre = document.getElementById("Nombre").value;
    var ingredientes = document.getElementById("Ingredientes").value;
    var valor = document.getElementById("Valor").value;

    if (nombre.length==0){
        errorNombre.style.visibility='visible';
    }
    else{
        console.log("Ta wena la cosa");
    }

    if (ingredientes.length==0){
        errorIngredientes.style.visibility='visible';
    }
    else{
        console.log("Ta wena la cosa");
    }

    if (valor.length==0){
        errorValor.style.visibility='visible';
    }
    else{
        console.log("Ta wena la cosa");
    }
}