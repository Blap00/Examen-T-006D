function ajaxote() {
    var codigoSeguimiento = $('#consultaSeguimiento').val();
    // $.ajax({
    //     url:"http://127.0.0.1:8000/api/lista_boleta?format=json", 
    //     type: "GET",
    //         success: function(resultado){
    //             for (elem of resultado){
    //                 numBoleta = elem.idBoleta;
    //                 inputConsulta = $('#consultaSeguimiento').val();
    //                 encontrada = "<p id='mensajeConsulta' name='mensajeConsulta' style='color:#0BD555;'>El pedido numero "+elem.idBoleta+" se ha encontrado</p>";
    //                 noEncontrada = "<p id='mensajeConsulta' name='mensajeConsulta' style='color:#FF0000;'>No se ha encontrado el pedido ingresado</p>";
    //                 console.log(inputConsulta);
    //                 console.log(elem);
    //                 console.log(numBoleta);
    //                 if (inputConsulta == numBoleta){
    //                     $("#mensajeConsulta")[0].outerHTML = encontrada;
    //                     $("#btnConsultaPedido").click(ajaxote);
    //                     $.ajax({
    //                         url:`http://127.0.0.1:8000/api/detalle_boleta/${codigoSeguimiento}/`,
    //                         type:"GET"
    //                     });
    //                     console.log('Cai en el if')
    //                     break;
    //                 }
    //                 else if (inputConsulta != numBoleta){
    //                     $("#mensajeConsulta")[0].outerHTML = noEncontrada;
    //                     $("#btnConsultaPedido").click(ajaxote);
    //                     console.log('Cai en el elif')
    //                 }
    //                 else{
    //                     $("#mensajeConsulta")[0].outerHTML = noEncontrada;
    //                     $("#btnConsultaPedido").click(ajaxote);
    //                     console.log('Cai en el else')
                        
    //                 }
    //             }
    //         },
    //         error: function(error){
    //             console.log(error);
    //         }
    // })
    $.ajax({
        url: `/api/detalle_boleta/${codigoSeguimiento}/`,
        type: 'GET',
        success: function(data){
            var fecha_pedido = new Date(data.fecha);
            var fecha_actual = new Date();
            console.log(fecha_pedido);
            console.log(fecha_actual);
            dias_diff = parseInt((fecha_actual - fecha_pedido) / (1000 * 60 * 60 * 24));
            $("#mensajeConsulta")[0].outerHTML = '';
            if (dias_diff <= 2) {
                $('#barrita_progreso')[0].style.width = "25%";
            }
            else if (dias_diff == 3 || dias_diff == 4) {
                $('#barrita_progreso')[0].style.width = "50%";
            }
            else if (dias_diff == 5 || dias_diff == 6) {
                $('#barrita_progreso')[0].style.width = "75%";
            }
            else {
                $('#barrita_progreso')[0].style.width = "100%";
            }
        },
        error: function(){
            noEncontrada = "<p id='mensajeConsulta' name='mensajeConsulta' style='color:#FF0000;'>No se ha encontrado el pedido ingresado</p>";
            $("#mensajeConsulta")[0].outerHTML = noEncontrada;
        }
    });
}

$(document).ready(function(){
    $("#btnConsultaPedido").click(ajaxote);
});

