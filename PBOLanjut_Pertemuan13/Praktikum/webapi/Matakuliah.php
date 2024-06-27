<?php
require_once 'database.php';

class Matakuliah
{
    private $db;
    private $table = 'matakuliah';
    public $kodemk = "";
    public $namamk = "";
    public $sks = "";

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

    public function get_by_kodemk(int $kodemk)
    {
        $query = "SELECT * FROM $this->table WHERE kodemk = $kodemk";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodemk`, `namamk`, `sks`) VALUES ('$this->kodemk', '$this->namamk', '$this->sks')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `kodemk` = '$this->kodemk', `namamk` = '$this->namamk', `sks` = '$this->sks' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_kodemk($kodemk): int
    {
        $query = "UPDATE $this->table SET `namamk` = '$this->namamk', `sks` = '$this->sks' WHERE kodemk = $kodemk";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_kodemk($kodemk): int
    {
        $query = "DELETE FROM $this->table WHERE kodemk = $kodemk";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>