<?php
require_once 'database.php';
require_once 'Warnet.php';

$db = new MySQLDatabase();
$sewa = new Warnet($db);
$id=0;
$idpc=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['idpc'])){
            $idpc = $_GET['idpc'];
        }
        
        if($id>0){    
            $result = $sewa->get_by_id($id);
        }elseif($idpc>0){
            $result = $sewa->get_by_idpc($idpc);
        } else {
            $result = $sewa->get_all();
        }        
       
        $mhs = array();
        while ($row = $result->fetch_assoc()) {
            $mhs[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($mhs);
        break;

    case 'POST':
        // Add a new sewa
        $sewa->idpc = $_POST['idpc'];
        $sewa->user = $_POST['user'];
        $sewa->tanggal = $_POST['tanggal'];
        $sewa->jam_mulai = $_POST['jam_mulai'];
        $sewa->jam_selesai = $_POST['jam_selesai'];
        $sewa->lama_waktu = $_POST['lama_waktu'];
        $sewa->tarif = $_POST['tarif'];
        $sewa->total = $_POST['total'];
        $sewa->status = $_POST['status'];
        $sewa->insert();
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Employee data created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Employee data not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'PUT':
        // Update an existing sewa
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['idpc'])){
            $idpc = $_GET['idpc'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $sewa->idpc = $_PUT['idpc'];
        $sewa->user = $_PUT['user'];
        $sewa->tanggal = $_PUT['tanggal'];
        $sewa->jam_mulai = $_PUT['jam_mulai'];
        $sewa->jam_selesai = $_PUT['jam_selesai'];
        $sewa->lama_waktu = $_PUT['lama_waktu'];
        $sewa->tarif = $_PUT['tarif'];
        $sewa->total = $_PUT['total'];
        $sewa->status = $_PUT['status'];
        if($id>0){    
            $sewa->update($id);
        }elseif($idpc>0){
            $sewa->update_by_idpc($idpc);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Employee data updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Employee data update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['idpc'])){
            $idpc = $_GET['idpc'];
        }
        if($id>0){    
            $sewa->delete($id);
        }elseif($idpc>0){
            $sewa->delete_by_idpc($idpc);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Employee data deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Employee data delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
}
$db->close()
?>
