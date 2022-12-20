/**
 * JavaScript script that fetches and prints how to
 * say “Hello” depending on the language
 * API service: https://www.fourtonfish.com/hellosalut/hello/
 */

$(document).ready(() => {
    
    $('#language_code').keypress((event) => {
        // if press enter
        if (event.which === 13) {
            event.preventDefault();
            apiRequest();
        }
    })

    $('#btn_translate').click(() => {
        apiRequest();
    })

    function apiRequest() {

        // input value
        const lang = $('#language_code').val();

        // get request...
        $.get('https://stefanbohacek.com/hellosalut/?lang=' + lang, (res) => {
            $('#hello').html(res.hello);
        }).fail((err) => {
            console.error(err)
        });
    }
})
