function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});


function csvExport(btn) {
    var documentName = btn.getAttribute('data-id');


    $.ajax({
        type: 'POST',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url: '/ajax/exportcsv/',
        data: {
            'document': documentName
        },
        dataType: 'json',
        "beforeSend": function (xhr, settings) {
            $(':button').prop('disabled', true);
            $('.ajax-loader').css("visibility", "visible");
            $('#success-message').css("visibility", "hidden");
            $.ajaxSettings.beforeSend(xhr, settings);
        },
        success: function (data) {
            $('#success-message').text(data.message);
            $('#success-message').css("visibility", "visible");
        },
        error: function (xhr, status, error) {
            var err = eval("(" + xhr.responseText + ")");
            alert(err.Message);
        },
        complete: function () {
            $('.ajax-loader').css("visibility", "hidden");
            $(':button').prop('disabled', false);
        }
    });
}

