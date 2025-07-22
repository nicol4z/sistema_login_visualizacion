$(document).ready(function () {

    $("#login-form").submit(function (e) {
        e.preventDefault();

        // Capturo los valores ingresados por el usuario
        const username = $("#username").val();
        const password = $("#password").val();

        // llamado ajax al backend para procesar el login
        $.ajax({
            url: "/login",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ username, password }),

            // si las credenciales son correctas, redirecciona al dashboard
            success: function () {
                window.location.href = "/dashboard";
            },

            // Si hay error (error en las credenciales) muestra alerta con el detalle
            error: function (xhr) {
                const error = xhr.responseJSON?.detail || "Error al iniciar sesión";
                alert(error);
            }
        });
    });
});
