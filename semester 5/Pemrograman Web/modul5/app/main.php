<?php

header("Content-Type: application/json; charset=UTF-8");

include "app/routes/"

use App\Routes\ProductRoutes;

// Tangkap Request method
$method = $_SERVER["REQUEST_METHOD"];
// Tangkap request path
$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);

// Panggil routes
$productRoute = new ProductRoutes();
$productRoute->handle($method, $path);