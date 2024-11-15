<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Random Image Search</title>
    <style>
        .search-container {
            max-width: 800px;
            margin: 20px auto;
            text-align: center;
            padding-bottom: 300px;
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

        .gsc-search-button-v2 svg {
            display: none !important;
        }

        .gsc-search-button-v2::after {
            content: attr(data-custom-text);
            font-size: 14px;
            color: white;
            padding: 0 10px;
        }

        .gcse-searchresults-only {
            margin-top: 20px;
        }
    </style>
    <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
</head>
<body>
    <div class="search-container">
        <img id="randomImage" src="images/gato.jpg" alt="Imagen aleatoria" class="cat-image">
        <div class="gcse-search" data-hl="es" data-gname="randomImageSearch" data-title="[SEARCHTEXT]"></div>
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

        let currentImageKey = null;

        // Function to set a specific image and update search button text
        function setImage(key) {
            const imageData = images[key];
            document.getElementById("randomImage").src = imageData.src;
            currentImageKey = key;
            updateSearchButtonText(imageData.text);
        }

        // Function to set a random image on page load
        function setRandomImage() {
            const keys = Object.keys(images);
            const randomKey = keys[Math.floor(Math.random() * keys.length)];
            setImage(randomKey);
            return randomKey;
        }

        // Function to update the search button text dynamically
        function updateSearchButtonText(text) {
            const searchButton = document.querySelector('.gsc-search-button-v2');
            if (searchButton) {
                searchButton.setAttribute('data-custom-text', text);
            }
        }

        // Initialize on page load
        window.onload = function() {
            // Set initial random image and store the key
            currentImageKey = setRandomImage();
            
            // Set up an observer to ensure the button text is updated after Google CSE loads
            const observer = new MutationObserver((mutations, obs) => {
                const searchButton = document.querySelector('.gsc-search-button-v2');
                if (searchButton) {
                    updateSearchButtonText(images[currentImageKey].text);
                    obs.disconnect(); // Stop observing once we've updated the button
                }
            });

            // Start observing the document for the search button to appear
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        };
    </script>
</body>
</html>
