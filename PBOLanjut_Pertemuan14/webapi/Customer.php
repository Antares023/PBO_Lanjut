<?php
require_once 'database.php';

class Customer
{
    private $db;
    private $table = 'customer';
    public $ktp = "";
    public $nama = "";
    public $jk = "";
    public $kota = "";

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

    public function get_by_ktp(int $ktp)
    {
        $query = "SELECT * FROM $this->table WHERE ktp = $ktp";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`ktp`, `nama`, `jk`, `kota`) VALUES ('$this->ktp', '$this->nama', '$this->jk', '$this->kota')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `ktp` = '$this->ktp', `nama` = '$this->nama', `jk` = '$this->jk', `kota` = '$this->kota' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_ktp($ktp): int
    {
        $query = "UPDATE $this->table SET `nama` = '$this->nama', `jk` = '$this->jk', `kota` = '$this->kota' WHERE ktp = $ktp";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_ktp($ktp): int
    {
        $query = "DELETE FROM $this->table WHERE ktp = $ktp";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>