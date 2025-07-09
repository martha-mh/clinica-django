$(document).ready(function () {

    /**** Para los mensajes *****/

    const $messageDiv = $('#swal-message');
    if ($messageDiv.length > 0) {
        const text = $messageDiv.data('text');
        const type = $messageDiv.data('type');
        if (text) {
            Swal.fire({
                icon: type === 'error' ? 'error' : 'success',
                text: text,
                showConfirmButton: false,
                timer: 2000
            });
        }
    }

    /**** FIN Para los mensajes *****/


    /***** Eventos *****/

    $('.btn-delete-appointment').click(function (e) {
        e.preventDefault();
        const url = $(this).attr('href');

        Swal.fire({
            title: 'Aviso',
            text: '¿Está seguro de que desea eliminar esta cita?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = url;
            }
        });
    });

    $('.btn-reset-appointment').click(function (e) {
        e.preventDefault();
        const url = $(this).attr('href');

        Swal.fire({
            title: 'Aviso',
            text: '¿Está seguro de que desea restaurar esta cita?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#28a745',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Sí, restablecer',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
            window.location.href = url;
            }
        });
    });

    $('#appointment-form').on('submit', function () {
        $('#id_patient').prop('disabled', false);
    });

    $('.btn-delete-doctor').click(function (e) {
        e.preventDefault();
        const url = $(this).attr('href');

        Swal.fire({
            title: 'Aviso',
            text: '¿Está seguro de que desea eliminar este doctor?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = url;
            }
        });
    });

    $('.btn-delete-patient').click(function (e) {
        e.preventDefault();
        const url = $(this).attr('href');

        Swal.fire({
            title: 'Aviso',
            text: '¿Está seguro de que desea eliminar este paciente?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#3085d6',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = url;
            }
        });
    });


    /***** FIN Eventos *****/

    $('#id_patient').select2({
        width: '100%',
        placeholder: "Selecciona un paciente",
        allowClear: true
    });

    $('#id_doctor').select2({
        width: '100%',
        placeholder: "Selecciona un doctor",
        allowClear: true
    });
});