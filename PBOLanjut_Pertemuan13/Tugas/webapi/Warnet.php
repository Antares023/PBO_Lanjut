<?php
require_once 'database.php';

class Warnet
{
    private $db;
    private $table ='sewa';
    public $idpc = "";
    public $user = "";
    public $tanggal = "";
    public $jam_mulai = "";
    public $jam_selesai = "";
    public $lama_waktu = "";
    public $tarif = "";
    public $total = "";
    public $status = "";

    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }

    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }

    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function get_by_idpc(int $idpc)
    {
        $query = "SELECT * FROM $this->table WHERE idpc = $idpc";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`idpc`, `user`, `tanggal`,`jam_mulai`,`jam_selesai`,`lama_waktu`,`tarif`,`total`,`status`) VALUES ('$this->idpc','$this->user','$this->tanggal','$this->jam_mulai','$this->jam_selesai','$this->lama_waktu','$this->tarif','$this->total','$this->status')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `idpc` = '$this->idpc', `user` = '$this->user', `tanggal` = '$this->tanggal', `jam_mulai` = '$this->jam_mulai', `jam_selesai` = '$this->jam_selesai', `lama_waktu` = '$this->lama_waktu', `tarif` = '$this->tarif', `total` = '$this->total', `status` = '$this->status' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_idpc($idpc): int
    {
        $query = "UPDATE $this->table SET `user` = '$this->user', `tanggal` = '$this->tanggal', `jam_mulai` = '$this->jam_mulai', `jam_selesai` = '$this->jam_selesai', `lama_waktu` = '$this->lama_waktu', `tarif` = '$this->tarif', `total` = '$this->total', `status` = '$this->status' WHERE idpc = $idpc";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_idpc($idpc): int
    {
        $query = "DELETE FROM $this->table WHERE idpc = $idpc";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>