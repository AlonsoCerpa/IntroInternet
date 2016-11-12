-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-11-2016 a las 04:41:43
-- Versión del servidor: 10.1.16-MariaDB
-- Versión de PHP: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inmobiliaria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `id` int(10) NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`id`, `usuario`, `password`) VALUES
(1, 'admin', 'adm'),
(2, 'gerente', 'grt'),
(3, 'alonso', 'als'),
(4, 'jose', 'abc123'),
(5, 'adf', '4r452');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imagenes`
--

CREATE TABLE `imagenes` (
  `id` int(2) NOT NULL,
  `inmueble_id` int(4) NOT NULL,
  `url` text NOT NULL,
  `principal` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inmobiliarias`
--

CREATE TABLE `inmobiliarias` (
  `id` int(10) NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `codigo` varchar(10) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `RUC` bigint(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `direccion` text NOT NULL,
  `telefono` int(9) NOT NULL,
  `celular` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `inmobiliarias`
--

INSERT INTO `inmobiliarias` (`id`, `usuario`, `password`, `codigo`, `nombre`, `RUC`, `email`, `direccion`, `telefono`, `celular`) VALUES
(1, 'carlos24', 'aDE#', 'ABC-091116', 'Mi Vivienda', 28456838499, 'carlos24@gmail.com', 'Calle Lima 14 Cayma Arequipa Peru', 781459, 959879124),
(2, 'asdf', 'asdf', 'empty', 'empty', 0, 'empty', 'empty', 0, 0),
(3, 'rtt', 'gfRffT Y', 'TRR-895623', 'asfds', 549, 'a@u.e.e', 'asfd', 461, 45);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inmuebles`
--

CREATE TABLE `inmuebles` (
  `id` int(4) NOT NULL,
  `codigo` varchar(6) NOT NULL,
  `direccion` text NOT NULL,
  `referencia` text NOT NULL,
  `precio` float(9,2) NOT NULL,
  `superficie_total` float(6,2) NOT NULL,
  `superficie_construida` float(6,2) NOT NULL,
  `descripcion` text NOT NULL,
  `tipo_id` int(1) NOT NULL,
  `inmobiliaria_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `inmuebles`
--

INSERT INTO `inmuebles` (`id`, `codigo`, `direccion`, `referencia`, `precio`, `superficie_total`, `superficie_construida`, `descripcion`, `tipo_id`, `inmobiliaria_id`) VALUES
(1, '0', 'efasdf', 'asdfs', 546.45, 456.45, 453.46, 'jlbjkl', 1, 4),
(2, 'ABC-05', 'asdf', 'terte', 424.45, 42.45, 4545.45, 'jlgjil78', 2, 4),
(3, 'ABC-05', 'dgs', 'gdfg', 45.00, 546.00, 56.00, 'ji', 1, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interes`
--

CREATE TABLE `interes` (
  `id` int(4) NOT NULL,
  `interesado_id` int(4) NOT NULL,
  `inmueble_id` int(4) NOT NULL,
  `consulta` varchar(200) NOT NULL,
  `contactado` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interesado`
--

CREATE TABLE `interesado` (
  `id` int(4) NOT NULL COMMENT 'clave primaria',
  `email` varchar(50) NOT NULL COMMENT 'email',
  `password` varchar(20) NOT NULL COMMENT 'password',
  `nombre` varchar(20) NOT NULL COMMENT 'nombre',
  `celular` int(9) NOT NULL COMMENT 'celular'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos`
--

CREATE TABLE `tipos` (
  `id` int(1) NOT NULL COMMENT 'Clave primaria',
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipos`
--

INSERT INTO `tipos` (`id`, `nombre`) VALUES
(1, 'Venta'),
(2, 'Alquiler');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `imagenes`
--
ALTER TABLE `imagenes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inmobiliarias`
--
ALTER TABLE `inmobiliarias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inmuebles`
--
ALTER TABLE `inmuebles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `interes`
--
ALTER TABLE `interes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `interesado`
--
ALTER TABLE `interesado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipos`
--
ALTER TABLE `tipos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administradores`
--
ALTER TABLE `administradores`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT de la tabla `imagenes`
--
ALTER TABLE `imagenes`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `inmobiliarias`
--
ALTER TABLE `inmobiliarias`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT de la tabla `inmuebles`
--
ALTER TABLE `inmuebles`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT de la tabla `interes`
--
ALTER TABLE `interes`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `interesado`
--
ALTER TABLE `interesado`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT COMMENT 'clave primaria';
--
-- AUTO_INCREMENT de la tabla `tipos`
--
ALTER TABLE `tipos`
  MODIFY `id` int(1) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria', AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
