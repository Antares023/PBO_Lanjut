<?php
require_once 'database.php';

class Barang
{
    private $db;
    private $table = 'barang';
    public $kode = "";
    public $nama_barang = "";
    public $harga = "";

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

    public function get_by_kode(int $kode)
    {
        $query = "SELECT * FROM $this->table WHERE kode = $kode";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode`, `nama_barang`, `harga`) VALUES ('$this->kode', '$this->nama_barang', '$this->harga')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `kode` = '$this->kode', `nama_barang` = '$this->nama_barang', `harga` = '$this->harga' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_kode($kode): int
    {
        $query = "UPDATE $this->table SET `nama_barang` = '$this->nama_barang', `harga` = '$this->harga' WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_kode($kode): int
    {
        $query = "DELETE FROM $this->table WHERE kode = $kode";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>