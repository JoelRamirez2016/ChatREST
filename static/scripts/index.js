$(document).ready(function() {

    /**
     * funcion para refrescar los mensages
     */
    let refrescarTablaEstadoSala = function() {  
        $("#chatmsg_refresh").load('msgcontent".do?randval='+ Math.random() + " #msgcontent", function(){                        
            var elem = document.getElementById('msgcontent');
            elem.scrollTop = elem.scrollHeight            
        });
    }

    var refreshId = setInterval(refrescarTablaEstadoSala, 5000);
    $.ajaxSetup({ cache: false });  
    

    /**
     * modificar visual input de imagen para mostrar nombre de la imagen antes de enviar
     */
    document.querySelector('.custom-file-input').addEventListener('change',function(e){
        var fileName = document.getElementById("inputImage").files[0].name;
        var nextSibling = e.target.nextElementSibling
        nextSibling.innerText = fileName
    })
    /**
     * concatenacion visual del mensaje propio en el chat
     */
    let appenedmsg = function (data) {
        var newid = 'msg_' + data.id;
        var newmsg = $("#msg_nn").clone().attr('id', newid).show();
        if( data.user_writer_id == $('#actual_user').val() ) newmsg.addClass('chat-msg-my float-right')
        else newmsg.addClass('chat-msg-other float-left')
        $("h4", newmsg).text(data.content_txt);
        if( data.content_img !== null ){
            $("img", newmsg).attr("src",data.content_img).show();  
        }       
        newmsg.appendTo("#msgcontent");
        console.log(data)
    }
    /**
     * Envio de formulario para la creacion y almacenamiento de mensajes
     */
    $('#formMsgDta').submit(function(e){
        e.preventDefault();    
        var formData = new FormData(this);

        $.ajax({
            headers : {
                'X-CSRFToken' : $('input[name ="csrfmiddlewaretoken"]').val()
            },
            url: '../messages/',
            type: 'POST',
            data: formData,
            success: function (data) {
                appenedmsg(data);
                $('#inputImage').val('');
                $('#content_txt').val('');
            },
            cache: false,
            contentType: false,
            processData: false
        });
    })
    /**
     * actializacion visual del borrado de mensajes propios
     */
    $('body').on('click', '.deleteButton', function() {
        idmsg = $(this).attr('id').substr($(this).attr('id').indexOf("_") + 1);
        $.ajax({
            headers : {
                'X-CSRFToken' : $('input[name ="csrfmiddlewaretoken"]').val()
            },
            url: '../messages/' + idmsg + '/',
            type: 'DELETE',
            success: function(result) {
                $('#msg_' + idmsg).remove()
            }
        });
    });
    // $('.deleteButton').click(function(){
    //     idmsg = $(this).attr('id').substr($(this).attr('id').indexOf("_") + 1);
    //     $.ajax({
    //         headers : {
    //             'X-CSRFToken' : $('input[name ="csrfmiddlewaretoken"]').val()
    //         },
    //         url: '../messages/' + idmsg + '/',
    //         type: 'DELETE',
    //         success: function(result) {
    //             $('#msg_' + idmsg).remove()
    //         }
    //     });
    // })  

    
    /* Imposible de usar
    let cargar_mensajes_ajax = function() {   //calls click event after a certain time      
        var time;
        setTimeout(function () {
            console.log('wait')   
            time++;
        }, 10000); 
        $.ajax({
            headers : {
                'X-CSRFToken' : $('input[name ="csrfmiddlewaretoken"]').val()
            },
            url: '../messages/' + '?page=' + page,  
            async: false,        
            type: 'GET',
            success: function (data) {                
                page++;
                var maxmsg = $("#msg_nn").prev()
                maxidmsg = maxmsg.attr('id').substr(maxmsg.attr('id').indexOf("_") + 1);
                index = data.results.findIndex(x => x.id == maxidmsg);
                if( index != -1){
                    console.log(index,data.results)
                }
                cargar_mensajes_ajax();
            },
            cache: false,
            contentType: false,
            processData: false
        }).fail( function( jqXHR, textStatus, errorThrown ) {
            page--
            setTimeout(function () {
                console.log('wait')   
            }, 10000); 
            cargar_mensajes_ajax()               
        })
        return time;
    }   

    async function asyncCall() {
        cargar_mensajes_ajax();
    }
      
    asyncCall();*/
});