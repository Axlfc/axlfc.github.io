<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Random Image Search</title>
    <style>
        .search-container {
            max-width: 800px;
            margin: 20px auto;
            text-align: center;
        }
        
        .cat-image {
            max-width: 300px;
            margin-bottom: 20px;
        }
        
        /* Hide default Google branding if desired */
        .gsc-control-cse {
            padding: 0 !important;
            border: none !important;
        }
        
        /* Ensure results appear below the search box */
        .gcse-searchresults-only {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="search-container">
        <img id="randomImage" src="" alt="Imagen aleatoria" class="cat-image">
        
        <!-- Search box -->
        <div class="gcse-search" data-hl="es" data-gname="randomImageSearch">
            <div class="gsc-control-cse">
                <div class="gsc-search-box-tools">
                    <div class="gsc-search-box">
                        <input type="text" placeholder="Buscar" class="gsc-input">
                        <div class="gsc-search-button">
                            <button class="gsc-search-button-v2" title="" aria-label="Buscar" type="button">
                                <svg class="gsc-search-button-v2-spacer" width="13" height="13" viewBox="0 0 13 13">
                                    <title>Buscar</title>
                                    <path d="M12.706 12.293l-0.707 0.707-4.058-4.061c-1.356 0.96-2.99 1.526-4.753 1.526-4.418 0-8-3.582-8-8s3.582-8 8-8 8 3.582 8 8c0 1.763-0.566 3.397-1.526 4.753z"></path>
                                </svg>
                            </button>
                        </div>
                        <div id="buttonText" style="display: none;"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script>
        // List of images and corresponding button texts
        const images = {
            "images/gato.jpg": "Salva al gatito",
            "images/carlos.jpg": "Salva al imperio",
            "images/claudio.jpg": "Fregquishimo",
            "images/marlo.jpg": "Dale al puto botón"
        };
        // Randomly select an image and button text
        const keys = Object.keys(images);
        const randomKey = keys[Math.floor(Math.random() * keys.length)];
        const buttonText = images[randomKey];
        // Set the random image source
        document.getElementById("randomImage").src = randomKey;
        // Set the button text
        document.getElementById("buttonText").textContent = buttonText;
        document.getElementById("buttonText").style.display = "inline";
    </script>
</body>
</html>
