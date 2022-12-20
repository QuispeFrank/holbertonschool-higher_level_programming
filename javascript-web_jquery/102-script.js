/**
 * JavaScript script that fetches and prints how to say “Hello” depending on the language
 * API service: https://www.fourtonfish.com/hellosalut/hello/
 */

$(document).ready(() => {
    $('#btn_translate').click(() => {

        // getting language code from input
        const lang = $('#language_code').val();

        // get request...
        $.get('https://stefanbohacek.com/hellosalut/?lang=' + lang, (res) => {
            $('#hello').html(res.hello);
        }).fail((err) => {console.error(err)});
    })
})
