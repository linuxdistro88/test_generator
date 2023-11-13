// main.js
document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('recipe-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // get the form data
        var ingredients = document.getElementById('ingredients').value;
        var method = document.getElementById('method').value;
        var diet = document.getElementById('diet').value;

        // basic validation
        if (!ingredients || !method || !diet) {
            alert('Please fill out all fields.');
            return;
        }

        // send the POST request
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ingredients: ingredients,
                method: method,
                diet: diet
            })
        })
        .then(response => response.json())
        .then(data => {
            // update the recipe div with the response
            document.getElementById('recipe').innerText = data.response;
        });
    });
});
