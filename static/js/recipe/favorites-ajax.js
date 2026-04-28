let favoriteForms = document.querySelectorAll(".ajax-form-feature");

favoriteForms.forEach(function(form) {
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        let button = form.querySelector("button");
        let wasFavorite = button.classList.contains("btn-twitch");
        if (button.classList.contains("btn-twitch")){
            button.classList.remove("btn-twitch", "text-white")
            button.classList.add("btn-warning", "text-black")
            button.innerHTML = "★<span>Unfavorite</span>";
        }
        else{
            button.classList.remove("btn-warning", "text-black")
            button.classList.add("btn-twitch", "text-white")
            button.innerHTML = "☆<span>Favorite</span>";
        }
        button.disabled = true;
        let url = form.action; 
        let formData = new FormData(form);
        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {"Accept": "application/json"}
        })
        .then(response => {
            if (!response.ok){
                throw new Error('Something went wrong! Server or client has troubles.');
            };
            return response.json()
        }) 
        .then(data => {
            let button = form.querySelector("button");
            if ((data.user_recipe_is_favorite === true)){
                console.log("Favorite added success!")
            }
            console.log(data)})
        .catch(error => {
            if (wasFavorite){
                button.classList.remove("btn-warning", "text-black")
                button.classList.add("btn-twitch", "text-white")
                button.innerHTML = "☆<span>Favorite</span>";
            }
            else{
                button.classList.remove("btn-twitch", "text-white")
                button.classList.add("btn-warning", "text-black")
                button.innerHTML = "★<span>Unfavorite</span>";
            }
            console.error("There was an error", error);
            })
        .finally(() => {
            button.disabled = false;
        });
        });
    });
    