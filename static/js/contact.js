// CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


$(function () {

    $("#contactForm").on("submit", function (event) {

        event.preventDefault();

        var name = $("#name").val();
        var email = $("#email").val();
        var subject = $("#subject").val();
        var message = $("#message").val();

        var $button = $("#sendMessageButton");
        $button.prop("disabled", true);

        $.ajax({
            url: "/contact-form/",
            type: "POST",
            headers: { "X-CSRFToken": csrftoken },
            data: {
                name: name,
                email: email,
                subject: subject,
                message: message
            },

            success: function () {
                $('#success').html("<div class='alert alert-success'>Message sent successfully!</div>");
                $('#contactForm').trigger("reset");
            },

            error: function () {
                $('#success').html("<div class='alert alert-danger'>Something went wrong!</div>");
            },

            complete: function () {
                setTimeout(function () {
                    $button.prop("disabled", false);
                }, 1000);
            }
        });

    });

});


$("#contactForm input, #contactForm textarea").focus(function () {
    $('#success').html('');
});
