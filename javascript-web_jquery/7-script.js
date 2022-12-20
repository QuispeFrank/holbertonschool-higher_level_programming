/**
 * JavaScript script that fetches the character name from
 * this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
 * The name will be displayed in the HTML tag DIV#character
 */

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (res, status) => {
    if (status === 'success') {
        $('#character').append(res.name);
    }
})
