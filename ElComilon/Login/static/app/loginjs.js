
const inputNombreusuario = document.getElementById("nameUser")
const inputPassword = document.getElementById("passwordUser")
const txt_error = document.getElementById('txt_error')
const txt_errorpass = document.getElementById('txt_errorpass')
const expresiones = {
	usuario: /^[a-z]+$/, // Letras, numeros, guion y guion_bajo
	password: /^.{4,12}$/, // 4 a 12 digitos.
}
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const Guardardatos = () => { 
//     const FormLogin = new FormData(document.getElementById('Form_login'))
//     fetch ("/",{
//         method: "POST",
//         body: FormLogin,
//         headers: {
//             "X-CSRFToken": getCookie('csrftoken'),
//         }
//     })
// }

// const Validarcampo = () =>{
// if(inputNombreusuario.value.length < 8){
//     inputNombreusuario.classList.add('inputinvalido')
//     txt_error.classList.remove('txtp')
//     txt_error.classList.add('TxtERROR')
//     txt_error.innerHTML = "El nombre de usuario debe ser minimo 8 caracteres" 
//     console.log("campos vacio") 
    
//   }
//     else{
//       txt_error.innerHTML = "Nombre de usuario valido" 
//       txt_error.classList.remove('TxtERROR')
//       txt_error.classList.add('txtexito')
//       inputNombreusuario.classList.remove('inputinvalido')
//       inputNombreusuario.classList.add('valido')
     
//     }   
//  if(inputPassword.value.length < 8) {
//   inputPassword.classList.add('inputinvalido')
//     txt_errorpass.classList.add('TxtERROR')
//     txt_errorpass.innerText = "La contraseña debe ser minimo 8 caracteres"
    
//  }
//     else{

//       txt_errorpass.innerHTML = "Contraseña valida" 
//       txt_errorpass.classList.remove('TxtERROR')
//       txt_errorpass.classList.add('txtexito')
//       inputPassword.classList.remove('inputinvalido')
//       inputPassword.classList.add('valido')
//       return
//     }
// }




