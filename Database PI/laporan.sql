-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2019 at 12:15 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `laporan`
--

-- --------------------------------------------------------

--
-- Table structure for table `t_50415094`
--

CREATE TABLE `t_50415094` (
  `nomor` int(11) NOT NULL,
  `nama` varchar(30) DEFAULT 'Ade Muhammad',
  `kelas` varchar(8) DEFAULT '4IA06',
  `tanggal` date NOT NULL,
  `hari` varchar(10) DEFAULT NULL,
  `jamMasuk` time NOT NULL,
  `jamKeluar` time DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_50415094`
--

INSERT INTO `t_50415094` (`nomor`, `nama`, `kelas`, `tanggal`, `hari`, `jamMasuk`, `jamKeluar`, `keterangan`) VALUES
(1, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '08:51:05', '08:51:27', 'Test Absen'),
(2, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '08:55:10', '08:55:30', 'YES'),
(3, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '08:55:48', '08:56:16', 'YES2'),
(4, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '09:01:20', NULL, NULL),
(5, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '09:29:16', '09:30:22', 'Salah wajah'),
(6, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '09:33:35', NULL, NULL),
(7, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '09:36:32', NULL, NULL),
(8, 'Ade Muhammad', '4IA06', '2019-02-27', 'Rabu', '09:40:36', '09:41:02', 'yes ');

-- --------------------------------------------------------

--
-- Table structure for table `t_57415251`
--

CREATE TABLE `t_57415251` (
  `nomor` int(11) NOT NULL,
  `nama` varchar(30) DEFAULT 'Yogi Ermanto',
  `kelas` varchar(8) DEFAULT '4IA16',
  `tanggal` date NOT NULL,
  `hari` varchar(10) DEFAULT NULL,
  `jamMasuk` time NOT NULL,
  `jamKeluar` time DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `t_57415485`
--

CREATE TABLE `t_57415485` (
  `nomor` int(11) NOT NULL,
  `nama` varchar(30) DEFAULT 'Farel',
  `kelas` varchar(8) DEFAULT '4IA14',
  `tanggal` date NOT NULL,
  `hari` varchar(10) DEFAULT NULL,
  `jamMasuk` time NOT NULL,
  `jamKeluar` time DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `t_50415094`
--
ALTER TABLE `t_50415094`
  ADD PRIMARY KEY (`nomor`);

--
-- Indexes for table `t_57415251`
--
ALTER TABLE `t_57415251`
  ADD PRIMARY KEY (`nomor`);

--
-- Indexes for table `t_57415485`
--
ALTER TABLE `t_57415485`
  ADD PRIMARY KEY (`nomor`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `t_50415094`
--
ALTER TABLE `t_50415094`
  MODIFY `nomor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `t_57415251`
--
ALTER TABLE `t_57415251`
  MODIFY `nomor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `t_57415485`
--
ALTER TABLE `t_57415485`
  MODIFY `nomor` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
