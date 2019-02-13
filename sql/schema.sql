SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";
--
-- Base de datos: `bothorarios`
--
CREATE DATABASE IF NOT EXISTS `bothorarios` DEFAULT CHARACTER SET latin2 COLLATE latin2_general_ci;
USE `bothorarios`;

-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `asignaturas`
--
CREATE TABLE `asignaturas` (
  `ClaveA` varchar(50) NOT NULL,
  `NombreA` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin2;
--
-- Volcado de datos para la tabla `asignaturas`
--
INSERT INTO `asignaturas` (`ClaveA`, `NombreA`) VALUES
('A-01', 'Calidad en el desarrollo de software'),
('A-02', 'Desarrollo de aplicaciones III'),
('A-03', 'Integradora II'),
('A-04', 'Expresion oral y escrita II'),
('A-05', 'Idioma V'),
('A-06', 'Tutoria'),
('A-07', 'Ingeniera de software II'),
('A-08', 'Administracion de proyectos de TI');
-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `asignatura_grupo`
--
CREATE TABLE `asignatura_grupo` (
  `ClaveAG` varchar(50) NOT NULL,
  `ClaveAP` varchar(50) NOT NULL,
  `ClaveG` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin2;
--
-- Volcado de datos para la tabla `asignatura_grupo`
--
INSERT INTO `asignatura_grupo` (`ClaveAG`, `ClaveAP`, `ClaveG`) VALUES
('AG-01', 'AP-01', 'TIC52'),
('AG-02', 'AP-02', 'TIC52'),
('AG-03', 'AP-03', 'TIC52'),
('AG-04', 'AP-04', 'TIC52'),
('AG-05', 'AP-05', 'TIC52'),
('AG-06', 'AP-06', 'TIC52'),
('AG-07', 'AP-07', 'TIC52'),
('AG-08', 'AP-08', 'TIC52');
-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `asignatura_profesor`
--
CREATE TABLE `asignatura_profesor` (
  `ClaveAP` varchar(50) NOT NULL,
  `ClaveA` varchar(50) NOT NULL,
  `ClaveP` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin2;
--
-- Volcado de datos para la tabla `asignatura_profesor`
--
INSERT INTO `asignatura_profesor` (`ClaveAP`, `ClaveA`, `ClaveP`) VALUES
('AP-01', 'A-01', 'P-01'),
('AP-02', 'A-02', 'P-02'),
('AP-03', 'A-03', 'P-07'),
('AP-04', 'A-04', 'P-03'),
('AP-05', 'A-05', 'P-06'),
('AP-06', 'A-06', 'P-02'),
('AP-07', 'A-07', 'P-04'),
('AP-08', 'A-08', 'P-05');
-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `grupos`
--
CREATE TABLE `grupos` (
  `ClaveG` varchar(50) NOT NULL,
  `GradoG` varchar(50) NOT NULL,
  `GrupoG` varchar(50) NOT NULL,
  `CarreraG` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin2;
--
-- Volcado de datos para la tabla `grupos`
--
INSERT INTO `grupos` (`ClaveG`, `GradoG`, `GrupoG`, `CarreraG`) VALUES
('TIC52', '5to', '2', 'Tecnologias de la informacion y comunicacion');
-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `horario`
--
CREATE TABLE `horario` (
  `ClaveH` varchar(50) NOT NULL,
  `ClaveAG` varchar(50) NOT NULL,
  `DiaH` varchar(50) NOT NULL,
  `HoraEntradaH` time NOT NULL,
  `HoraSalidaH` time NOT NULL,
  `Salon` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin2;
--
-- Volcado de datos para la tabla `horario`
--
INSERT INTO `horario` (`ClaveH`, `ClaveAG`, `DiaH`, `HoraEntradaH`, `HoraSalidaH`, `Salon`) VALUES
('AGD-01', 'AG-01', 'Lunes', '07:00:00', '09:00:00', 'G2'),
('AGD-02', 'AG-01', 'Martes', '13:00:00', '15:00:00', 'G2'),
('AGD-03', 'AG-01', 'Jueves', '12:00:00', '14:00:00', 'G2'),
('AGD-04', 'AG-02', 'Lunes', '09:00:00', '11:00:00', 'LAB1'),
('AGD-05', 'AG-02', 'Miercoles', '07:00:00', '09:00:00', 'MAC'),
('AGD-06', 'AG-02', 'Jueves', '07:00:00', '09:00:00', 'MAC'),
('AGD-07', 'AG-02', 'Viernes', '12:00:00', '13:00:00', 'LAB4'),
('AGD-08', 'AG-03', 'Lunes', '11:00:00', '12:00:00', 'G2'),
('AGD-09', 'AG-03', 'Jueves', '11:00:00', '12:00:00', 'MAC'),
('AGD-10', 'AG-04', 'Lunes', '12:00:00', '14:00:00', 'G2'),
('AGD-11', 'AG-04', 'Miercoles', '12:00:00', '14:00:00', 'G2'),
('AGD-12', 'AG-04', 'Viernes', '13:00:00', '14:00:00', 'G2'),
('AGD-13', 'AG-05', 'Martes', '07:00:00', '09:00:00', ''),
('AGD-14', 'AG-05', 'Viernes', '07:00:00', '09:00:00', ''),
('AGD-15', 'AG-06', 'Martes', '09:00:00', '10:00:00', 'G2'),
('AGD-16', 'AG-07', 'Martes', '10:00:00', '13:00:00', 'LAB1'),
('AGD-17', 'AG-07', 'Miercoles', '11:00:00', '12:00:00', 'LAB2'),
('AGD-18', 'AG-07', 'Jueves', '09:00:00', '11:00:00', 'MAC'),
('AGD-19', 'AG-08', 'Miercoles', '09:00:00', '11:00:00', 'G2'),
('AGD-20', 'AG-08', 'Viernes', '09:00:00', '12:00:00', 'G2');
-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `profesores`
--
CREATE TABLE `profesores` (
  `ClaveP` varchar(50) NOT NULL,
  `NombreP` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin2;
--
-- Volcado de datos para la tabla `profesores`
--
INSERT INTO `profesores` (`ClaveP`, `NombreP`) VALUES
('P-01', 'Oscar Lira Uribe'),
('P-02', 'Salvador Hernandez Mendoza'),
('P-03', 'Maria del Rocio'),
('P-04', 'Victor Hernandez'),
('P-05', 'Nezter'),
('P-06', 'Academia de idiomas'),
('P-07', 'Elizabeth Garcia Urbina');
--
-- Índices para tablas volcadas
--
--
-- Indices de la tabla `asignaturas`
--
ALTER TABLE `asignaturas`
  ADD PRIMARY KEY (`ClaveA`);
--
-- Indices de la tabla `asignatura_grupo`
--
ALTER TABLE `asignatura_grupo`
  ADD PRIMARY KEY (`ClaveAG`),
  ADD KEY `AG_AP` (`ClaveAP`),
  ADD KEY `AG_G` (`ClaveG`);
--
-- Indices de la tabla `asignatura_profesor`
--
ALTER TABLE `asignatura_profesor`
  ADD PRIMARY KEY (`ClaveAP`),
  ADD KEY `AP_A` (`ClaveA`),
  ADD KEY `AP_P` (`ClaveP`);
--
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`ClaveG`);
--
-- Indices de la tabla `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`ClaveH`) USING BTREE,
  ADD KEY `AGD_AG` (`ClaveAG`);
--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`ClaveP`);
--
-- Restricciones para tablas volcadas
--
--
-- Filtros para la tabla `asignatura_grupo`
--
ALTER TABLE `asignatura_grupo`
  ADD CONSTRAINT `AG_AP` FOREIGN KEY (`ClaveAP`) REFERENCES `asignatura_profesor` (`ClaveAP`),
  ADD CONSTRAINT `AG_G` FOREIGN KEY (`ClaveG`) REFERENCES `grupos` (`ClaveG`);
--
-- Filtros para la tabla `asignatura_profesor`
--
ALTER TABLE `asignatura_profesor`
  ADD CONSTRAINT `AP_A` FOREIGN KEY (`ClaveA`) REFERENCES `asignaturas` (`ClaveA`),
  ADD CONSTRAINT `AP_P` FOREIGN KEY (`ClaveP`) REFERENCES `profesores` (`ClaveP`);
--
-- Filtros para la tabla `horario`
--
ALTER TABLE `horario`
  ADD CONSTRAINT `AGD_AG` FOREIGN KEY (`ClaveAG`) REFERENCES `asignatura_grupo` (`ClaveAG`);
--
-- Creación de usuario para acceder a la BD
--
CREATE USER 'bot'@'localhost' IDENTIFIED BY 'bot.2019';
