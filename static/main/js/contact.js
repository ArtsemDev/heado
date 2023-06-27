'use strict'

$('a#contact').click(function (e) {
    e.preventDefault()
    let form = document.querySelector('form#contact-form')
    let data = {
        name: form.name.value,
        email: form.email.value,
        message: form.message.value
    }
    $.ajax({
        url: '/api/contact',
        method: 'post',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function (data) {
            document.querySelector('div.alert-success').innerHTML = data.detail
            document.querySelector('div.alert-danger').innerHTML = ''
            document.querySelector('form#contact-form').querySelector('input#name').value = ''
            document.querySelector('form#contact-form').querySelector('input#email').value = ''
            document.querySelector('form#contact-form').querySelector('textarea#message').value = ''
        },
        error: function (response) {
            document.querySelector('div.alert-success').innerHTML = ''
            document.querySelector('div.alert-danger').innerHTML = response.responseJSON.detail[0].msg
        }
    })
})
