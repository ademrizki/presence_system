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
-- Database: `presensi`
--

-- --------------------------------------------------------

--
-- Table structure for table `facebase`
--

CREATE TABLE `facebase` (
  `no` int(11) NOT NULL,
  `npm` varchar(8) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `kelas` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facebase`
--

INSERT INTO `facebase` (`no`, `npm`, `nama`, `kelas`) VALUES
(10, '50415094', 'Ade Muhammad', '4IA06'),
(11, '57415251', 'Yogi Ermanto', '4IA16'),
(12, '57415485', 'Farel', '4IA14');

-- --------------------------------------------------------

--
-- Table structure for table `passkey`
--

CREATE TABLE `passkey` (
  `no` int(11) NOT NULL,
  `pkey` int(6) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `npm` varchar(8) NOT NULL,
  `kelas` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `passkey`
--

INSERT INTO `passkey` (`no`, `pkey`, `nama`, `npm`, `kelas`) VALUES
(10, 111111, 'Ade Muhammad', '50415094', '4IA06'),
(11, 592351, 'Yogi Ermanto', '57415251', '4IA16'),
(12, 222222, 'Farel', '57415485', '4IA14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `facebase`
--
ALTER TABLE `facebase`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `passkey`
--
ALTER TABLE `passkey`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `facebase`
--
ALTER TABLE `facebase`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `passkey`
--
ALTER TABLE `passkey`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
