let favoriteForms = document.querySelectorAll(".ajax-form-feature");

favoriteForms.forEach(function(form) {
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        let url = form.action; 
        let formData = new FormData(form);
        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {"Accept": "application/json"}
        })
        .then(response => response.json()) 
        .then(data => {
            let button = form.querySelector("button");
            if ((data.user_recipe_is_favorite === true)){
                button.classList.remove("btn-twitch", "text-white")
                button.classList.add("btn-warning", "text-black")
                button.innerText = "🖤 Unfavorite";
            }
            else{
                button.classList.remove("btn-warning", "text-black")
                button.classList.add("btn-twitch", "text-white")
                button.innerText = "🤍Favorite";
            }
            console.log(data);
        });
    });
});
   