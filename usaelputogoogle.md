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
        <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
        <div class="gcse-search"></div>
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

        // Set the random image source
        document.getElementById("randomImage").src = randomKey;
    </script>
</body>
</html>
