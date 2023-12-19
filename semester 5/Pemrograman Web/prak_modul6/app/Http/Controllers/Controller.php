<?php

namespace app\controller;

include "app/traits/apiFormat.php";
include "app/models/mahasiswa.php";

use app\models\Mahasiswa;
use app\traits\ApiResponse;

class Controller_mahasiswa{
    use ApiResponse;

    public function indexMahasiswa(){
        $mahasiswa = new Mahasiswa;
        $response = $mahasiswa->getMahasiswa();
        return $this->apiResponse(200, "success", $response);
    }
    public function indexMatkul(){
        $mahasiswa = new Mahasiswa;
        $response = $mahasiswa->getMatkul();
        return $this->apiResponse(200, "success", $response);
    }

    public function getMhsById($id){
        $mahasiswa = new Mahasiswa();
        $response = $mahasiswa->getMahasiswaById($id);
        return $this->apiResponse(200, "success", $response);
    }
    
    public function createMahasiswa() {
        // Tangkap input JSON
        $jsonInput = file_get_contents('php://input');
        $inputData = json_decode($jsonInput, true);
    
        // Validasi apakah input valid
        if (json_last_error()) {
            return $this->apiResponse(400, "error invalid input", null);
        }
    
        // Tangkap data dari input
        $nama = $inputData["nama"] ?? null;
        $jurusan = $inputData["jurusan"] ?? null;
        $id_matkul = $inputData["id_matkul"] ?? null;
    
        if (!$nama || !$jurusan || !$id_matkul) {
            return $this->apiResponse(400, "error missing data", null);
        }
    
        $mahasiswa = new Mahasiswa();
        $response = $mahasiswa->createMhs([
            "nama" => $nama,
            "jurusan" => $jurusan,
            "id_matkul" => $id_matkul,
        ]);
    
        return $this->apiResponse(200, "success", $response);
    }
    
    public function updateMahasiswa($id) {
        // Tangkap input JSON
        $jsonInput = file_get_contents('php://input');
        $inputData = json_decode($jsonInput, true);
    
        // Validasi apakah input valid
        if (json_last_error()) {
            return $this->apiResponse(400, "error invalid input", null);
        }
    
        $mahasiswa = new Mahasiswa;
        $response = $mahasiswa->updateMhs($inputData, $id);
    
        return $this->apiResponse(200, "success", $response);
    }

    public function deleteMahasiswa($id) {
        $mahasiswa = new Mahasiswa;
        $response = $mahasiswa->deleteMhs($id);
    
        return $this->apiResponse(200, "success", $response);
    }
    public function joinMahasiswa() {
        $mahasiswa = new Mahasiswa;
        $response = $mahasiswa->joinMhs();
    
        return $this->apiResponse(200, "success", $response);
    }
    
    

}