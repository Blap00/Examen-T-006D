$(document).ready(function(){
    jQuery.validator.addMethod("customNombre", function(value, element) { 
       return this.optional( element ) || /^([a-zA-Z0-9])+$/.test( value ); 
       }, "Porfavor, solo letras");
    
    jQuery.validator.addMethod("customEmail", function(value, element) { 
    return this.optional( element ) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value ); 
    }, "Porfavor, ingresa un correo valido. Ejemplo: correo@mail.com");
    
    jQuery.validator.addMethod("noEspacio",function(value, element) { 
       return value == '' || value.trim().length != 0;  
     }, "No espacios");
    
    
       var $formulario = $('#formularioRegistro');
       if($formulario.length){
          $formulario.validate({
             rules:{
                username:{
                   required: true,
                   minlength: 3,
                   maxlength: 30,
                   customNombre: true
                },

                email:{
                   required: true,
                   noEspacio: true,
                   customEmail: true
                },
                contraseña:{
                   required: true,
                   noEspacio:true,
                   minlength:3,
                   maxlength: 50
                }
             },
             messages:{
                username:{
                   required: 'El nombre es obligatorio.',
                   minlength:'El nombre debe tener minimo 4 caracteres',
                   maxlength:'El nombre debe tener maximo 30 caracteres'
                },
                email:{
                   required: 'El correo es obligatorio.',
                   email:'Ingrese un correo valido.'

                },
                contraseña:{
                    required: 'La clave es obligatoria',
                    minlength: 'La clave debe contener minimo 3 caracteres',
                    maxlength: 'La clave debe contener maximo 50 caracteres'
                 }
             }
          });
       }
    });
    