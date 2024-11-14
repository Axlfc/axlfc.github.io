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
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            max-width: 600px;
            background-color: white;
            padding: 10px;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        /* Customize the search input box */
        .gcse-search input.gsc-input {
            height: 30px;
            width: calc(100% - 100px);
            font-size: 16px;
            border: 1px solid #7e9db9;
            padding: 5px 10px;
        }

        /* Custom styling for the search button */
        .gsc-search-button-v2 {
            width: 100px;
            font-size: 0 !important;
            background-color: #4285f4 !important;
            border-color: #4285f4 !important;
            padding: 7px 15px !important;
        }

        .gsc-search-button-v2:after {
            content: 'Salva al gatito' !important;
            font-size: 11px;
            display: inline-block;
            color: white;
        }

        /* Optional: Hide the search icon */
        .gsc-search-button-v2 svg {
            display: none !important;
        }

        /* Center the search results */
        .gcse-searchresults-only {
            margin-top: 50px;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="search-container">
        <img src="images/gato.jpg" alt="Gatito" class="cat-image">
        <div class="search-box">
            <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
            <div class="gcse-search"></div>
        </div>
    </div>
</body>
</html>
