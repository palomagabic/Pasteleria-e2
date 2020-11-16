$(function () {
    $("#mi_formulario").validate({
        rules:
        {
            rut:
            {
                
                required:true,
                minlength:6,
                maxlength:10,
            },
            nombre:
            {
                required:true,
                minlength:6,
                maxlength:20,
            },
            email:
            {
                email: true,
                required: true,
                minlength: 6,
                maxlength: 100,
            },
            telefono:
            {
                required: true,
                minlength: 8,
                maxlength: 9,
            },
            direccion:
            {
                required: true,
                minlength: 4,
                
            },
   
        },
        messages:
        {
            rut:
            {

                required: "Debes ingresar un rut válido",
                minlength: "Debes ingresar un rut válido",
                maxlength: "sin puntos y con guion.",
            },
            email:
            {
                email: "Formato de email no válido.",
                required: "Debes ingresar un email válido",
                minlength: "Debes ingresar un email válido",
                maxlength: "Excedes el largo máximo permitido.",
            },
            nombre:
            {
                required:"Debes ingresar Nombre",
                minlength:"Debes ingresar entre 6 a 20 carateres.",
                maxlength:"Debes ingresar entre 6 a 20 carateres.",
            },
            telefono:
            {
                required: "Debes ingresar Telefono",
                minlength: "Ingrese telefono correcto.",
                maxlength: "Ingrese telefono correcto.",
            },
            direccion:
            {
                required: "Debes ingresar direccion",
                minlength: "Ingrese direccion valida.",

            },

        }
    });
});