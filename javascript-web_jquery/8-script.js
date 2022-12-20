/**  
 * JavaScript script that fetches and lists the title for all movies
 * by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
 * All movie titles will be list in the HTML tag UL#list_movies
 */

$.get('https://swapi-api.hbtn.io/api/films/?format=json', (res, status) => {
   if (status === 'success') {

    const allMovies = res.results;
    const titles = allMovies.map(movie => { return '<li>' + movie.title + '</li>' });
    $('#list_movies').append(titles);

   } 
})
