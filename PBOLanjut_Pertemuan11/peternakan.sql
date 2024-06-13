-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2024 at 04:03 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nilai_mahasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `peternakan`
--

CREATE TABLE `peternakan` (
  `id` int(11) NOT NULL,
  `fakultas` varchar(25) NOT NULL,
  `prodi` varchar(25) NOT NULL,
  `semester` enum('Ganjil','Genap') NOT NULL DEFAULT 'Ganjil',
  `tahun_akademik` varchar(15) NOT NULL,
  `matakuliah` varchar(25) NOT NULL,
  `nim` varchar(15) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `kahadiran` decimal(10,2) NOT NULL,
  `uts` decimal(10,2) NOT NULL,
  `uas` decimal(10,2) NOT NULL,
  `sikap` decimal(10,2) NOT NULL,
  `tugas_harian` decimal(10,2) NOT NULL,
  `tugas_kelompok` decimal(10,2) NOT NULL,
  `tugas_besar` decimal(10,2) NOT NULL,
  `nilai_akhir` decimal(10,2) NOT NULL,
  `nilai_mutu` char(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `peternakan`
--

INSERT INTO `peternakan` (`id`, `fakultas`, `prodi`, `semester`, `tahun_akademik`, `matakuliah`, `nim`, `nama`, `kahadiran`, `uts`, `uas`, `sikap`, `tugas_harian`, `tugas_kelompok`, `tugas_besar`, `nilai_akhir`, `nilai_mutu`) VALUES
(1, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311001', 'NURWAHIDIN NUGRAHA', 85.00, 83.00, 82.00, 0.00, 76.00, 80.00, 0.00, 77.65, 'B'),
(2, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311002', 'HABIBI', 92.00, 89.00, 86.00, 0.00, 90.00, 91.00, 0.00, 84.35, 'B'),
(3, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311003', 'RISNAENI ADHARI', 85.00, 87.00, 90.00, 0.00, 95.00, 93.00, 0.00, 85.10, 'A'),
(4, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311004', 'MOHAMAD RIZKI HERDIANSYAH', 92.00, 86.00, 85.00, 0.00, 79.00, 86.00, 0.00, 81.55, 'B'),
(5, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311005', 'FAIZAL DARMAWAN', 92.00, 87.00, 91.00, 0.00, 89.00, 89.00, 0.00, 85.30, 'A'),
(6, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311006', 'DHARMAWAN YUDHA EKAPAMUJI', 85.00, 86.00, 87.00, 0.00, 84.00, 80.00, 0.00, 81.85, 'B'),
(7, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311011', 'NUR FAUZY LUKMAN', 85.00, 79.00, 87.00, 0.00, 78.00, 80.00, 0.00, 78.80, 'B'),
(8, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311015', 'ADE IMAN', 77.00, 80.00, 88.00, 0.00, 79.00, 89.00, 0.00, 80.35, 'B'),
(9, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311016', 'ASEF THRIANA NUGRAHA PUTRA', 92.00, 89.00, 91.00, 0.00, 89.00, 91.00, 0.00, 86.00, 'A'),
(10, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311017', 'ALI KALMANI', 100.00, 91.00, 0.00, 0.00, 86.00, 95.00, 0.00, 55.35, 'D'),
(11, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311018', 'FIRMAN ALFARIZI PUTRA', 85.00, 84.00, 93.00, 0.00, 86.00, 96.00, 0.00, 85.10, 'A'),
(12, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Bahan Pakan dan Formulasi', '210311019', 'MUHAMMAD FADLUN', 85.00, 88.00, 89.00, 0.00, 86.00, 91.00, 0.00, 83.75, 'B'),
(13, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311001', 'ZHANUBHA CINTA AURELLINE', 100.00, 80.00, 90.00, 96.00, 90.00, 0.00, 0.00, 91.10, 'A'),
(14, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311002', 'MUHAMAD ZIDAN KURNIAWAN', 93.00, 80.00, 65.00, 90.00, 86.00, 0.00, 0.00, 82.75, 'B'),
(15, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311003', 'LISANIA CAHYA AGUSTIN', 93.00, 73.00, 90.00, 93.00, 87.00, 0.00, 0.00, 86.90, 'A'),
(16, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311004', 'MILY RELANDA', 60.00, 70.00, 80.00, 85.00, 85.00, 0.00, 0.00, 74.75, 'B'),
(17, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311005', 'MAULANA AKBAR', 100.00, 90.00, 80.00, 96.00, 88.00, 0.00, 0.00, 90.60, 'A'),
(18, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311007', 'MUHAMMAD ARGI RAHMADI', 93.00, 75.00, 70.00, 90.00, 89.00, 0.00, 0.00, 83.50, 'B'),
(19, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311008', 'MOHAMAD DEKI KURNIAWAN', 71.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TL'),
(20, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311009', 'AEF SAEFUL FATAH', 93.00, 90.00, 80.00, 90.00, 87.00, 0.00, 0.00, 88.00, 'A'),
(21, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311010', 'KHOLIZA', 93.00, 75.00, 70.00, 90.00, 85.00, 0.00, 0.00, 82.50, 'B'),
(22, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311011', 'AN`IM RAJABIY', 80.00, 75.00, 65.00, 85.00, 88.00, 0.00, 0.00, 78.50, 'B'),
(23, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311012', 'ARYA WINATA', 100.00, 90.00, 75.00, 93.00, 87.00, 0.00, 0.00, 89.05, 'A'),
(24, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311013', 'DIMAS UJANG SUSILO', 100.00, 90.00, 85.00, 96.00, 90.00, 0.00, 0.00, 92.10, 'A'),
(25, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311014', 'M. GHULAM AL KHIDZIR', 100.00, 93.00, 90.00, 100.00, 90.00, 0.00, 0.00, 94.10, 'A'),
(26, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311015', 'RIFQI NIKI DWI FAUZI', 93.00, 73.00, 65.00, 90.00, 88.00, 0.00, 0.00, 81.85, 'B'),
(27, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311016', 'MUHAMAD ABDU ROHMAN', 80.00, 80.00, 75.00, 85.00, 88.00, 0.00, 0.00, 81.50, 'B'),
(28, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Biologi', '220311017', 'MUHAMAD FAIZA NURUL PADILLAH', 93.00, 75.00, 75.00, 93.00, 90.00, 0.00, 0.00, 85.05, 'A'),
(29, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311001', 'NURWAHIDIN NUGRAHA', 70.00, 88.00, 0.00, 0.00, 86.00, 0.00, 88.00, 87.22, 'A'),
(30, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311002', 'HABIBI', 60.00, 88.00, 0.00, 0.00, 86.00, 0.00, 87.00, 86.63, 'A'),
(31, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311003', 'RISNAENI ADHARI', 70.00, 87.00, 0.00, 0.00, 87.00, 0.00, 86.00, 86.34, 'A'),
(32, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311004', 'MOHAMAD RIZKI HERDIANSYAH', 70.00, 88.00, 0.00, 0.00, 86.00, 0.00, 87.00, 86.73, 'A'),
(33, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311005', 'FAIZAL DARMAWAN', 90.00, 88.00, 0.00, 0.00, 88.00, 0.00, 86.00, 87.04, 'A'),
(34, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311006', 'DHARMAWAN YUDHA EKAPAMUJI', 70.00, 87.00, 0.00, 0.00, 86.00, 0.00, 87.00, 86.83, 'A'),
(35, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311011', 'NUR FAUZY LUKMAN', 70.00, 88.00, 0.00, 0.00, 87.00, 0.00, 88.00, 87.52, 'A'),
(36, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311015', 'ADE IMAN', 40.00, 86.00, 0.00, 0.00, 86.00, 0.00, 87.00, 85.63, 'A'),
(37, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311016', 'ASEF THRIANA NUGRAHA PUTRA', 80.00, 87.00, 0.00, 0.00, 86.00, 0.00, 86.00, 86.14, 'A'),
(38, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311017', 'ALI KALMANI', 100.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 'E'),
(39, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311018', 'FIRMAN ALFARIZI PUTRA', 70.00, 86.00, 0.00, 0.00, 86.00, 0.00, 88.00, 86.82, 'A'),
(40, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Dasar-dasar Manajemen', '210311019', 'MUHAMMAD FADLUN', 70.00, 87.00, 0.00, 0.00, 87.00, 0.00, 88.00, 87.62, 'A'),
(41, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311001', 'NURWAHIDIN NUGRAHA', 47.00, 50.00, 60.00, 90.00, 90.00, 0.00, 0.00, 65.25, 'C'),
(42, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311002', 'HABIBI', 87.00, 90.00, 90.00, 96.00, 90.00, 0.00, 0.00, 89.85, 'A'),
(43, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311003', 'RISNAENI ADHARI', 67.00, 70.00, 80.00, 90.00, 90.00, 0.00, 0.00, 78.25, 'B'),
(44, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311004', 'MOHAMAD RIZKI HERDIANSYAH', 60.00, 60.00, 85.00, 90.00, 85.00, 0.00, 0.00, 74.25, 'B'),
(45, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311005', 'FAIZAL DARMAWAN', 87.00, 90.00, 90.00, 96.00, 88.00, 0.00, 0.00, 89.35, 'A'),
(46, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311006', 'DHARMAWAN YUDHA EKAPAMUJI', 87.00, 65.00, 90.00, 90.00, 85.00, 0.00, 0.00, 83.00, 'B'),
(47, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311011', 'NUR FAUZY LUKMAN', 47.00, 65.00, 75.00, 85.00, 80.00, 0.00, 0.00, 68.25, 'C'),
(48, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311015', 'ADE IMAN', 20.00, 65.00, 60.00, 85.00, 86.00, 0.00, 0.00, 60.00, 'C'),
(49, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311016', 'ASEF THRIANA NUGRAHA PUTRA', 87.00, 80.00, 85.00, 90.00, 88.00, 0.00, 0.00, 85.75, 'A'),
(50, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311017', 'ALI KALMANI', 71.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TL'),
(51, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311018', 'FIRMAN ALFARIZI PUTRA', 87.00, 80.00, 90.00, 96.00, 90.00, 0.00, 0.00, 87.85, 'A'),
(52, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Genetika', '210311019', 'MUHAMMAD FADLUN', 93.00, 65.00, 80.00, 90.00, 85.00, 0.00, 0.00, 82.50, 'B'),
(53, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311001', 'FAJAR AMIR', 40.00, 70.00, 70.00, 0.00, 0.00, 0.00, 70.00, 66.00, 'C'),
(54, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311002', 'RIFKY RAMDHANI', 50.00, 70.00, 80.00, 0.00, 0.00, 0.00, 80.00, 74.00, 'B'),
(55, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311003', 'NIZAM ARQOTH', 40.00, 70.00, 70.00, 0.00, 0.00, 0.00, 90.00, 69.00, 'C'),
(56, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311004', 'MUCHAMMAD RIDWAN', 40.00, 90.00, 85.00, 0.00, 0.00, 0.00, 90.00, 82.00, 'B'),
(57, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311006', 'DIMAS BIMANTORO', 50.00, 90.00, 90.00, 0.00, 0.00, 0.00, 90.00, 86.00, 'A'),
(58, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311007', 'SAPTO AKBAR NUGROHO', 50.00, 80.00, 80.00, 0.00, 0.00, 0.00, 80.00, 77.00, 'B'),
(59, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311008', 'ILHAM SHODIQ', 0.00, 70.00, 80.00, 0.00, 0.00, 0.00, 80.00, 69.00, 'C'),
(60, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311010', 'BUKHORI MAULANA', 80.00, 95.00, 95.00, 0.00, 0.00, 0.00, 95.00, 93.30, 'A'),
(61, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311011', 'M FAQIH', 30.00, 70.00, 70.00, 0.00, 0.00, 0.00, 70.00, 63.00, 'C'),
(62, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311012', 'SOFI NABILA', 70.00, 90.00, 95.00, 0.00, 0.00, 0.00, 95.00, 86.50, 'A'),
(63, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311013', 'NISAH NURCAHYANI', 70.00, 90.00, 95.00, 0.00, 0.00, 0.00, 90.00, 85.00, 'A'),
(64, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311014', 'SAMSUL MU\'ARIF', 60.00, 70.00, 80.00, 0.00, 0.00, 0.00, 80.00, 69.00, 'C'),
(65, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311016', 'ANGGI DWI ASTUTI', 60.00, 90.00, 95.00, 0.00, 0.00, 0.00, 95.00, 87.30, 'A'),
(66, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311020', 'ASRI DEWI NABILATUL JANNAH', 50.00, 95.00, 90.00, 0.00, 0.00, 0.00, 95.00, 87.30, 'A'),
(67, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '200311021', 'HERI ASSIDDIQ', 60.00, 80.00, 80.00, 0.00, 0.00, 0.00, 80.00, 72.00, 'B'),
(68, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Teknologi Daging dan', '211311001', 'ZYDANE WYLDAN RAHMAWAN', 60.00, 70.00, 80.00, 0.00, 0.00, 0.00, 80.00, 69.00, 'C'),
(69, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311001', 'FAJAR AMIR', 50.00, 80.00, 80.00, 0.00, 70.00, 0.00, 80.00, 78.00, 'B'),
(70, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311002', 'RIFKY RAMDHANI', 25.00, 85.00, 80.00, 0.00, 70.00, 0.00, 80.00, 79.50, 'B'),
(71, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311003', 'NIZAM ARQOTH', 100.00, 80.00, 80.00, 0.00, 70.00, 0.00, 80.00, 78.00, 'B'),
(72, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311004', 'MUCHAMMAD RIDWAN', 0.00, 80.00, 85.00, 0.00, 70.00, 0.00, 80.00, 79.50, 'B'),
(73, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311006', 'DIMAS BIMANTORO', 75.00, 90.00, 90.00, 0.00, 80.00, 0.00, 90.00, 88.00, 'A'),
(74, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311007', 'SAPTO AKBAR NUGROHO', 50.00, 80.00, 80.00, 0.00, 80.00, 0.00, 80.00, 80.00, 'B'),
(75, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311008', 'ILHAM SHODIQ', 75.00, 70.00, 80.00, 0.00, 80.00, 0.00, 80.00, 77.00, 'B'),
(76, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311010', 'BUKHORI MAULANA', 100.00, 95.00, 90.00, 0.00, 100.00, 0.00, 95.00, 94.50, 'A'),
(77, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311011', 'M FAQIH', 0.00, 80.00, 80.00, 0.00, 60.00, 0.00, 80.00, 76.00, 'B'),
(78, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311012', 'SOFI NABILA', 100.00, 95.00, 90.00, 0.00, 90.00, 0.00, 90.00, 91.50, 'A'),
(79, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311013', 'NISAH NURCAHYANI', 100.00, 90.00, 90.00, 0.00, 90.00, 0.00, 90.00, 90.00, 'A'),
(80, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311014', 'SAMSUL MU\'ARIF', 25.00, 75.00, 85.00, 0.00, 70.00, 0.00, 85.00, 79.00, 'B'),
(81, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311016', 'ANGGI DWI ASTUTI', 75.00, 90.00, 90.00, 0.00, 90.00, 0.00, 90.00, 90.00, 'A'),
(82, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311020', 'ASRI DEWI NABILATUL JANNAH', 100.00, 80.00, 90.00, 0.00, 100.00, 0.00, 90.00, 89.00, 'A'),
(83, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '200311021', 'HERI ASSIDDIQ', 75.00, 80.00, 80.00, 0.00, 80.00, 0.00, 80.00, 80.00, 'B'),
(84, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Ilmu Ternak Potong', '211311001', 'ZYDANE WYLDAN RAHMAWAN', 75.00, 80.00, 75.00, 0.00, 80.00, 0.00, 85.00, 79.50, 'B'),
(85, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311001', 'ZHANUBHA CINTA AURELLINE', 92.00, 80.00, 90.00, 0.00, 0.00, 0.00, 90.00, 87.20, 'A'),
(86, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311002', 'MUHAMAD ZIDAN KURNIAWAN', 83.00, 85.00, 85.00, 0.00, 0.00, 0.00, 90.00, 86.30, 'A'),
(87, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311003', 'LISANIA CAHYA AGUSTIN', 83.00, 85.00, 90.00, 0.00, 0.00, 0.00, 90.00, 87.80, 'A'),
(88, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311004', 'MILY RELANDA', 50.00, 75.00, 80.00, 0.00, 0.00, 0.00, 75.00, 74.00, 'B'),
(89, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311005', 'MAULANA AKBAR', 92.00, 90.00, 90.00, 0.00, 0.00, 0.00, 90.00, 90.20, 'A'),
(90, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311007', 'MUHAMMAD ARGI RAHMADI', 92.00, 90.00, 90.00, 0.00, 0.00, 0.00, 90.00, 90.20, 'A'),
(91, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311008', 'MOHAMAD DEKI KURNIAWAN', 17.00, 70.00, 70.00, 0.00, 0.00, 0.00, 70.00, 64.70, 'C'),
(92, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311009', 'AEF SAEFUL FATAH', 83.00, 85.00, 85.00, 0.00, 0.00, 0.00, 90.00, 86.30, 'A'),
(93, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311010', 'KHOLIZA', 92.00, 90.00, 85.00, 0.00, 0.00, 0.00, 90.00, 88.70, 'A'),
(94, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311011', 'AN`IM RAJABIY', 92.00, 90.00, 90.00, 0.00, 0.00, 0.00, 90.00, 90.20, 'A'),
(95, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311012', 'ARYA WINATA', 92.00, 90.00, 90.00, 0.00, 0.00, 0.00, 90.00, 90.20, 'A'),
(96, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311013', 'DIMAS UJANG SUSILO', 92.00, 85.00, 90.00, 0.00, 0.00, 0.00, 90.00, 88.70, 'A'),
(97, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311014', 'M. GHULAM AL KHIDZIR', 92.00, 85.00, 90.00, 0.00, 0.00, 0.00, 85.00, 87.20, 'A'),
(98, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311015', 'RIFQI NIKI DWI FAUZI', 83.00, 85.00, 90.00, 0.00, 0.00, 0.00, 85.00, 86.30, 'A'),
(99, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311016', 'MUHAMAD ABDU ROHMAN', 92.00, 90.00, 85.00, 0.00, 0.00, 0.00, 90.00, 88.70, 'A'),
(100, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Kimia', '220311017', 'MUHAMAD FAIZA NURUL PADILLAH', 92.00, 90.00, 85.00, 0.00, 0.00, 0.00, 90.00, 88.70, 'A'),
(101, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311001', 'NURWAHIDIN NUGRAHA', 87.00, 85.00, 79.00, 0.00, 80.00, 75.00, 0.00, 79.75, 'B'),
(102, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311002', 'HABIBI', 100.00, 84.00, 80.00, 0.00, 90.00, 90.00, 0.00, 87.80, 'A'),
(103, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311003', 'RISNAENI ADHARI', 80.00, 89.00, 90.00, 0.00, 96.00, 95.00, 0.00, 91.45, 'A'),
(104, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311004', 'MOHAMAD RIZKI HERDIANSYAH', 93.00, 79.00, 86.00, 0.00, 80.00, 78.00, 0.00, 81.60, 'B'),
(105, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311005', 'FAIZAL DARMAWAN', 93.00, 84.00, 89.00, 0.00, 86.00, 87.00, 0.00, 87.25, 'A'),
(106, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311006', 'DHARMAWAN YUDHA EKAPAMUJI', 93.00, 79.00, 85.00, 0.00, 76.00, 80.00, 0.00, 81.50, 'B'),
(107, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311011', 'NUR FAUZY LUKMAN', 87.00, 72.00, 87.00, 0.00, 74.00, 79.00, 0.00, 79.25, 'B'),
(108, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311015', 'ADE IMAN', 67.00, 83.00, 84.00, 0.00, 75.00, 76.00, 0.00, 78.25, 'B'),
(109, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311016', 'ASEF THRIANA NUGRAHA PUTRA', 100.00, 90.00, 90.00, 0.00, 95.00, 95.00, 0.00, 93.50, 'A'),
(110, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311017', 'ALI KALMANI', 86.00, 85.00, 0.00, 0.00, 86.00, 76.00, 0.00, 65.10, 'C'),
(111, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311018', 'FIRMAN ALFARIZI PUTRA', 100.00, 87.00, 85.00, 0.00, 79.00, 83.00, 0.00, 85.30, 'A'),
(112, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Landasan Ilmu Nutrisi', '210311019', 'MUHAMMAD FADLUN', 100.00, 78.00, 87.00, 0.00, 76.00, 79.00, 0.00, 82.05, 'B'),
(113, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311001', 'NURWAHIDIN NUGRAHA', 89.00, 83.00, 85.00, 0.00, 80.00, 80.00, 0.00, 82.50, 'B'),
(114, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311002', 'HABIBI', 100.00, 90.00, 86.00, 0.00, 83.00, 85.00, 0.00, 87.40, 'A'),
(115, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311003', 'RISNAENI ADHARI', 100.00, 92.00, 90.00, 0.00, 90.00, 90.00, 0.00, 91.40, 'A'),
(116, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311004', 'MOHAMAD RIZKI HERDIANSYAH', 89.00, 87.00, 85.00, 0.00, 83.00, 85.00, 0.00, 85.50, 'A'),
(117, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311005', 'FAIZAL DARMAWAN', 100.00, 85.00, 85.00, 0.00, 85.00, 85.00, 0.00, 86.50, 'A'),
(118, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311006', 'DHARMAWAN YUDHA EKAPAMUJI', 89.00, 88.00, 84.00, 0.00, 80.00, 85.00, 0.00, 85.05, 'A'),
(119, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311011', 'NUR FAUZY LUKMAN', 89.00, 75.00, 82.00, 0.00, 80.00, 82.00, 0.00, 81.00, 'B'),
(120, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311015', 'ADE IMAN', 78.00, 72.00, 76.00, 0.00, 80.00, 82.00, 0.00, 77.00, 'B'),
(121, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311016', 'ASEF THRIANA NUGRAHA PUTRA', 100.00, 85.00, 88.00, 0.00, 90.00, 89.00, 0.00, 89.25, 'A'),
(122, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311017', 'ALI KALMANI', 100.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 10.00, 'E'),
(123, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311018', 'FIRMAN ALFARIZI PUTRA', 89.00, 85.00, 84.00, 0.00, 80.00, 80.00, 0.00, 82.70, 'B'),
(124, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Manajemen Agribisnis', '210311019', 'MUHAMMAD FADLUN', 100.00, 72.00, 77.00, 0.00, 80.00, 80.00, 0.00, 79.80, 'B'),
(125, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311001', 'NURWAHIDIN NUGRAHA', 31.00, 70.00, 87.00, 0.00, 0.00, 100.00, 0.00, 69.42, 'C'),
(126, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311002', 'HABIBI', 92.00, 85.00, 65.00, 0.00, 100.00, 100.00, 0.00, 89.20, 'A'),
(127, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311003', 'RISNAENI ADHARI', 85.00, 88.00, 73.00, 0.00, 100.00, 100.00, 0.00, 90.50, 'A'),
(128, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311004', 'MOHAMAD RIZKI HERDIANSYAH', 62.00, 60.00, 60.00, 0.00, 100.00, 100.00, 0.00, 80.20, 'B'),
(129, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311005', 'FAIZAL DARMAWAN', 85.00, 75.00, 64.00, 0.00, 100.00, 100.00, 0.00, 86.20, 'A'),
(130, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311006', 'DHARMAWAN YUDHA EKAPAMUJI', 69.00, 70.00, 70.00, 0.00, 0.00, 100.00, 0.00, 69.70, 'C'),
(131, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311011', 'NUR FAUZY LUKMAN', 23.00, 60.00, 63.00, 0.00, 100.00, 100.00, 0.00, 76.80, 'B'),
(132, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311015', 'ADE IMAN', 54.00, 73.00, 76.00, 0.00, 0.00, 100.00, 0.00, 73.30, 'B'),
(133, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311016', 'ASEF THRIANA NUGRAHA PUTRA', 92.00, 83.00, 70.00, 0.00, 100.00, 100.00, 0.00, 89.70, 'A'),
(134, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311017', 'ALI KALMANI', 100.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'TL'),
(135, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311018', 'FIRMAN ALFARIZI PUTRA', 92.00, 63.00, 63.00, 0.00, 100.00, 100.00, 0.00, 84.20, 'B'),
(136, 'Fakultas Teknik', 'Peternakan', 'Ganjil', '2022/2023', 'Reproduksi Ternak dan IB', '210311019', 'MUHAMMAD FADLUN', 69.00, 60.00, 71.00, 0.00, 60.00, 100.00, 0.00, 77.10, 'B');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `peternakan`
--
ALTER TABLE `peternakan`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
