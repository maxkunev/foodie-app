let favoriteForms = document.querySelectorAll(".ajax-form-feature");

favoriteForms.forEach(function(form) {
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        let button = form.querySelector("button");
        let classlist_origin = button.classList
        if (button.classList.contains("btn-twitch")){
            button.classList.remove("btn-twitch", "text-white")
            button.classList.add("btn-warning", "text-black")
            button.innerText = "🖤 Unfavorite";
        }
        else{
            button.classList.remove("btn-warning", "text-black")
            button.classList.add("btn-twitch", "text-white")
            button.innerText = "🤍Favorite";
        }
        let url = form.action; 
        let formData = new FormData(form);
        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {"Accept": "application/json"}
        })
        .then(response => {
            if (!response.ok){
                throw new Error('Something went wrong! Server has trouble.')
                button.classList = classlist_origin;
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
            console.error("There was an error", error);
            });
        });
    });

   