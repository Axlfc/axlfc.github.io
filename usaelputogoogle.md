<html>
<head>
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

        /* Custom styling for the search button */
        .gsc-search-button-v2 {
            font-size: 0px !important;
        }

        .gsc-search-button-v2:after {
            content: 'Salva al gatito' !important;
            font-size: 14px !important;
            padding: 0 10px;
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
        <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
        <div class="gcse-search"></div>
    </div>
</body>
</html>
