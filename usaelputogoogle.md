<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Random Image Search</title>
    <style>
        .search-container {
            max-width: 800px;
            margin: 20px auto;
            text-align: center;
            padding-bottom: 300px; /* Adds padding below the search box */
        }
        
        .cat-image {
            max-width: 300px;
            margin-bottom: 20px;
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }

        .image-button {
            padding: 10px 20px;
            font-size: 14px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
        }

        .image-button:hover {
            background-color: #0056b3;
        }

        /* Hide the default magnifying glass icon */
        .gsc-search-button-v2 svg {
            display: none !important;
        }

        /* Add custom text to the search button using pseudo-element */
        .gsc-search-button-v2::after {
            content: attr(data-custom-text); /* Use a custom attribute for the button text */
            font-size: 14px;
            color: white;
            padding: 0 10px;
        }

        /* Ensure results appear below the search box */
        .gcse-searchresults-only {
            margin-top: 20px;
        }
    </style>
    <!-- Google CSE Script -->
    <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
</head>
<body>
    <div class="search-container">
        <!-- Random image display -->
        <img id="randomImage" src="images/gato.jpg" alt="Imagen aleatoria" class="cat-image">

        <!-- Google Custom Search Box and Results -->
        <div class="gcse-search" data-hl="es" data-gname="randomImageSearch" data-title="[SEARCHTEXT]"></div>

        <!-- Container for the image-switching buttons at the bottom -->
        <div class="button-container">
            <button class="image-button" onclick="setImage('gato')">Salva al gatito</button>
            <button class="image-button" onclick="setImage('carlos')">Salva al imperio</button>
            <button class="image-button" onclick="setImage('claudio')">Fregquishimo</button>
            <button class="image-button" onclick="setImage('marlo')">Dale al puto botón</button>
        </div>
    </div>

    <script>
        // List of images and corresponding button texts
        const images = {
            "gato": { src: "images/gato.jpg", text: "Salva al gatito" },
            "carlos": { src: "images/carlos.jpg", text: "Salva al imperio" },
            "claudio": { src: "images/claudio.jpg", text: "Fregquishimo" },
            "marlo": { src: "images/marlo.jpg", text: "Dale al puto botón" }
        };

        // Function to set a specific image and update search button text
        function setImage(key) {
            const imageData = images[key];
            document.getElementById("randomImage").src = imageData.src;
            updateSearchButtonText(imageData.text);
        }

        // Function to set a random image on page load
        window.onload = function() {
            const keys = Object.keys(images);
            const randomKey = keys[Math.floor(Math.random() * keys.length)];
            setImage(randomKey);
        };

        // Function to update the search button text dynamically
        function updateSearchButtonText(text) {
            const searchButton = document.querySelector('.gsc-search-button-v2');
            if (searchButton) {
                searchButton.setAttribute('data-custom-text', text);
            }
        }

        // Ensures search button text updates once Google CSE has loaded
        window.addEventListener('load', () => {
            // Wait for the Google search button to load, then set the initial button text
            setTimeout(() => {
                const searchButton = document.querySelector('.gsc-search-button-v2');
                if (searchButton) {
                    updateSearchButtonText(images["gato"].text); // Set default text to initial image
                }
            }, 500);
        });
    </script>
</body>
</html>
