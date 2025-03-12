let counter = 0;

function count(){
    counter++;
    document.querySelector('button').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count})