
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
  console.log(inputNombreusuario.value)
  console.log(expresiones.usuario.test(inputNombreusuario))
  if(expresiones.usuario.test(inputNombreusuario)){
    txt_error.classList.replace('TxtERROR','txtp')
    inputNombreusuario.classList.replace('inputinvalido','inputvalido')
    console.log("campo usuario correcto") 
  }
  else{ 
    inputNombreusuario.classList.add('inputinvalido')
    txt_error.classList.replace('txtp','TxtERROR')
    console.log("campo usuario incorrecto") 
  }
  console.log(expresiones.password.test(inputPassword))
  if(expresiones.password.test(inputPassword)){
    console.log("campo password correcto")
  }
  else{ 
    inputPassword.classList.add('inputinvalido')
    txt_errorpass.classList.add('TxtERROR')
    console.log("campo password incorrecto")
  }
  return
}

FormLogin.addEventListener("submit",e => {
 
  e.preventDefault()
  Validarcampo(e)
}
)






