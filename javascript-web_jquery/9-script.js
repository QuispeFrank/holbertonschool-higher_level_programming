/**
 * JavaScript script that fetches from https://stefanbohacek.com/hellosalut/?lang=fr
 * and displays the value of hello from that fetch in the HTML tag DIV#hello
 * The translation of “hello” will be displayed in the HTML tag DIV#hello
 * The Script must work when it is imported from the <head> tag
 */

$.holdReady(true);
$(document).ready(() => $.holdReady(false));

$.get('https://stefanbohacek.com/hellosalut/?lang=fr', (res, status) => {
    if (status === 'success') {
        $('#hello').append(res.hello);
    }
})
