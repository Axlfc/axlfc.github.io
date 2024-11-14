<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Salva al gatito</title>
    <style>
        .search-container {
            width: 800px;
            margin: 0 auto;
            position: relative;
            text-align: center;
        }
        
        .cat-image {
            width: 100%;
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
            width: calc(100% - 100px);
            font-size: 16px;
            padding: 0 10px;
        }

        /* Custom styling for the search button */
        .gsc-search-button-v2 {
            width: 100px;
            font-size: 0 !important;
        }

        .gsc-search-button-v2:after {
            content: 'Salva al gatito' !important;
            font-size: 14px;
            padding: 0 10px;
            display: inline-block;
        }

        /* Optional: Hide the search icon */
        .gsc-search-button-v2 svg {
            display: none !important;
        }
    </style>
</head>
<body>
    <div class="search-container">
        <script>
            // Array of image sources
            const imageSources = [
                "images/claudio.jpg",
                "images/gato.jpg",
                "images/carlos.jpg",
                "images/marlo.jpg"
            ];

            // Get a random index from the array
            const randomIndex = Math.floor(Math.random() * imageSources.length);

            // Get the corresponding image source
            const randomImageSource = imageSources[randomIndex];

            // Set the src attribute of the image element
            const imageElement = document.querySelector(".cat-image");
            imageElement.src = randomImageSource;
        </script>
        
        <img src="/api/placeholder/800/400" alt="Gatito" class="cat-image">
        
        <!-- Search box -->
        <div class="search-box">
            <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
            <div class="gcse-search"></div>
        </div>
    </div>
</body>
</html>
