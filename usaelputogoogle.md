<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Random Image Search</title>
    <style>
        .search-container {
            max-width: 800px;
            margin: 20px auto;
            text-align: center;
            position: relative;
        }
        
        .cat-image {
            width: 100%;
            max-height: 300px;
        }
        
        .search-box {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            width: 80%;
            display: flex;
        }

        /* Customize the search input box */
        .gcse-search input.gsc-input {
            height: 30px;
            width: calc(100% - 120px);
            font-size: 16px;
            padding: 0 10px;
        }

        /* Custom styling for the search button */
        .gsc-search-button-v2 {
            width: 120px;
            font-size: 0 !important;
        }

        .gsc-search-button-v2:after {
            font-size: 14px;
            padding: 0 10px;
            display: inline-block;
        }

        /* Hide the search icon */
        .gsc-search-button-v2 svg {
            display: none !important;
        }
    </style>
</head>
<body>
    <div class="search-container">
        <img id="randomImage" src="" alt="Imagen aleatoria" class="cat-image">
        
        <!-- Search box -->
        <div class="search-box">
            <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
            <div class="gcse-search"></div>
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
        const randomText = images[randomKey];

        // Set the random image source and button text
        document.getElementById("randomImage").src = randomKey;
        document.querySelector(".gsc-search-button-v2:after").textContent = randomText;
    </script>
</body>
</html>
