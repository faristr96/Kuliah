<?php

header("Content-Type: application/json; charset=UTF-8");

include "app/routes/mahasiswaRoutes.php";

use app\routes\MahasiswaRoutes;

// Tangkap Request method
$method = $_SERVER["REQUEST_METHOD"];
// Tangkap request path
$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);

// Panggil routes
$mahasiswaRoutes = new MahasiswaRoutes();
$mahasiswaRoutes->handle($method, $path);