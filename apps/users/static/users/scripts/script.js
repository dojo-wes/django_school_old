$(document).ready(function() {
  $('#reg-form').submit(function(e) {
    e.preventDefault();
    $.ajax({
      url: '/users/create/',
      type: 'post',
      headers: {
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()
      },
      data: {
        email: $('#reg-email').val(),
        password: $('#reg-password').val()
      },
      success: function(data) {
        console.log('this is the data coming back from the server', data);
        window.location.href = '/users';
      },
      error: function(data) {
        const errors = JSON.parse(data.responseText).errors;
        let htmlStr = '<ul class="errors">';
        for(error of errors) {
          htmlStr += `
            <li>${error}</li>
          `;
        };
        htmlStr += '</ul>';
        $('#reg-form').prepend(htmlStr);
        $('#reg-password').val('');
      }
    });
  })
});