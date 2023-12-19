<?php 
namespace app\models;
include "app/Config/database_config.php";
use app\config\DatabaseConfig;
use mysqli;

class Mahasiswa extends DatabaseConfig {   
    
    public $conn;

    public function __construct() {
        // Connect ke database mysql
        $this->conn = new mysqli($this->host, $this->user, $this->password, $this->database_name, $this->port);
        // Check connection
        if ($this->conn->connect_error) {
            die("Connection failed: " . $this->conn->connect_error);
        }
    }
    public function getMahasiswa() {
        $sql = "SELECT * FROM mahasiswa";
        $result = $this->conn->query($sql);
        $this ->conn->close();
        $data =[];
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }
        return $data;
    }
    public function getMatkul() {
        $sql = "SELECT * FROM mata_kuliah";
        $result = $this->conn->query($sql);
        $this ->conn->close();
        $data =[];
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }
        return $data;
    }
    public function getMahasiswaById($id) {
        $sql = "SELECT * FROM mahasiswa WHERE id = ?";
        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        $this->conn->close();
        $data = [];
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }
        return $data;
    }
    public function getMatkulById($id) {
        $sql = "SELECT * FROM mata_kuliah WHERE id = ?";
        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        $this->conn->close();
        $data = [];
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }
        return $data;
    }

    public function createMhs($data) {
        $nama = $data["nama"];
        $jurusan = $data["jurusan"];
        $id_matkul = $data["id_matkul"];
        $query = "INSERT INTO mahasiswa (nama, jurusan, id_matkul) VALUES (?, ?, ?)";
        $stmt = $this->conn->prepare($query);
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("ssi", $nama, $jurusan, $id_matkul);
        $stmt->execute();
        $this->conn->close();
    }

    public function updateMhs($data, $id) {
        $nama = $data["nama"] ?? null;
        $jurusan = $data["jurusan"] ?? null;
        $id_matkul = $data["id_matkul"] ?? null;
        $query = "UPDATE mahasiswa SET nama=?, jurusan=?, id_matkul=? WHERE id=?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("sssi", $nama, $jurusan, $id_matkul, $id);
        $stmt->execute();
        $stmt->close();
        $this->conn->close();
    
        return "Mahasiswa berhasil diupdate";
    }
    
    public function deleteMhs($id) {
        $query = "DELETE FROM mahasiswa WHERE id=?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $stmt->close();
        $this->conn->close();
    
        return "Mahasiswa berhasil dihapus";
    }
    public function joinMhs() {
        // Kueri SQL untuk LEFT JOIN antara mahasiswa dan mata_kuliah
        $query = "SELECT mahasiswa.*, mata_kuliah.nama_matkul 
                  FROM mahasiswa 
                  LEFT JOIN mata_kuliah ON mahasiswa.id_matkul = mata_kuliah.id";
        $result = $this->conn->query($query);
        $data = [];
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }
        $result->close();
        $this->conn->close();
    
        return $data;
    }
    
    
    
}
?>