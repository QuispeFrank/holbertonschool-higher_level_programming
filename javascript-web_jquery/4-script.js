/**
 * JavaScript script that toggles the class
 * of the <header> element when the user clicks
 * on the tag DIV#toggle_header
 */

$('#toggle_header').click(() => {
    $('header').toggleClass('red green');
    }
)
