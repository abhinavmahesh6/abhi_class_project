-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aeroplane`
--

DROP TABLE IF EXISTS `aeroplane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aeroplane` (
  `Plane_ID` char(6) NOT NULL,
  `Company` varchar(30) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Place_of_Departure` varchar(20) DEFAULT NULL,
  `Destination` varchar(20) DEFAULT NULL,
  `Time_of_Dep` time DEFAULT NULL,
  `Duration` time DEFAULT NULL,
  PRIMARY KEY (`Plane_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeroplane`
--

LOCK TABLES `aeroplane` WRITE;
/*!40000 ALTER TABLE `aeroplane` DISABLE KEYS */;
INSERT INTO `aeroplane` VALUES ('AA5545','American Airlines','Boeing','Chicago','Las Vegas','19:30:00','04:00:00'),('AA7182','American Airlines','Boeing','New York','Paris','19:30:00','04:00:00'),('AA8907','American Airlines','Boeing','New York','San Francisco','19:30:00','04:00:00'),('AC1034','Air Canada','Boeing','Ottawa','Chicago','19:30:00','04:00:00'),('AC1873','Air Canada','Boeing','Madrid','Ottawa','19:30:00','04:00:00'),('AC5748','Air Canada','Boeing','Mumbai','Montreal','19:30:00','04:00:00'),('AC8921','Air Canada','Boeing','Vancouver','Tokyo','19:30:00','04:00:00'),('AE3423','Air Europa','Boeing','Amsterdam','Madrid','19:30:00','04:00:00'),('AE9203','Air Europa','Boeing','Berlin','Montreal','19:30:00','04:00:00'),('AF6723','Aeroflot','Airbus','Moscow','Paris','19:30:00','04:00:00'),('AF8390','Aeroflot','Boeing','Moscow','Helsinki','19:30:00','04:00:00'),('AF9567','Air France','Boeing','Rio','Paris','19:30:00','04:00:00'),('AI6564','Air India','Boeing','Kolkata','Hyderabad','06:00:00','02:30:00'),('AI7493','Air India','Boeing','Delhi','Frankfurt','19:30:00','04:00:00'),('AI7823','Air India','Boeing','New Delhi','Paris','19:30:00','04:00:00'),('AR1629','Air France','Boeing','Dubai','Paris','19:30:00','04:00:00'),('AR1947','Air France','Boeing','Cape Town','Paris','19:30:00','04:00:00'),('AS5678','Air Asia','Airbus','Beijing','Bali','19:30:00','04:00:00'),('AX2032','Indian Airlines','Airbus','Chennai','Mumbai','19:30:00','04:00:00'),('AX9087','Indian Airlines','Airbus','Kochi','Dubai','19:30:00','04:00:00'),('BA0567','British Airways','Boeing','Edinburgh','Montreal','19:30:00','04:00:00'),('BA0923','British Airways','Airbus','Stockholm','Copenhagen','19:30:00','04:00:00'),('BA8905','British Airways','Boeing','Edinburgh','Los Angeles','19:30:00','04:00:00'),('BA8906','British Airways','Boeing','Dubai','London','19:30:00','04:00:00'),('CA0988','Carribean Airlines','Airbus','Barbedos','Montreal','19:30:00','04:00:00'),('CP2097','Cathay Pacific','Boeing','Vancouver','Bali','19:30:00','04:00:00'),('CP4523','Cathay Pacific','Boeing','Tokyo','Sydney','19:30:00','04:00:00'),('CP8907','Cathay Pacific','Boeing','Mumbai','Shangai','19:30:00','04:00:00'),('EM4957','Emirates','Boeing','Dubai','Frankfurt','19:30:00','04:00:00'),('EM5478','Emirates','Boeing','Dubai','Paris','19:30:00','04:00:00'),('ER3404','Ethihad Airways','Boeing','Chennai','Dubai','19:30:00','04:00:00'),('FA3412','Finnair','Boeing','Helsinki','Stockholm','19:30:00','04:00:00'),('IA2093','Indonesian Airlines','Airbus','Singapore','Bali','19:30:00','04:00:00'),('IA2463','Indonesian Airlines','Boeing','Sydney','Bali','19:30:00','04:00:00'),('IA7868','Indonesian Airlines','Boeing','Chennai','Bali','19:30:00','04:00:00'),('IN7806','Indigo','Airbus','Guwahati','Mumbai','19:30:00','04:00:00'),('IN8907','Indigo','Airbus','Hyderabad','Banglore','19:30:00','04:00:00'),('JA3987','Jet Airways','Airbus','Delhi','Kolkata','19:30:00','04:00:00'),('JF2634','Singapore Airlines','Boeing','Singapore','Chennai','19:30:00','04:00:00'),('JF4786','Singapore Airlines','Airbus','Kuala Lumpur','Singapore','19:30:00','04:00:00'),('LT1583','Lufthansa','Boeing','Berlin','Moscow','19:30:00','04:00:00'),('LT1685','Lufthansa','Boeing','Hong Kong','Paris','19:30:00','04:00:00'),('LT1956','Lufthansa','Boeing','Chicago','Frankfurt','19:30:00','04:00:00'),('LT9089','Lufthansa','Airbus','Copenhagen','Amsterdam','19:30:00','04:00:00'),('QA9547','Qantas','Boeing','Fiji','Frankfurt','19:30:00','04:00:00'),('SA9403','SwissAir','Boeing','Geneva','Frankfurt','19:30:00','04:00:00'),('SJ0988','SpiceJet','Airbus','Kolkata','Mumbai','19:30:00','04:00:00'),('SJ3468','SpiceJet','Airbus','Kanyakumari','Leh','19:30:00','04:00:00'),('TA1097','Thai Airways','Airbus','Singapore','Bali','19:30:00','04:00:00'),('WJ0012','WestJet','Airbus','Las Vegas','Vancouver','19:30:00','04:00:00'),('WJ9568','WestJet','Boeing','Los Angeles','Montreal','19:30:00','04:00:00');
/*!40000 ALTER TABLE `aeroplane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aeroplane_cost`
--

DROP TABLE IF EXISTS `aeroplane_cost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aeroplane_cost` (
  `Plane_ID` char(6) DEFAULT NULL,
  `Class` varchar(15) DEFAULT NULL,
  `Cost` int DEFAULT NULL,
  KEY `Plane_ID` (`Plane_ID`),
  CONSTRAINT `aeroplane_cost_ibfk_1` FOREIGN KEY (`Plane_ID`) REFERENCES `aeroplane` (`Plane_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aeroplane_cost`
--

LOCK TABLES `aeroplane_cost` WRITE;
/*!40000 ALTER TABLE `aeroplane_cost` DISABLE KEYS */;
INSERT INTO `aeroplane_cost` VALUES ('AX2032','Business',8700),('AX2032','Premium Economy',7000),('AX2032','Economy',5800),('ER3404','Business',23000),('ER3404','Premium Economy',20000),('ER3404','Economy',16700),('BA8906','Business',32000),('BA8906','Premium Economy',29000),('BA8906','Economy',25500),('SJ0988','Business',8600),('SJ0988','Premium Economy',7200),('SJ0988','Economy',6000),('JF2634','Business',32000),('JF2634','Premium Economy',29000),('JF2634','Economy',26500),('JF4786','Business',15000),('JF4786','Premium Economy',12000),('JF4786','Economy',9500),('IN7806','Business',7400),('IN7806','Premium Economy',5800),('IN7806','Economy',4000),('SJ3468','Business',10300),('SJ3468','Premium Economy',9000),('SJ3468','Economy',7500),('BA8905','Business',35000),('BA8905','Premium Economy',32500),('BA8905','Economy',30000),('AA8907','Business',16000),('AA8907','Premium Economy',14500),('AA8907','Economy',13000),('CP8907','Business',20000),('CP8907','Premium Economy',17000),('CP8907','Economy',15000),('AX9087','Business',15400),('AX9087','Premium Economy',14000),('AX9087','Economy',12500),('LT1583','Business',25500),('LT1583','Premium Economy',24200),('LT1583','Economy',23132),('AF8390','Business',31999),('AF8390','Premium Economy',29998),('AF8390','Economy',26999),('JA3987','Business',7300),('JA3987','Premium Economy',6500),('JA3987','Economy',5000),('IN8907','Business',4500),('IN8907','Premium Economy',3700),('IN8907','Economy',2900),('FA3412','Business',5700),('FA3412','Premium Economy',4800),('FA3412','Economy',4000),('BA0923','Business',4799),('BA0923','Premium Economy',3999),('BA0923','Economy',3299),('LT9089','Business',6300),('LT9089','Premium Economy',5600),('LT9089','Economy',4700),('AE3423','Business',4900),('AE3423','Premium Economy',4400),('AE3423','Economy',3900),('AC1873','Business',37000),('AC1873','Premium Economy',34000),('AC1873','Economy',31000),('AC1034','Business',11000),('AC1034','Premium Economy',9400),('AC1034','Economy',8000),('AA5545','Business',6500),('AA5545','Premium Economy',5600),('AA5545','Economy',4900),('WJ0012','Business',6700),('WJ0012','Premium Economy',5800),('WJ0012','Economy',5000),('AC8921','Business',40000),('AC8921','Premium Economy',38400),('AC8921','Economy',35000),('CP4523','Business',150000),('CP4523','Premium Economy',136000),('CP4523','Economy',129000),('EM5478','Business',27000),('EM5478','Premium Economy',25500),('EM5478','Economy',24000),('AI6564','Business',15000),('AI6564','Premium Economy',10000),('AI6564','Economy',7000);
/*!40000 ALTER TABLE `aeroplane_cost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `Bookedby` varchar(30) NOT NULL,
  `BookingID` bigint DEFAULT NULL,
  `Date_of_Booking` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES ('Mahesh',4299659200,'2021-01-24');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cust_info`
--

DROP TABLE IF EXISTS `cust_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cust_info` (
  `Name` varchar(30) DEFAULT NULL,
  `Passport_No` bigint DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Age` varchar(10) DEFAULT NULL,
  `Travel_ID` varchar(10) NOT NULL,
  `meal_pref` varchar(10) DEFAULT NULL,
  `Plane_ID` char(6) DEFAULT NULL,
  `Date_of_Dep` date DEFAULT NULL,
  `Time_of_Dep` time DEFAULT NULL,
  `BookingID` bigint DEFAULT NULL,
  `Class` varchar(15) DEFAULT NULL,
  `Adult` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Travel_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cust_info`
--

LOCK TABLES `cust_info` WRITE;
/*!40000 ALTER TABLE `cust_info` DISABLE KEYS */;
INSERT INTO `cust_info` VALUES ('Mahesh',123456789012,'M','17','A0075','Veg','AI6564','2021-01-28','06:00:00',4299659200,'Premium Economy','Adult');
/*!40000 ALTER TABLE `cust_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-24 14:50:06
