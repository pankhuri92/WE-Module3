-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2024 at 02:38 PM
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
-- Database: `pokemon`
--

-- --------------------------------------------------------

--
-- Table structure for table `pokemonmoves`
--

CREATE TABLE `pokemonmoves` (
  `pokemon_id` int(11) NOT NULL,
  `move_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pokemonmoves`
--

INSERT INTO `pokemonmoves` (`pokemon_id`, `move_id`) VALUES
(1, 1),
(1, 4),
(1, 7),
(2, 1),
(2, 3),
(2, 7),
(3, 1),
(3, 2),
(3, 7),
(4, 1),
(4, 6),
(4, 7),
(5, 1),
(5, 5),
(5, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pokemonmoves`
--
ALTER TABLE `pokemonmoves`
  ADD PRIMARY KEY (`pokemon_id`,`move_id`),
  ADD KEY `move_id` (`move_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pokemonmoves`
--
ALTER TABLE `pokemonmoves`
  ADD CONSTRAINT `pokemonmoves_ibfk_1` FOREIGN KEY (`pokemon_id`) REFERENCES `pokemons` (`id`),
  ADD CONSTRAINT `pokemonmoves_ibfk_2` FOREIGN KEY (`move_id`) REFERENCES `moves` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
