<?php 
namespace app\routes;

include "app/controller/controller_mahasiswa.php";
// mahasiswaRoutes.php


use app\controller\Controller_mahasiswa;

class MahasiswaRoutes{
    public function handle($method, $path){
        if ($method === "GET" && $path === "/api/mahasiswa") {
            $controller = new Controller_mahasiswa();
            echo $controller->indexMahasiswa();
        }

        if ($method === "GET" && $path === "/api/matkul") {
            $controller = new Controller_mahasiswa();
            echo $controller->indexMatkul();
        }

        if ($method === "GET" && strpos($path, "/api/mahasiswa/") === 0) {
            // Extract id dari path
            $pathParts = explode("/", $path);
            $id = $pathParts[count($pathParts) - 1];

            $controller = new Controller_mahasiswa();
            echo $controller->getMhsById($id);
        }

        if ($method === "POST" && $path === "/api/mahasiswa") {
            $controller = new Controller_mahasiswa();
            echo $controller->createMahasiswa();
        }

        // Jika request method put dan path mengandung "/api/product/
        if ($method === "PUT" && strpos($path, "/api/mahasiswa/") === 0) {
            // Extract id dari path
            $pathParts = explode('/', $path);
            $id = $pathParts[count($pathParts) - 1];

            $controller = new Controller_mahasiswa;
            echo $controller->updateMahasiswa($id);
        }

        if ($method === "DELETE" && strpos($path, "/api/mahasiswa/") === 0) {
            // Extract id dari path
            $pathParts = explode("/", $path);
            $id = $pathParts[count($pathParts) - 1];

            $controller = new Controller_mahasiswa;
            echo $controller->deleteMahasiswa($id);
        }
        
        if ($method === "GET" && $path === "/api/mahasiswa/full") {
            $controller = new Controller_mahasiswa();
            echo $controller->joinMahasiswa();
        }
        
    }
}
?>