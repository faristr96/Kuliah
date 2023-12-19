<?php

namespace app\traits;

// Untuk formatting response
trait ApiResponse 
{
    public function apiResponse($code = 200, $message = "success", $data = []) 
    {
        // Dari parameter akan di format menjadi seperti dibawah ini
        return json_encode([
            "code" => $code,
            "message" => $message,
            "data" => $data
        ]);
    }
}