CREATE DATABASE  IF NOT EXISTS `mantenimiento_industrial` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mantenimiento_industrial`;
-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mantenimiento_industrial
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Dumping data for table `api_empresa`
--

LOCK TABLES `api_empresa` WRITE;
/*!40000 ALTER TABLE `api_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `api_equipo`
--

LOCK TABLES `api_equipo` WRITE;
/*!40000 ALTER TABLE `api_equipo` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `api_ordentrabajo`
--

LOCK TABLES `api_ordentrabajo` WRITE;
/*!40000 ALTER TABLE `api_ordentrabajo` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_ordentrabajo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `api_planmantencion`
--

LOCK TABLES `api_planmantencion` WRITE;
/*!40000 ALTER TABLE `api_planmantencion` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_planmantencion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `api_tecnico`
--

LOCK TABLES `api_tecnico` WRITE;
/*!40000 ALTER TABLE `api_tecnico` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_tecnico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Token',7,'add_token'),(26,'Can change Token',7,'change_token'),(27,'Can delete Token',7,'delete_token'),(28,'Can view Token',7,'view_token'),(29,'Can add token',8,'add_tokenproxy'),(30,'Can change token',8,'change_tokenproxy'),(31,'Can delete token',8,'delete_tokenproxy'),(32,'Can view token',8,'view_tokenproxy'),(33,'Can add Empresa',9,'add_empresa'),(34,'Can change Empresa',9,'change_empresa'),(35,'Can delete Empresa',9,'delete_empresa'),(36,'Can view Empresa',9,'view_empresa'),(37,'Can add Equipo',10,'add_equipo'),(38,'Can change Equipo',10,'change_equipo'),(39,'Can delete Equipo',10,'delete_equipo'),(40,'Can view Equipo',10,'view_equipo'),(41,'Can add Plan de Mantención',11,'add_planmantencion'),(42,'Can change Plan de Mantención',11,'change_planmantencion'),(43,'Can delete Plan de Mantención',11,'delete_planmantencion'),(44,'Can view Plan de Mantención',11,'view_planmantencion'),(45,'Can add Técnico',12,'add_tecnico'),(46,'Can change Técnico',12,'change_tecnico'),(47,'Can delete Técnico',12,'delete_tecnico'),(48,'Can view Técnico',12,'view_tecnico'),(49,'Can add Orden de Trabajo',13,'add_ordentrabajo'),(50,'Can change Orden de Trabajo',13,'change_ordentrabajo'),(51,'Can delete Orden de Trabajo',13,'delete_ordentrabajo'),(52,'Can view Orden de Trabajo',13,'view_ordentrabajo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'api','empresa'),(10,'api','equipo'),(13,'api','ordentrabajo'),(11,'api','planmantencion'),(12,'api','tecnico'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'authtoken','token'),(8,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-12-10 22:20:43.980219'),(2,'auth','0001_initial','2025-12-10 22:20:44.566079'),(3,'admin','0001_initial','2025-12-10 22:20:44.702590'),(4,'admin','0002_logentry_remove_auto_add','2025-12-10 22:20:44.708120'),(5,'admin','0003_logentry_add_action_flag_choices','2025-12-10 22:20:44.714237'),(6,'api','0001_initial','2025-12-10 22:20:45.207040'),(7,'contenttypes','0002_remove_content_type_name','2025-12-10 22:20:45.337276'),(8,'auth','0002_alter_permission_name_max_length','2025-12-10 22:20:45.407559'),(9,'auth','0003_alter_user_email_max_length','2025-12-10 22:20:45.439617'),(10,'auth','0004_alter_user_username_opts','2025-12-10 22:20:45.446969'),(11,'auth','0005_alter_user_last_login_null','2025-12-10 22:20:45.511851'),(12,'auth','0006_require_contenttypes_0002','2025-12-10 22:20:45.515402'),(13,'auth','0007_alter_validators_add_error_messages','2025-12-10 22:20:45.522094'),(14,'auth','0008_alter_user_username_max_length','2025-12-10 22:20:45.594133'),(15,'auth','0009_alter_user_last_name_max_length','2025-12-10 22:20:45.662707'),(16,'auth','0010_alter_group_name_max_length','2025-12-10 22:20:45.682376'),(17,'auth','0011_update_proxy_permissions','2025-12-10 22:20:45.690228'),(18,'auth','0012_alter_user_first_name_max_length','2025-12-10 22:20:45.752672'),(19,'authtoken','0001_initial','2025-12-10 22:20:45.846363'),(20,'authtoken','0002_auto_20160226_1747','2025-12-10 22:20:45.876676'),(21,'authtoken','0003_tokenproxy','2025-12-10 22:20:45.881196'),(22,'sessions','0001_initial','2025-12-10 22:20:45.935003');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'mantenimiento_industrial'
--

--
-- Dumping routines for database 'mantenimiento_industrial'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-10 22:01:28
