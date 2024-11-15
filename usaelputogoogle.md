<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Random Image Search</title>
    <style>
        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .search-container {
            max-width: 800px;
            margin: 20px auto;
            text-align: center;
        }
        
        .image-wrapper {
            position: relative;
            display: inline-block;
            margin-bottom: 20px;
        }

        .cat-image {
            max-width: 300px;
            width: 100%;
            height: auto;
            display: block;
        }

        .search-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 10px;
        }

        /* Custom styles for Google CSE */
        .gsc-control-cse {
            padding: 0 !important;
            border: none !important;
            background: transparent !important;
        }

        .gsc-search-button-v2 {
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            max-width: 200px !important;
            min-height: 36px !important;
            height: 36px !important;
        }

        .gsc-search-button-v2 svg {
            display: none !important;
        }

        .gsc-search-button-v2::after {
            content: attr(data-custom-text);
            font-size: 14px;
            color: white;
            padding: 0 10px;
            display: block;
            line-height: 1;
        }

        footer {
            margin-top: auto;
            padding: 20px;
            background-color: #f8f9fa;
            text-align: center;
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 0 auto;
            max-width: 800px;
        }

        .image-button {
            padding: 10px 20px;
            font-size: 14px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            min-width: 120px;
            max-width: 200px;
        }

        .image-button:hover {
            background-color: #0056b3;
        }

        @media (max-width: 600px) {
            .button-container {
                flex-wrap: wrap;
            }
            
            .image-button {
                font-size: 12px;
                padding: 8px 16px;
            }
        }
    </style>
    <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
</head>
<body>
    <div class="search-container">
        <div class="image-wrapper">
            <img id="randomImage" src="images/gato.jpg" alt="Imagen aleatoria" class="cat-image">
            <div class="search-overlay">
                <div class="gcse-search" data-hl="es" data-gname="randomImageSearch"></div>
            </div>
        </div>
    </div>

    <footer>
        <div class="button-container">
            <button class="image-button" onclick="setImage('gato')">domokun</button>
            <button class="image-button" onclick="setImage('carlos')">carlos I</button>
            <button class="image-button" onclick="setImage('claudio')">claudio</button>
            <button class="image-button" onclick="setImage('marlo')">marlo</button>
        </div>
    </footer>

    <script>
        const images = {
            "claudio": { src: "images/claudio.jpg", text: "Fregquishimo", down_button_text: "claudio" },
            "marlo": { src: "images/marlo.jpg", text: "Dale al puto botón", down_button_text: "marlo" },
            "carlos": { src: "images/carlos.jpg", text: "Salva al imperio", down_button_text: "carlos I" },
            "gato": { src: "images/gato.jpg", text: "Salva al gatito", down_button_text: "domokun" }
        };

        let currentImageKey = null;

        function setImage(key) {
            const imageData = images[key];
            document.getElementById("randomImage").src = imageData.src;
            currentImageKey = key;
            updateSearchButtonText(imageData.text);
        }

        function updateSearchButtonText(text) {
            const searchButton = document.querySelector('.gsc-search-button-v2');
            if (searchButton) {
                searchButton.setAttribute('data-custom-text', text);
            }
        }

        window.onload = function() {
            const keys = Object.keys(images);
            const randomKey = keys[Math.floor(Math.random() * keys.length)];
            currentImageKey = randomKey;
            setImage(randomKey);

            const observer = new MutationObserver((mutations, obs) => {
                const searchButton = document.querySelector('.gsc-search-button-v2');
                if (searchButton) {
                    updateSearchButtonText(images[currentImageKey].text);
                    obs.disconnect();
                }
            });

            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        };
    </script>
</body>
</html>