$(document).ready(function(){

jQuery.validator.addMethod("customNombre", function(value, element) { 
   return this.optional( element ) || /^([a-zA-Z])+$/.test( value ); 
   }, "Porfavor, solo letras");

jQuery.validator.addMethod("customEmail", function(value, element) { 
return this.optional( element ) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value ); 
}, "Porfavor, ingresa un correo valido. Ejemplo: correo@mail.com");

jQuery.validator.addMethod("noEspacio",function(value, element) { 
   return value == '' || value.trim().length != 0;  
 }, "No espacios");


   var $Contactoform = $('#FormularioContacto');
   if($Contactoform.length){
      $Contactoform.validate({
         rules:{
            nombre:{
               required: true,
               minlength: 3,
               maxlength: 30,
               customNombre: true
            },
            telefono:{
               number: true,
               minlength:9,
               maxlength:11,
               noEspacio: true
            },
            email:{
               required: true,
               noEspacio: true,
               customEmail: true
            },
            mensaje:{
               required: false,
               minlength:10,
               maxlength: 50
            },
            problema:{
               required:true
            },
            archivo:{
               required:true
            }
         },
         messages:{
            nombre:{
               required: 'El nombre es obligatorio.',
               minlength:'El nombre debe tener minimo 4 caracteres',
               maxlength:'El nombre debe tener maximo 30 caracteres'
            },
            telefono:{
               minlength: 'El numero tiene que tener al menos 9 digitos',
               maxlength: 'El numero no puede superar los 11 digitos'
            },
            email:{
               required: 'El correo es obligatorio.',
               email:'Ingrese un correo valido.'
            },
            mensaje:{
               minlength:'El mensaje no puede ser menor a 10 caracteres',
               maxlength:'El mensaje no puede ser mayor a 50 caracteres'
            },
            problema:{
               required:'Debes elegir un tipo problema'
            },
            archivo:{
               required:'Debe seleccionar un archivo como evidencia'
            }
         }
      });
   }
});




function mouseover(a){
   a.style.color= "#1D8348";
   a.style.fontSize ="70px";
   a.style.transitionDuration=".5s";
}
function mouseout(a){
   a.style.color= "black";
   a.style.fontSize ="56px";
}

function mouseover2(b){
   b.style.color="black";
}
function mouseout2(b){
   b.style.color="white";
}
function mouseover3(a){
   a.style.color= "#1D8348";
   a.style.fontSize ="35px";
   a.style.transitionDuration=".5s";
}
function mouseout3(a){
   a.style.color= "black";
   a.style.fontSize ="28px";
}
