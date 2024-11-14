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
            bottom: 0px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
        }

        /* Customize the search input box */
        .gcse-search input.gsc-input {
            height: 30px;
            width: calc(100% - 100px);
            font-size: 16px;
        }

        /* Custom styling for the search button */
        .gsc-search-button-v2 {
            width: 100px;
            font-size: 0 !important;
        }

        .gsc-search-button-v2:after {
            content: 'Salva al gatito' !important;
            font-size: 11px;
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
        <img src="images/gato.jpg" alt="Gatito" class="cat-image">
        
        <!-- Search box -->
        <div class="search-box">
            <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
            <div class="gcse-search"></div>
        </div>
    </div>
</body>
</html>
