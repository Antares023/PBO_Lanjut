<?php
require_once 'database.php';
require_once 'Mahasiswa.php';

$db = new MySQLDatabase();
$mahasiswa = new Mahasiswa($db);
$id=0;
$nim=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        
        if($id>0){    
            $result = $mahasiswa->get_by_id($id);
        }elseif($nim>0){
            $result = $mahasiswa->get_by_nim($nim);
        } else {
            $result = $mahasiswa->get_all();
        }        
       
        $mhs = array();
        while ($row = $result->fetch_assoc()) {
            $mhs[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($mhs);
        break;

    case 'POST':
        // Add a new mahasiswa
        $mahasiswa->nim = $_POST['nim'];
        $mahasiswa->nama = $_POST['nama'];
        $mahasiswa->jk = $_POST['jk'];
        $mahasiswa->prodi = $_POST['prodi'];
        $mahasiswa->insert();
        
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
        // Update an existing mahasiswa
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $mahasiswa->nim = $_PUT['nim'];
        $mahasiswa->nama = $_PUT['nama'];
        $mahasiswa->jk = $_PUT['jk'];
        $mahasiswa->prodi = $_PUT['prodi'];
        if($id>0){    
            $mahasiswa->update($id);
        }elseif($nim>0){
            $mahasiswa->update_by_nim($nim);
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
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        if($id>0){    
            $mahasiswa->delete($id);
        }elseif($nim>0){
            $mahasiswa->delete_by_nim($nim);
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
