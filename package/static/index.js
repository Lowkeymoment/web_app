document.addEventListener("DOMContentLoaded", function(){
    document.querySelector("form").onsubmit = function(){
        const name = document.querySelector("#name").value;
        alert(`You have submitted your name as: "${name}"`)
    }
});