
function eliminar_trabajo(id){
    
    Swal.fire({

        "title" : "¿Desea eliminar un trabajo?",
        "text" : "Esta accion no se puede deshacer",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText":"Cancelar",
        "cofirmButtonText":"Elminar"
    })
    .then(function(result){
        if(result.isConfirmed){
            window.location.href = "/eliminar-trabajos/"+id+"/"
        }
    })

};