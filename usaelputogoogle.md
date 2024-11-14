<!DOCTYPE html>
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
        
        .search-box {
            width: 100%;
            max-width: 600px;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #7e9db9;
            border-radius: 4px;
        }
        
        .search-button {
            padding: 10px 20px;
            background-color: #4285f4;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        .search-button:hover {
            background-color: #357abd;
        }
    </style>
</head>
<body>
    <div class="search-container">
        <img src="images/gato.jpg" alt="Gatito" class="cat-image">
        
        <div class="gcse-search-box">
            <script async src="https://cse.google.com/cse.js?cx=b735149c4c66c416c"></script>
            <div class="gcse-searchbox-only" data-resultsUrl="results.html">
                <form>
                    <input type="search" class="search-box">
                    <button type="submit" class="search-button">Salva al gatito</button>
                </form>
            </div>
        </div>
        
        <div class="gcse-searchresults"></div>
    </div>
</body>
</html>
