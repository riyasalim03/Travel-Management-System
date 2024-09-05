-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: agency
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `bid` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `start` varchar(20) DEFAULT NULL,
  `dest` varchar(20) DEFAULT NULL,
  `nos` int DEFAULT NULL,
  `no` int DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (102,300,'bus','kollam','kannur',5,8900),(103,345,'bus','kollam','kannur',3,9534),(105,123,'bus','kollam','kannur',3,8900),(109,123,'flight','dubai','kochi',1,1245),(110,123,'bus','kollam','kannur',2,8900),(111,123,'bus','kollam','kannur',1,8900),(112,123,'train','tvm','pune',2,1234),(113,123,'bus','bangalore','goa',2,5609),(114,123,'bus','bangalore','goa',2,5609),(115,123,'bus','bangalore','goa',2,5609);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bus`
--

DROP TABLE IF EXISTS `bus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bus` (
  `no` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `start` varchar(20) DEFAULT NULL,
  `dest` varchar(20) DEFAULT NULL,
  `nosa` int DEFAULT NULL,
  `day` date NOT NULL,
  PRIMARY KEY (`no`,`day`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus`
--

LOCK TABLES `bus` WRITE;
/*!40000 ALTER TABLE `bus` DISABLE KEYS */;
INSERT INTO `bus` VALUES (2365,'orange','kozhikode','palakkad',45,'2023-12-20'),(2365,'orange','kozhikode','palakkad',45,'2023-12-21'),(4578,'raj travels','thrissur','kollam',26,'2023-12-20'),(4578,'raj travels','thrissur','kollam',26,'2023-12-21'),(5609,'sharma express','bangalore','goa',40,'2023-12-20'),(5609,'sharma express','bangalore','goa',46,'2023-12-21'),(8900,'emerald travels','kollam','kannur',11,'2023-12-20'),(9534,'ksrtc','kollam','kannur',15,'2023-12-20'),(9534,'ksrtc','kollam','kannur',15,'2023-12-21'),(9845,'green travels','tvm','thrissur',23,'2023-12-20'),(9845,'green travels','tvm','thrissur',23,'2023-12-21');
/*!40000 ALTER TABLE `bus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `currb`
--

DROP TABLE IF EXISTS `currb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `currb` (
  `bno` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `currb`
--

LOCK TABLES `currb` WRITE;
/*!40000 ALTER TABLE `currb` DISABLE KEYS */;
INSERT INTO `currb` VALUES (101);
/*!40000 ALTER TABLE `currb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cust`
--

DROP TABLE IF EXISTS `cust`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cust` (
  `user_id` int NOT NULL,
  `pass` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cust`
--

LOCK TABLES `cust` WRITE;
/*!40000 ALTER TABLE `cust` DISABLE KEYS */;
INSERT INTO `cust` VALUES (123,'abc','amit'),(345,'lmn','ross'),(456,'pqr','dave'),(567,'def','robert'),(789,'xyz','john');
/*!40000 ALTER TABLE `cust` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `no` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `start` varchar(20) DEFAULT NULL,
  `dest` varchar(20) DEFAULT NULL,
  `nosa` int DEFAULT NULL,
  `day` date NOT NULL,
  PRIMARY KEY (`no`,`day`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (123,'jet airways','chennai','kolkata',32,'2023-12-20'),(123,'jet airways','chennai','kolkata',32,'2023-12-21'),(1245,'emirates','dubai','kochi',27,'2023-12-20'),(1245,'emirates','dubai','kochi',38,'2023-12-21'),(3467,'silk air','mumbai','delhi',56,'2023-12-20'),(3467,'silk air','mumbai','delhi',56,'2023-12-21'),(6789,'air india','kochi','mumbai',34,'2023-12-20'),(6789,'air india','kochi','mumbai',34,'2023-12-21'),(7890,'indigo','delhi','bangalore',25,'2023-12-20'),(7890,'indigo','delhi','bangalore',25,'2023-12-21');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train` (
  `no` int NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `start` varchar(30) DEFAULT NULL,
  `dest` varchar(30) DEFAULT NULL,
  `nosa` int DEFAULT NULL,
  `day` date NOT NULL,
  PRIMARY KEY (`no`,`day`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES (1234,'pune express','tvm','pune',18,'2023-12-21'),(1234,'pune express','tvm','pune',17,'2023-12-30'),(2345,'intercity','kozhikode','kochi',14,'2023-12-21'),(2345,'intercity','kozhikode','kochi',14,'2023-12-30'),(3456,'vande bharat','kollam','tvm',18,'2023-12-21'),(3456,'vande bharat','kollam','tvm',18,'2023-12-30'),(4567,'rajdhani','pune','kochi',25,'2023-12-21'),(4567,'rajdhani','pune','kochi',25,'2023-12-30'),(5678,'orient','palakkad','kollam',23,'2023-12-21'),(5678,'orient','palakkad','kollam',23,'2023-12-30');
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-20  0:59:08
