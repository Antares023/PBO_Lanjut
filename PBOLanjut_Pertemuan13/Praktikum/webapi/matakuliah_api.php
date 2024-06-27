<?php
require_once 'database.php';
require_once 'Matakuliah.php';

$db = new MySQLDatabase();
$matakuliah = new Matakuliah($db);
$id=0;
$kodemk=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodemk'])){
            $kodemk = $_GET['kodemk'];
        }
        
        if($id>0){    
            $result = $matakuliah->get_by_id($id);
        }elseif($kodemk>0){
            $result = $matakuliah->get_by_kodemk($kodemk);
        } else {
            $result = $matakuliah->get_all();
        }        
       
        $mhs = array();
        while ($row = $result->fetch_assoc()) {
            $mhs[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($mhs);
        break;

    case 'POST':
        // Add a new matakuliah
        $matakuliah->kodemk = $_POST['kodemk'];
        $matakuliah->namamk = $_POST['namamk'];
        $matakuliah->sks = $_POST['sks'];
        $matakuliah->insert();
        
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
        // Update an existing matakuliah
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodemk'])){
            $kodemk = $_GET['kodemk'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $matakuliah->kodemk = $_PUT['kodemk'];
        $matakuliah->namamk = $_PUT['namamk'];
        $matakuliah->sks = $_PUT['sks'];
        if($id>0){    
            $matakuliah->update($id);
        }elseif($kodemk>0){
            $matakuliah->update_by_kodemk($kodemk);
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
        if(isset($_GET['kodemk'])){
            $kodemk = $_GET['kodemk'];
        }
        if($id>0){    
            $matakuliah->delete($id);
        }elseif($kodemk>0){
            $matakuliah->delete_by_kodemk($kodemk);
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
