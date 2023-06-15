CREATE DATABASE  IF NOT EXISTS `bd_inventario` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bd_inventario`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: bd_inventario
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_acceso`
--

DROP TABLE IF EXISTS `tbl_acceso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_acceso` (
  `usuario_codigo` int NOT NULL,
  `modulo_codigo` varchar(45) NOT NULL,
  `acceso_estado` varchar(45) NOT NULL,
  KEY `fk_tbl_acceso_tbl_usuario1_idx` (`usuario_codigo`),
  KEY `fk_tbl_acceso_tbl_modulo1_idx` (`modulo_codigo`),
  CONSTRAINT `fk_tbl_acceso_tbl_modulo1` FOREIGN KEY (`modulo_codigo`) REFERENCES `tbl_modulo` (`modulo_codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_tbl_acceso_tbl_usuario1` FOREIGN KEY (`usuario_codigo`) REFERENCES `tbl_usuario` (`usuario_codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_acceso`
--

LOCK TABLES `tbl_acceso` WRITE;
/*!40000 ALTER TABLE `tbl_acceso` DISABLE KEYS */;
INSERT INTO `tbl_acceso` VALUES (1,'001','activo'),(1,'00101','activo'),(1,'00102','activo'),(1,'00103','activo'),(1,'00104','activo'),(1,'00105','activo'),(1,'002','activo'),(1,'003','activo'),(3,'001','activo'),(2,'001','activo'),(2,'00101','activo'),(1,'00201','activo'),(1,'00301','activo'),(2,'00102','inactivo'),(2,'00103','inactivo'),(2,'00104','inactivo'),(2,'00105','inactivo'),(2,'002','inactivo'),(2,'00201','inactivo'),(2,'003','inactivo'),(2,'00301','inactivo'),(3,'00101','activo'),(3,'00102','activo'),(3,'00103','inactivo'),(3,'00104','inactivo'),(3,'00105','inactivo'),(3,'002','inactivo'),(3,'00201','inactivo'),(3,'003','inactivo'),(3,'00301','inactivo'),(1,'01','activo'),(2,'01','inactivo'),(3,'01','inactivo'),(1,'004','activo'),(1,'00202','activo'),(1,'00203','activo'),(1,'00204','activo'),(1,'00302','inactivo'),(1,'00303','inactivo'),(1,'00304','inactivo'),(1,'00401','inactivo'),(1,'00402','inactivo'),(1,'00403','inactivo'),(1,'00404','inactivo'),(1,'005','inactivo'),(1,'00501','inactivo'),(1,'00502','inactivo'),(1,'00503','inactivo'),(1,'00504','inactivo'),(1,'006','inactivo'),(1,'00601','inactivo'),(1,'00602','inactivo');
/*!40000 ALTER TABLE `tbl_acceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_bitacora`
--

DROP TABLE IF EXISTS `tbl_bitacora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_bitacora` (
  `bitacora_codigo` int NOT NULL AUTO_INCREMENT,
  `bitacora_descripcion` longtext NOT NULL,
  `bitacora_fecha` datetime NOT NULL,
  PRIMARY KEY (`bitacora_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_bitacora`
--

LOCK TABLES `tbl_bitacora` WRITE;
/*!40000 ALTER TABLE `tbl_bitacora` DISABLE KEYS */;
INSERT INTO `tbl_bitacora` VALUES (1,'Se Realizo una Compra de Producto kjhg con Codigo as500 Con un Peso de 2.00 cada uno, Cantidad Comprada de 1 con el Precio de 2.00 Se vendera a 2.00 teniendo una Ganancia de 0.00 el Codigo Categoria asignado es 1 con Codigo de Impuesto 1 el Codigo del Proveedor es el 1','2020-04-17 03:35:26'),(2,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as500 a as500  Se Camibo el nombre de kjhg a Sera Se Modifico la Cantidad 1 a 1 Se Modifico el Peso 2.00 a 2.00 Se Modifico el Precio de Costo 2.00 a 2.00 Se Modifico el Precio Venta 2.00 a 2.00 Se Modifico el Codigo de Categoria1 a 1 Se Modifico el Codigo de Impuesto 1 a 1 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 0.00 a 0.00','2020-04-17 03:35:50'),(3,'Se Realizo una Compra de Producto WIIU con Codigo as400 Con un Peso de 35.00 cada uno, Cantidad Comprada de 5 con el Precio de 35.00 Se vendera a 187.00 teniendo una Ganancia de 10.00 el Codigo Categoria asignado es 2 con Codigo de Impuesto 3 el Codigo del Proveedor es el 1','2020-04-17 04:10:14'),(4,'Se Realizo una Compra de Producto WIIU con Codigo as600 Con un Peso de 35.00 cada uno, Cantidad Comprada de 5 con el Precio de 35.00 Se vendera a 187.00 teniendo una Ganancia de 10.00 el Codigo Categoria asignado es 2 con Codigo de Impuesto 3 el Codigo del Proveedor es el 1','2020-04-17 04:14:59'),(5,'Se Realizo una Compra de Producto Gatonera con Codigo as700 Con un Peso de 35.00 cada uno, Cantidad Comprada de 5 con el Precio de 35.00 Se vendera a 187.00 teniendo una Ganancia de 10.00 el Codigo Categoria asignado es 1 con Codigo de Impuesto 3 el Codigo del Proveedor es el 1','2020-04-17 04:14:59'),(6,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as700 a as700  Se Camibo el nombre de Gatonera a Gatonera Se Modifico la Cantidad 5 a 2 Se Modifico el Peso 35.00 a 35.00 Se Modifico el Precio de Costo 170.00 a 170.00 Se Modifico el Precio Venta 187.00 a 187.00 Se Modifico el Codigo de Categoria1 a 1 Se Modifico el Codigo de Impuesto 3 a 3 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 10.00 a 10.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 05:39:00'),(7,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as100 a as100  Se Camibo el nombre de PetFood 100 a PetFood 100 Se Modifico la Cantidad 3 a 0 Se Modifico el Peso 100.00 a 100.00 Se Modifico el Precio de Costo 500.00 a 500.00 Se Modifico el Precio Venta 510.00 a 510.00 Se Modifico el Codigo de Categoria2 a 2 Se Modifico el Codigo de Impuesto 2 a 2 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 2.00 a 2.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 05:39:24'),(8,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as600 a as600  Se Camibo el nombre de WIIU a WIIU Se Modifico la Cantidad 5 a 2 Se Modifico el Peso 35.00 a 35.00 Se Modifico el Precio de Costo 170.00 a 170.00 Se Modifico el Precio Venta 187.00 a 187.00 Se Modifico el Codigo de Categoria2 a 2 Se Modifico el Codigo de Impuesto 3 a 3 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 10.00 a 10.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 05:39:24'),(9,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as700 a as700  Se Camibo el nombre de Gatonera a Gatonera Se Modifico la Cantidad 2 a 1 Se Modifico el Peso 35.00 a 35.00 Se Modifico el Precio de Costo 170.00 a 170.00 Se Modifico el Precio Venta 187.00 a 187.00 Se Modifico el Codigo de Categoria1 a 1 Se Modifico el Codigo de Impuesto 3 a 3 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 10.00 a 10.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 07:14:32'),(10,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as300 a as300  Se Camibo el nombre de Perrera a Perrera Se Modifico la Cantidad 3 a 2 Se Modifico el Peso 0.00 a 0.00 Se Modifico el Precio de Costo 0.00 a 0.00 Se Modifico el Precio Venta 0.00 a 0.00 Se Modifico el Codigo de Categoria1 a 1 Se Modifico el Codigo de Impuesto 1 a 1 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 0.00 a 0.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 07:26:13'),(11,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as200 a as200  Se Camibo el nombre de WIII a WIII Se Modifico la Cantidad 3 a 2 Se Modifico el Peso 30.00 a 30.00 Se Modifico el Precio de Costo 200.00 a 200.00 Se Modifico el Precio Venta 210.00 a 210.00 Se Modifico el Codigo de Categoria1 a 1 Se Modifico el Codigo de Impuesto 4 a 4 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 5.00 a 5.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 07:32:19'),(12,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as200 a as200  Se Camibo el nombre de WIII a WIII Se Modifico la Cantidad 2 a 1 Se Modifico el Peso 30.00 a 30.00 Se Modifico el Precio de Costo 200.00 a 200.00 Se Modifico el Precio Venta 210.00 a 210.00 Se Modifico el Codigo de Categoria1 a 1 Se Modifico el Codigo de Impuesto 4 a 4 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 5.00 a 5.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 07:32:34'),(13,'Se Actualizo El Producto de la tabla tbl_producto con el codigo as600 a as600  Se Camibo el nombre de WIIU a WIIU Se Modifico la Cantidad 2 a 1 Se Modifico el Peso 35.00 a 35.00 Se Modifico el Precio de Costo 170.00 a 170.00 Se Modifico el Precio Venta 187.00 a 187.00 Se Modifico el Codigo de Categoria2 a 2 Se Modifico el Codigo de Impuesto 3 a 3 Se Modifico el Codigo de Proveedor 1 a 1 Se Modifico el Porcentaje de Ganancia 10.00 a 10.00 Se Modifico el Porcentaje de Descunto 0.00 a 0.00','2020-04-18 07:33:10'),(14,'Se Realizo una Compra de Producto nom con Codigo cod002 Con un Peso de 200.00 cada uno, Cantidad Comprada de 23 con el Precio de 200.00 Se vendera a 310.00 teniendo una Ganancia de 0.00 el Codigo Categoria asignado es 1 con Codigo de Impuesto 1 el Codigo del Proveedor es el 1 Con un Descuento de 0.00','2020-04-18 18:52:05'),(15,'Se Realizo una Compra de Producto Huevos con Codigo hv100 Con un Peso de 5.00 cada uno, Cantidad Comprada de 30 con el Precio de 5.00 Se vendera a 90.90 teniendo una Ganancia de 1.00 el Codigo Categoria asignado es 1 con Codigo de Impuesto 2 el Codigo del Proveedor es el 1 Con un Descuento de 0.00','2020-04-18 19:09:17');
/*!40000 ALTER TABLE `tbl_bitacora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_categoria`
--

DROP TABLE IF EXISTS `tbl_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_categoria` (
  `categoria_codigo` int NOT NULL AUTO_INCREMENT,
  `categoria_nombre` text NOT NULL,
  `categoria_descripcion` text,
  PRIMARY KEY (`categoria_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_categoria`
--

LOCK TABLES `tbl_categoria` WRITE;
/*!40000 ALTER TABLE `tbl_categoria` DISABLE KEYS */;
INSERT INTO `tbl_categoria` VALUES (1,'Gallina','Huevos'),(2,'Perros','Caninos');
/*!40000 ALTER TABLE `tbl_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_cliente`
--

DROP TABLE IF EXISTS `tbl_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_cliente` (
  `cliente_codigo` int NOT NULL AUTO_INCREMENT,
  `cliente_nombre` text NOT NULL,
  `cliente_rtn` bigint NOT NULL,
  `cliente_direccion` longtext NOT NULL,
  PRIMARY KEY (`cliente_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_cliente`
--

LOCK TABLES `tbl_cliente` WRITE;
/*!40000 ALTER TABLE `tbl_cliente` DISABLE KEYS */;
INSERT INTO `tbl_cliente` VALUES (1,'Mario Castañeda',101197000526,'La Masica');
/*!40000 ALTER TABLE `tbl_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_cliente_contacto`
--

DROP TABLE IF EXISTS `tbl_cliente_contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_cliente_contacto` (
  `cliente_codigo` int NOT NULL,
  `cliente_contacto_telefono` int NOT NULL,
  `cliente_contacto_email` varchar(45) NOT NULL,
  PRIMARY KEY (`cliente_codigo`,`cliente_contacto_telefono`,`cliente_contacto_email`),
  KEY `fk_tbl_cliente_contacto_tbl_cliente1_idx` (`cliente_codigo`),
  CONSTRAINT `fk_tbl_cliente_contacto_tbl_cliente1` FOREIGN KEY (`cliente_codigo`) REFERENCES `tbl_cliente` (`cliente_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_cliente_contacto`
--

LOCK TABLES `tbl_cliente_contacto` WRITE;
/*!40000 ALTER TABLE `tbl_cliente_contacto` DISABLE KEYS */;
INSERT INTO `tbl_cliente_contacto` VALUES (1,654,'f');
/*!40000 ALTER TABLE `tbl_cliente_contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_config`
--

DROP TABLE IF EXISTS `tbl_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_config` (
  `config_codigo` int NOT NULL,
  `config_descripcion` varchar(45) DEFAULT NULL,
  `config_factor` int DEFAULT NULL,
  `config_correlativo_factura` int DEFAULT NULL,
  `config_correlativo_compra` int DEFAULT NULL,
  PRIMARY KEY (`config_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_config`
--

LOCK TABLES `tbl_config` WRITE;
/*!40000 ALTER TABLE `tbl_config` DISABLE KEYS */;
INSERT INTO `tbl_config` VALUES (1,NULL,NULL,14,2);
/*!40000 ALTER TABLE `tbl_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_deduccion`
--

DROP TABLE IF EXISTS `tbl_deduccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_deduccion` (
  `deduccion_codigo` int NOT NULL AUTO_INCREMENT,
  `deduccion_nombre` varchar(45) NOT NULL,
  `deduccion_descripcion` varchar(200) DEFAULT NULL,
  `deduccion_forma` varchar(45) NOT NULL,
  `deduccion_estado` varchar(45) NOT NULL,
  PRIMARY KEY (`deduccion_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_deduccion`
--

LOCK TABLES `tbl_deduccion` WRITE;
/*!40000 ALTER TABLE `tbl_deduccion` DISABLE KEYS */;
INSERT INTO `tbl_deduccion` VALUES (1,'IHSS','Deduccion de Seguro Publico','Porcentaje','habilitado'),(2,'RAP','Deduccion Publico Obligatorio','Monto','habilitado');
/*!40000 ALTER TABLE `tbl_deduccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_detalle_recibo_proveedor`
--

DROP TABLE IF EXISTS `tbl_detalle_recibo_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_detalle_recibo_proveedor` (
  `detalle_recibo_proveedor_saldo` decimal(20,2) NOT NULL,
  `detalle_recibo_proveedor_total` decimal(20,2) NOT NULL,
  `detalle_recibo_proveedor_saldoA` decimal(20,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_detalle_recibo_proveedor`
--

LOCK TABLES `tbl_detalle_recibo_proveedor` WRITE;
/*!40000 ALTER TABLE `tbl_detalle_recibo_proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_detalle_recibo_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_empleado`
--

DROP TABLE IF EXISTS `tbl_empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_empleado` (
  `empleado_codigo` int NOT NULL AUTO_INCREMENT,
  `empleado_nombre` varchar(45) NOT NULL,
  `empleado_snombre` varchar(45) DEFAULT NULL,
  `empleado_apellido` varchar(45) NOT NULL,
  `empleado_sapellido` varchar(45) DEFAULT NULL,
  `empleado_id` bigint NOT NULL,
  `empleado_fecha_nacimiento` datetime NOT NULL,
  `empleado_genero` varchar(45) NOT NULL,
  `empleado_estado_civil` varchar(45) NOT NULL,
  `empleado_cargo` varchar(45) NOT NULL,
  `empleado_tipo_contratacion` varchar(45) NOT NULL,
  `empleado_estado` varchar(45) NOT NULL,
  PRIMARY KEY (`empleado_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_empleado`
--

LOCK TABLES `tbl_empleado` WRITE;
/*!40000 ALTER TABLE `tbl_empleado` DISABLE KEYS */;
INSERT INTO `tbl_empleado` VALUES (1,'Salvador','Alejandro','Gonzalez','Acosta',107199600654,'1996-03-11 00:00:00','Masculino','Casado','Venta','Temporal','activo');
/*!40000 ALTER TABLE `tbl_empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_empleado_deduccion`
--

DROP TABLE IF EXISTS `tbl_empleado_deduccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_empleado_deduccion` (
  `empleado_codigo` int NOT NULL,
  `deduccion_codigo` int NOT NULL,
  `emp_ded_tipo` varchar(45) NOT NULL,
  `emp_ded_valor` varchar(45) NOT NULL,
  PRIMARY KEY (`empleado_codigo`,`deduccion_codigo`),
  KEY `fk_tbl_empleado_has_tbl_deduccion_tbl_deduccion1_idx` (`deduccion_codigo`),
  KEY `fk_tbl_empleado_has_tbl_deduccion_tbl_empleado1_idx` (`empleado_codigo`),
  CONSTRAINT `fk_tbl_empleado_has_tbl_deduccion_tbl_deduccion1` FOREIGN KEY (`deduccion_codigo`) REFERENCES `tbl_deduccion` (`deduccion_codigo`),
  CONSTRAINT `fk_tbl_empleado_has_tbl_deduccion_tbl_empleado1` FOREIGN KEY (`empleado_codigo`) REFERENCES `tbl_empleado` (`empleado_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_empleado_deduccion`
--

LOCK TABLES `tbl_empleado_deduccion` WRITE;
/*!40000 ALTER TABLE `tbl_empleado_deduccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_empleado_deduccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_empleado_salario`
--

DROP TABLE IF EXISTS `tbl_empleado_salario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_empleado_salario` (
  `empleado_codigo` int NOT NULL,
  `empleado_salario` int NOT NULL,
  PRIMARY KEY (`empleado_codigo`,`empleado_salario`),
  KEY `fk_tbl_empleado_salario_tbl_empleado1_idx` (`empleado_codigo`),
  CONSTRAINT `fk_tbl_empleado_salario_tbl_empleado1` FOREIGN KEY (`empleado_codigo`) REFERENCES `tbl_empleado` (`empleado_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_empleado_salario`
--

LOCK TABLES `tbl_empleado_salario` WRITE;
/*!40000 ALTER TABLE `tbl_empleado_salario` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_empleado_salario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_impuesto`
--

DROP TABLE IF EXISTS `tbl_impuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_impuesto` (
  `impueto_codigo` int NOT NULL AUTO_INCREMENT,
  `impuesto_descripcion` varchar(100) DEFAULT NULL,
  `impuesto_valor` decimal(9,2) DEFAULT NULL,
  PRIMARY KEY (`impueto_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_impuesto`
--

LOCK TABLES `tbl_impuesto` WRITE;
/*!40000 ALTER TABLE `tbl_impuesto` DISABLE KEYS */;
INSERT INTO `tbl_impuesto` VALUES (1,'ISV 0',0.00),(2,'ISV 15',0.15),(3,'ISV 16',0.16),(4,'ISV 18',0.18);
/*!40000 ALTER TABLE `tbl_impuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_modulo`
--

DROP TABLE IF EXISTS `tbl_modulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_modulo` (
  `modulo_codigo` varchar(45) NOT NULL,
  `modulo_nombre` varchar(45) DEFAULT NULL,
  `modulo_descrip` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`modulo_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_modulo`
--

LOCK TABLES `tbl_modulo` WRITE;
/*!40000 ALTER TABLE `tbl_modulo` DISABLE KEYS */;
INSERT INTO `tbl_modulo` VALUES ('001','Usuario','Menu de los Usuarios'),('00101','Crear','Crear un nuevo Usuario'),('00102','Modificar','Modificar un Usuario'),('00103','Eliminar','Eliminar el acceso a un Usuario'),('00104','Restaurar','Restaurar el acceso a un Usuario'),('00105','Accesos','Asignar o Remover Accesos a un Usuario'),('002','Cliente','Menu de los Clientes'),('00201','Crear Cliente','Crear un Cliente Nuevo'),('00202','Modificar Cliente','Modificar Cliente Existente'),('00203','Eliminar Cliente','Eliminar Cliente Existente'),('00204','Restaurar Cliente','Restaurar Cliente Existente No Disponible'),('003','Proveedor','Menu de los Proveedores'),('00301','Crear Proveedor','Crear un Proveedor Nuevo'),('00302','Modificar Proveedor','Modificar Datos de un Proveedor Agregado'),('00303','Eliminar Proveedor','Eliminar Algun Proveedor Agregado'),('00304','Restaurar Proveedor','Restaurar Proveedor anteriormente Agregado'),('004','Empleados','Configurar Empleados'),('00401','Crear Empleado','Ingresar Empleado Nuevo'),('00402','Modificar Empleado','Modificar Empleado Existente'),('00403','Eliminar Empleado','Eliminar Empleado Existente'),('00404','Restaurar Empleado','Restaurar Empleado Existente'),('005','Deduccion','Configurar Deduccion'),('00501','Crear Deduccion','Agregar un Deduccion a la Lista Disponible'),('00502','Modificar Deduccion','Modificar alguna Deduccion que este en la Lista Disponible'),('00503','Eliminar Deduccion','Eliminar alguna Deduccion de la Lista Disponible'),('00504','Restaurar Deduccion','Restaura alguna Deduccion que este Deshabilitada'),('006','Planilla','Menu de Planilla'),('00601','Ver Planilla','Ver Planilla'),('00602','Configurar Planilla','Configurar Planilla'),('01','Ajustes','Permitir Cambiar Ajustes Generales');
/*!40000 ALTER TABLE `tbl_modulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_producto`
--

DROP TABLE IF EXISTS `tbl_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_producto` (
  `producto_codigo` int NOT NULL AUTO_INCREMENT,
  `producto_codigobarra` varchar(45) NOT NULL,
  `producto_descripcion` varchar(200) NOT NULL,
  `producto_stock` int NOT NULL,
  `producto_peso` decimal(9,2) NOT NULL,
  `producto_precio_costo` decimal(9,2) NOT NULL,
  `producto_precio_venta` decimal(9,2) NOT NULL,
  `categoria_codigo` int NOT NULL,
  `impuesto_codigo` int NOT NULL,
  `proveedor_codigo` int NOT NULL,
  `producto_ganancia` decimal(9,2) NOT NULL,
  `producto_descuento` decimal(9,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`producto_codigo`,`impuesto_codigo`,`proveedor_codigo`),
  KEY `fk_tbl_producto_tbl_categoria1_idx` (`categoria_codigo`),
  KEY `fk_tbl_producto_tbl_impuesto1_idx` (`impuesto_codigo`),
  KEY `fk_tbl_producto_tbl_proveedor1_idx` (`proveedor_codigo`),
  CONSTRAINT `fk_tbl_producto_tbl_categoria1` FOREIGN KEY (`categoria_codigo`) REFERENCES `tbl_categoria` (`categoria_codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_tbl_producto_tbl_impuesto1` FOREIGN KEY (`impuesto_codigo`) REFERENCES `tbl_impuesto` (`impueto_codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_tbl_producto_tbl_proveedor1` FOREIGN KEY (`proveedor_codigo`) REFERENCES `tbl_proveedor` (`proveedor_codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_producto`
--

LOCK TABLES `tbl_producto` WRITE;
/*!40000 ALTER TABLE `tbl_producto` DISABLE KEYS */;
INSERT INTO `tbl_producto` VALUES (1,'as100','PetFood 100',0,100.00,500.00,510.00,2,2,1,2.00,0.00),(2,'as200','WIII',4,30.00,200.00,210.00,1,4,1,5.00,0.00),(3,'as300','Perrera',2,0.00,0.00,0.00,1,1,1,0.00,0.00),(4,'as400','Robin',1,190.00,5.00,5.00,2,4,1,0.00,0.00),(5,'as500','Sera',1,2.00,2.00,2.00,1,1,1,0.00,0.00),(7,'as600','WIIU',1,35.00,170.00,187.00,2,3,1,10.00,0.00),(8,'as700','Gatonera',1,35.00,170.00,187.00,1,3,1,10.00,0.00),(11,'cod01','nom',1,200.00,20.00,25.00,1,1,1,2.00,0.00),(19,'cod','nom',3,200.00,300.00,310.00,1,1,1,0.00,0.00),(20,'cod01','nom',5,200.00,20.00,20.40,1,1,1,2.00,0.00),(22,'cod002','nom',20,200.00,300.00,310.00,1,1,1,0.00,0.00),(23,'hv100','Huevos',30,5.00,90.00,90.90,1,2,1,1.00,0.00);
/*!40000 ALTER TABLE `tbl_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_proveedor`
--

DROP TABLE IF EXISTS `tbl_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_proveedor` (
  `proveedor_codigo` int NOT NULL AUTO_INCREMENT,
  `proveedor_nombre` varchar(200) NOT NULL,
  `proveedor_rtn` bigint NOT NULL,
  `proveedor_direccion` longtext,
  PRIMARY KEY (`proveedor_codigo`),
  UNIQUE KEY `proveedor_nombre_UNIQUE` (`proveedor_nombre`),
  UNIQUE KEY `proveedor_rtn_UNIQUE` (`proveedor_rtn`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_proveedor`
--

LOCK TABLES `tbl_proveedor` WRITE;
/*!40000 ALTER TABLE `tbl_proveedor` DISABLE KEYS */;
INSERT INTO `tbl_proveedor` VALUES (1,'CARGILL',1011990002413,'Col. Confite');
/*!40000 ALTER TABLE `tbl_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_proveedor_contacto`
--

DROP TABLE IF EXISTS `tbl_proveedor_contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_proveedor_contacto` (
  `proveedor_codigo` int NOT NULL,
  `proveedor_contacto_telefono` int NOT NULL,
  `proveedor_contacto_email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proveedor_codigo`,`proveedor_contacto_telefono`),
  KEY `fk_tbl_proveedor_contacto_tbl_proveedor1_idx` (`proveedor_codigo`),
  CONSTRAINT `fk_tbl_proveedor_contacto_tbl_proveedor1` FOREIGN KEY (`proveedor_codigo`) REFERENCES `tbl_proveedor` (`proveedor_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_proveedor_contacto`
--

LOCK TABLES `tbl_proveedor_contacto` WRITE;
/*!40000 ALTER TABLE `tbl_proveedor_contacto` DISABLE KEYS */;
INSERT INTO `tbl_proveedor_contacto` VALUES (1,95633607,'cargil@cargil.com');
/*!40000 ALTER TABLE `tbl_proveedor_contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_recibo`
--

DROP TABLE IF EXISTS `tbl_recibo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_recibo` (
  `recibo_codigo` int NOT NULL AUTO_INCREMENT,
  `transacciones_codigo` varchar(200) NOT NULL,
  PRIMARY KEY (`recibo_codigo`,`transacciones_codigo`),
  KEY `fk_tbl_recibo_tbl_transacciones1_idx` (`transacciones_codigo`),
  CONSTRAINT `fk_tbl_recibo_tbl_transacciones1` FOREIGN KEY (`transacciones_codigo`) REFERENCES `tbl_transacciones` (`transacciones_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_recibo`
--

LOCK TABLES `tbl_recibo` WRITE;
/*!40000 ALTER TABLE `tbl_recibo` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_recibo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_recibo_proveedor`
--

DROP TABLE IF EXISTS `tbl_recibo_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_recibo_proveedor` (
  `codigo_recibo` int NOT NULL,
  `recibo_proveedor_total` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`codigo_recibo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_recibo_proveedor`
--

LOCK TABLES `tbl_recibo_proveedor` WRITE;
/*!40000 ALTER TABLE `tbl_recibo_proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_recibo_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_transaccion_cliente`
--

DROP TABLE IF EXISTS `tbl_transaccion_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_transaccion_cliente` (
  `transacciones_codigo` varchar(200) NOT NULL,
  `cliente_codigo` int NOT NULL,
  `vendedor_codigo` int NOT NULL,
  PRIMARY KEY (`transacciones_codigo`),
  KEY `fk_tbl_transaccion_cliente_tbl_cliente1_idx` (`cliente_codigo`),
  CONSTRAINT `fk_tbl_transaccion_cliente_tbl_cliente1` FOREIGN KEY (`cliente_codigo`) REFERENCES `tbl_cliente` (`cliente_codigo`),
  CONSTRAINT `fk_tbl_transaccion_cliente_tbl_transacciones1` FOREIGN KEY (`transacciones_codigo`) REFERENCES `tbl_transacciones` (`transacciones_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_transaccion_cliente`
--

LOCK TABLES `tbl_transaccion_cliente` WRITE;
/*!40000 ALTER TABLE `tbl_transaccion_cliente` DISABLE KEYS */;
INSERT INTO `tbl_transaccion_cliente` VALUES ('FAC-002',1,1);
/*!40000 ALTER TABLE `tbl_transaccion_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_transaccion_detalle`
--

DROP TABLE IF EXISTS `tbl_transaccion_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_transaccion_detalle` (
  `transacciones_codigo` varchar(200) NOT NULL,
  `transaccion_detalle_posicion` varchar(45) NOT NULL,
  `producto_codigo` int NOT NULL,
  `transaccion_detalle_resta_unidad` int NOT NULL,
  `transaccion_detalle_cantidad` int NOT NULL,
  `transaccion_detalle_total_unidad` decimal(20,2) NOT NULL,
  `transaccion_detalle_total` decimal(20,2) NOT NULL,
  `transaccion_detalle_isv` decimal(20,2) NOT NULL,
  `transaccion_detalle_desc` decimal(20,2) NOT NULL,
  KEY `fk_tbl_transaccion_detalle_tbl_transacciones1_idx` (`transacciones_codigo`),
  KEY `fk_tbl_transaccion_detalle_tbl_producto1_idx` (`producto_codigo`),
  CONSTRAINT `fk_tbl_transaccion_detalle_tbl_producto1` FOREIGN KEY (`producto_codigo`) REFERENCES `tbl_producto` (`producto_codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_tbl_transaccion_detalle_tbl_transacciones1` FOREIGN KEY (`transacciones_codigo`) REFERENCES `tbl_transacciones` (`transacciones_codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_transaccion_detalle`
--

LOCK TABLES `tbl_transaccion_detalle` WRITE;
/*!40000 ALTER TABLE `tbl_transaccion_detalle` DISABLE KEYS */;
INSERT INTO `tbl_transaccion_detalle` VALUES ('FAC-002','1',2,-1,1,210.00,247.80,37.80,0.00),('FAC-002','1',2,-1,1,210.00,247.80,37.80,0.00),('FAC-002','2',7,-1,1,187.00,216.92,29.92,0.00),('FAC-004','0',19,-2,2,310.00,0.00,0.00,0.00),('FAC-004','1',8,-1,1,187.00,0.00,0.16,0.00),('FAC-005','0',19,-10,10,310.00,0.00,0.00,3100.00),('FAC-006','0',19,-3,3,310.00,0.00,0.00,930.00),('FAC-007','0',19,-3,3,310.00,0.00,0.00,930.00),('FAC-008','0',19,-2,2,310.00,0.00,0.00,620.00),('FAC-009','0',11,-2,2,25.00,0.00,0.00,50.00),('FAC-010','0',22,-3,3,310.00,0.00,0.00,930.00),('FAC-011','0',11,-2,2,25.00,0.00,0.00,50.00),('FAC-012','0',19,-1,1,310.00,0.00,0.00,310.00),('FAC-013','0',19,-1,1,310.00,0.00,0.00,310.00),('COM-001','0',2,-3,3,210.00,0.00,0.00,630.00);
/*!40000 ALTER TABLE `tbl_transaccion_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_transaccion_proveedor`
--

DROP TABLE IF EXISTS `tbl_transaccion_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_transaccion_proveedor` (
  `transacciones_codigo` varchar(200) NOT NULL,
  `proveedor_codigo` int NOT NULL,
  PRIMARY KEY (`transacciones_codigo`),
  KEY `fk_tbl_transaccion_proveedor_tbl_proveedor1_idx` (`proveedor_codigo`),
  CONSTRAINT `fk_tbl_transaccion_proveedor_tbl_proveedor1` FOREIGN KEY (`proveedor_codigo`) REFERENCES `tbl_proveedor` (`proveedor_codigo`),
  CONSTRAINT `fk_tbl_transaccion_proveedor_tbl_transacciones` FOREIGN KEY (`transacciones_codigo`) REFERENCES `tbl_transacciones` (`transacciones_codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_transaccion_proveedor`
--

LOCK TABLES `tbl_transaccion_proveedor` WRITE;
/*!40000 ALTER TABLE `tbl_transaccion_proveedor` DISABLE KEYS */;
INSERT INTO `tbl_transaccion_proveedor` VALUES ('COM-001',1);
/*!40000 ALTER TABLE `tbl_transaccion_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_transacciones`
--

DROP TABLE IF EXISTS `tbl_transacciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_transacciones` (
  `transacciones_codigo` varchar(200) NOT NULL,
  `transacciones_fecha` datetime NOT NULL,
  `transacciones_cliente` varchar(45) NOT NULL,
  `transacciones_total` decimal(20,2) NOT NULL,
  `transacciones_referencia` varchar(45) NOT NULL,
  `transacciones_tipo_pago` varchar(45) NOT NULL,
  `transacciones_estado` varchar(45) NOT NULL,
  PRIMARY KEY (`transacciones_codigo`,`transacciones_referencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_transacciones`
--

LOCK TABLES `tbl_transacciones` WRITE;
/*!40000 ALTER TABLE `tbl_transacciones` DISABLE KEYS */;
INSERT INTO `tbl_transacciones` VALUES ('COM-001','2020-04-18 00:00:00','1011990002413',2384.10,'Contado','Tarjeta','Cancelado'),('COM-001','2023-04-11 18:01:38','1011990002413',630.00,'Credito','Efectivo','Cancelado'),('COM-0010','2020-04-18 00:00:00','1011990002413',31251184.13,'Contado','Efectivo','Cancelado'),('COM-0011','2020-04-18 00:00:00','1011990002413',102.00,'Contado','Efectivo','Cancelado'),('COM-0012','2020-04-18 00:00:00','1011990002413',102.00,'Contado','Efectivo','Cancelado'),('COM-0013','2020-04-18 00:00:00','1011990002413',3136.05,'Contado','Efectivo','Cancelado'),('COM-002','2020-04-18 00:00:00','1011990002413',2363.70,'Contado','Efectivo','Cancelado'),('COM-003','2020-04-18 00:00:00','1011990002413',32117.09,'Contado','Efectivo','Cancelado'),('COM-004','2020-04-18 00:00:00','1011990002413',2384.10,'Contado','Efectivo','Cancelado'),('COM-005','2020-04-18 00:00:00','1011990002413',103762.89,'Contado','Efectivo','Cancelado'),('COM-006','2020-04-18 00:00:00','1011990002413',0.00,'Contado','Efectivo','Cancelado'),('COM-007','2020-04-18 00:00:00','1011990002413',216.92,'Contado','Tarjeta','Cancelado'),('COM-008','2020-04-18 00:00:00','1011990002413',0.00,'Contado','Efectivo','Cancelado'),('COM-009','2020-04-18 00:00:00','1011990002413',165.36,'Contado','Efectivo','Cancelado'),('FAC-001','2020-04-18 00:00:00','101197000526',0.00,'Contado','Efectivo','Cancelado'),('FAC-002','2020-04-18 00:00:00','101197000526',247.80,'Contado','Efectivo','Cancelado'),('FAC-004','2023-04-11 13:56:03','101197000526',807.00,'Contado','Efectivo','Cancelado'),('FAC-005','2023-04-11 14:12:13','',3100.00,'Contado','Efectivo','Cancelado'),('FAC-006','2023-04-11 14:31:55','101197000526',930.00,'Contado','Efectivo','Cancelado'),('FAC-007','2023-04-11 14:34:48','101197000526',930.00,'Credito','Efectivo','Cancelado'),('FAC-008','2023-04-11 14:35:06','101197000526',620.00,'Credito','Efectivo','Cancelado'),('FAC-009','2023-04-11 14:37:15','101197000526',50.00,'Credito','Efectivo','Cancelado'),('FAC-010','2023-04-11 14:37:55','101197000526',930.00,'Credito','Efectivo','Cancelado'),('FAC-011','2023-04-11 14:43:56','101197000526',50.00,'Credito','Efectivo','Cancelado'),('FAC-012','2023-04-11 14:58:17','',310.00,'Credito','Efectivo','Cancelado'),('FAC-013','2023-04-11 15:00:21','',310.00,'Credito','Efectivo','Cancelado');
/*!40000 ALTER TABLE `tbl_transacciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_usuario`
--

DROP TABLE IF EXISTS `tbl_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_usuario` (
  `usuario_codigo` int NOT NULL AUTO_INCREMENT,
  `usuario_nick` varchar(45) NOT NULL,
  `usuario_clave` varchar(45) NOT NULL,
  `usuario_estado` varchar(45) NOT NULL,
  PRIMARY KEY (`usuario_codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_usuario`
--

LOCK TABLES `tbl_usuario` WRITE;
/*!40000 ALTER TABLE `tbl_usuario` DISABLE KEYS */;
INSERT INTO `tbl_usuario` VALUES (1,'admin','admin','habilitado'),(2,'cusadmin','password','deshabilitado'),(3,'us001','admin','habilitado');
/*!40000 ALTER TABLE `tbl_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_vendedor`
--

DROP TABLE IF EXISTS `tbl_vendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_vendedor` (
  `vendedor_codigo` int NOT NULL AUTO_INCREMENT,
  `vendedor_nombre` varchar(45) NOT NULL,
  `usuario_codigo` int NOT NULL,
  `empleado_codigo` int NOT NULL,
  `vendedor_estado` varchar(45) NOT NULL,
  PRIMARY KEY (`vendedor_codigo`,`usuario_codigo`),
  KEY `fk_tbl_vendedor_tbl_usuario_idx` (`usuario_codigo`),
  KEY `fk_tbl_vendedor_tbl_empleado1_idx` (`empleado_codigo`),
  CONSTRAINT `fk_tbl_vendedor_tbl_empleado1` FOREIGN KEY (`empleado_codigo`) REFERENCES `tbl_empleado` (`empleado_codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_tbl_vendedor_tbl_usuario` FOREIGN KEY (`usuario_codigo`) REFERENCES `tbl_usuario` (`usuario_codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_vendedor`
--

LOCK TABLES `tbl_vendedor` WRITE;
/*!40000 ALTER TABLE `tbl_vendedor` DISABLE KEYS */;
INSERT INTO `tbl_vendedor` VALUES (1,'Salvador',1,1,'activo');
/*!40000 ALTER TABLE `tbl_vendedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vista_cliente`
--

DROP TABLE IF EXISTS `vista_cliente`;
/*!50001 DROP VIEW IF EXISTS `vista_cliente`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista_cliente` AS SELECT 
 1 AS `cliente_codigo`,
 1 AS `cliente_nombre`,
 1 AS `cliente_rtn`,
 1 AS `cliente_direccion`,
 1 AS `cliente_contacto_telefono`,
 1 AS `cliente_contacto_email`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vista_det_productos`
--

DROP TABLE IF EXISTS `vista_det_productos`;
/*!50001 DROP VIEW IF EXISTS `vista_det_productos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista_det_productos` AS SELECT 
 1 AS `producto_codigo`,
 1 AS `producto_codigobarra`,
 1 AS `producto_descripcion`,
 1 AS `producto_stock`,
 1 AS `producto_peso`,
 1 AS `producto_precio_costo`,
 1 AS `producto_precio_venta`,
 1 AS `categoria_nombre`,
 1 AS `impuesto_valor`,
 1 AS `proveedor_nombre`,
 1 AS `producto_ganancia`,
 1 AS `producto_descuento`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vista_factura`
--

DROP TABLE IF EXISTS `vista_factura`;
/*!50001 DROP VIEW IF EXISTS `vista_factura`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista_factura` AS SELECT 
 1 AS `Factura`,
 1 AS `Posicion`,
 1 AS `Fecha`,
 1 AS `Producto`,
 1 AS `Cantidad`,
 1 AS `Precio`,
 1 AS `Subtotal`,
 1 AS `Descuento`,
 1 AS `Isv`,
 1 AS `Total`,
 1 AS `Cliente`,
 1 AS `Vendedor`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vista_cliente`
--

/*!50001 DROP VIEW IF EXISTS `vista_cliente`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista_cliente` AS select `C`.`cliente_codigo` AS `cliente_codigo`,`C`.`cliente_nombre` AS `cliente_nombre`,`C`.`cliente_rtn` AS `cliente_rtn`,`C`.`cliente_direccion` AS `cliente_direccion`,`CC`.`cliente_contacto_telefono` AS `cliente_contacto_telefono`,`CC`.`cliente_contacto_email` AS `cliente_contacto_email` from (`tbl_cliente` `C` join `tbl_cliente_contacto` `CC` on((`CC`.`cliente_codigo` = `C`.`cliente_codigo`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vista_det_productos`
--

/*!50001 DROP VIEW IF EXISTS `vista_det_productos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista_det_productos` AS select `P`.`producto_codigo` AS `producto_codigo`,`P`.`producto_codigobarra` AS `producto_codigobarra`,`P`.`producto_descripcion` AS `producto_descripcion`,`P`.`producto_stock` AS `producto_stock`,`P`.`producto_peso` AS `producto_peso`,`P`.`producto_precio_costo` AS `producto_precio_costo`,`P`.`producto_precio_venta` AS `producto_precio_venta`,`C`.`categoria_nombre` AS `categoria_nombre`,`I`.`impuesto_valor` AS `impuesto_valor`,`PR`.`proveedor_nombre` AS `proveedor_nombre`,`P`.`producto_ganancia` AS `producto_ganancia`,`P`.`producto_descuento` AS `producto_descuento` from (((`tbl_producto` `P` join `tbl_impuesto` `I` on((`I`.`impueto_codigo` = `P`.`impuesto_codigo`))) join `tbl_categoria` `C` on((`C`.`categoria_codigo` = `P`.`categoria_codigo`))) join `tbl_proveedor` `PR` on((`PR`.`proveedor_codigo` = `P`.`proveedor_codigo`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vista_factura`
--

/*!50001 DROP VIEW IF EXISTS `vista_factura`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista_factura` AS select `T`.`transacciones_codigo` AS `Factura`,`TD`.`transaccion_detalle_posicion` AS `Posicion`,`T`.`transacciones_fecha` AS `Fecha`,`P`.`producto_descripcion` AS `Producto`,`TD`.`transaccion_detalle_cantidad` AS `Cantidad`,`TD`.`transaccion_detalle_total_unidad` AS `Precio`,`TD`.`transaccion_detalle_total` AS `Subtotal`,`TD`.`transaccion_detalle_desc` AS `Descuento`,`TD`.`transaccion_detalle_isv` AS `Isv`,`T`.`transacciones_total` AS `Total`,`C`.`cliente_nombre` AS `Cliente`,`V`.`vendedor_nombre` AS `Vendedor` from (((((`tbl_transacciones` `T` join `tbl_transaccion_detalle` `TD` on((`TD`.`transacciones_codigo` = `T`.`transacciones_codigo`))) join `tbl_transaccion_cliente` `TC` on((`TC`.`transacciones_codigo` = `TD`.`transacciones_codigo`))) join `tbl_producto` `P` on((`P`.`producto_codigo` = `TD`.`producto_codigo`))) join `tbl_vendedor` `V` on((`V`.`vendedor_codigo` = `TC`.`vendedor_codigo`))) join `tbl_cliente` `C` on((`C`.`cliente_codigo` = `TC`.`cliente_codigo`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-11 18:04:25
