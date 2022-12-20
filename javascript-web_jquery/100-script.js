/**
 * JavaScript script that updates the text color of the
 * <header> element to red (#FF0000),  using document.querySelector
 * to select the HTML tag.
 */

document.addEventListener('DOMContentLoaded', () => { 
    const FirstHeader = document.querySelector('header');
    FirstHeader.style.color = 'red';
})
