let Botonsiguiente = document.getElementById("btn-siguiente")
const inputNombreusuario = document.getElementById("nameUser")
const inputPassword = document.getElementById("passwordUser")
const FormLogin = document.getElementById('Form_login')
const txt_error = document.getElementById('txt_error')
const txt_errorpass = document.getElementById('txt_errorpass')
const expresiones = {
	usuario: /^[a-z]+$/, // Letras, numeros, guion y guion_bajo
	password: /^.{4,12}$/, // 4 a 12 digitos.
}
const Validarcampo = (e) =>
{
if(inputNombreusuario.value.length < 8){
    inputNombreusuario.classList.add('inputinvalido')
    txt_error.classList.remove('txtp')
    txt_error.classList.add('TxtERROR')
    txt_error.innerHTML = "El nombre de usuario debe ser minimo 8 caracteres" 
    console.log("campos vacio") 
    
  }
    else{
      txt_error.innerHTML = "Nombre de usuario valido" 
      txt_error.classList.remove('TxtERROR')
      txt_error.classList.add('txtexito')
      inputNombreusuario.classList.remove('inputinvalido')
      inputNombreusuario.classList.add('valido')
     
    }
 if(inputPassword.value.length < 8) {
  inputPassword.classList.add('inputinvalido')
    txt_errorpass.classList.add('TxtERROR')
    txt_errorpass.innerText = "La contraseña debe ser minimo 8 caracteres"
    
 }
    else{

      txt_errorpass.innerHTML = "Contraseña valida" 
      txt_errorpass.classList.remove('TxtERROR')
      txt_errorpass.classList.add('txtexito')
      inputPassword.classList.remove('inputinvalido')
      inputPassword.classList.add('valido')
      return
    }
/*
   else {
    inputNombreusuario.classList.replace('inputinvalido','inputvalido')
    txt_error.classList.remove('TxtERROR')
    txt_error.classList.add('txtp')

    inputPassword.classList.replace('inputinvalido','inputvalido')
    txt_errorpass.classList.remove('TxtERROR')
    txt_errorpass.classList.add('txtp')
     console.log("EXito")
     return
   }

  return
  */
}

FormLogin.addEventListener("submit",e => {
  e.preventDefault()
  console.log("Enviando info")
  Validarcampo(e)
}
)






