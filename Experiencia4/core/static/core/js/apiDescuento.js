function ajaxito() {
    var codigoDescuento;
    var inputDescuento;
    var buttonSuccess;
    var buttonError;
    var buttonNotFound;
    $.ajax({
        url:"http://127.0.0.1:8000/api/lista_descuento?format=json", 
        type: "GET",
            success: function(resultado){
                for (elem of resultado){
                    codigoDescuento = elem.IdCodigo;
                    inputDescuento = $('#inputDes').val();
                    buttonSuccess = "<button type='button' class='btn btn-outline-success' name='checkDescuento' id='checkDescuento'>Descuento del "+elem.Porcentaje+"% a sido aplicado</button>";
                    buttonError = "<button type='button' class='btn btn-outline-danger' name='checkDescuento' id='checkDescuento'>El código de descuento no existe</button>";
                    buttonNotFound = "<button type='button' class='btn btn-outline-warning' name='checkDescuento' id='checkDescuento'>No se ha ingresado ningun codigo</button>";

                    if (inputDescuento == codigoDescuento){
                        $("#checkDescuento")[0].outerHTML = buttonSuccess;
                        $("#checkDescuento").click(ajaxito);
                        $.ajax({
                            url:`http://127.0.0.1:8000/api/detalle_descuento/${codigoDescuento}/`,
                            type:"GET"
                        });
                        break;
                    }
                    else if (inputDescuento != codigoDescuento){
                        $("#checkDescuento")[0].outerHTML = buttonError;
                        $("#checkDescuento").click(ajaxito);
                    }
                    else{
                        $("#checkDescuento")[0].outerHTML = buttonNotFound;
                        $("#checkDescuento").click(ajaxito);
                    }
                }
            },
            // error: function(error){
            //     console.log(error);
            // }
    })
}

$(document).ready(function(){
    $("#checkDescuento").click(ajaxito);
});

