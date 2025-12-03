// CSRF Token function for Django
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

    $("#bookingForm input").jqBootstrapValidation({
        preventSubmit: true,

        submitSuccess: function ($form, event) {
            event.preventDefault();

            var fname = $("input#fname").val();
            var lname = $("input#lname").val();
            var name = fname + ' ' + lname;
            var mobile = $("input#mobile").val();
            var email = $("input#email").val();
            var date_1 = $("input#date-1").val();
            var date_2 = $("input#date-2").val();
            var request = $("input#request").val();

            var $button = $("#bookingButton");
            $button.prop("disabled", true);

            $.ajax({
               url: "/booking-form/",   // Django URL
                type: "POST",
                headers: { "X-CSRFToken": csrftoken },  // Important
                data: { 
                    fname: fname,
                    lname: lname,
                    mobile: mobile,
                    email: email,
                    date_1: date_1,
                    date_2: date_2,
                    request: request
                },

                success: function () {
                    $('#success').html("<div class='alert alert-success'>");
                    $('#success > .alert-success')
                        .append("<strong>Booking successfully saved in database!</strong>");
                    $('#success > .alert-success')
                        .append("</div>");
                    
                    $('#bookingForm').trigger("reset");
                },

                error: function () {
                    $('#success').html("<div class='alert alert-danger'>");
                    $('#success > .alert-danger')
                        .append("<strong>Sorry " + name + ", something went wrong!</strong>");
                    $('#success > .alert-danger')
                        .append("</div>");
                },

                complete: function () {
                    setTimeout(function () {
                        $button.prop("disabled", false);
                    }, 1000);
                }
            });
        },

        filter: function () {
            return $(this).is(":visible");
        },
    });

});

$('#bookingForm input').focus(function () {
    $('#success').html('');
});
