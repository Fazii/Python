-- MySQL dump 10.13  Distrib 5.7.16, for Win64 (x86_64)
--
-- Host: localhost    Database: wypozyczalnia_filmow
-- ------------------------------------------------------
-- Server version	5.7.16-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aktorzy`
--

DROP TABLE IF EXISTS `aktorzy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aktorzy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aktor` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aktor` (`aktor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aktorzy`
--

LOCK TABLES `aktorzy` WRITE;
/*!40000 ALTER TABLE `aktorzy` DISABLE KEYS */;
INSERT INTO `aktorzy` VALUES (4,'Sandra Bullock'),(1,'Tomasz Karolak'),(3,'Will Smith');
/*!40000 ALTER TABLE `aktorzy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `archiwum_wypozyczen`
--

DROP TABLE IF EXISTS `archiwum_wypozyczen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `archiwum_wypozyczen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nr_karty_wypozyczajacego` int(11) NOT NULL,
  `ID_egzemplarza` int(11) NOT NULL,
  `data_wypozyczenia` date DEFAULT NULL,
  `na_ile_dni` int(11) DEFAULT NULL,
  `data_oddania` date DEFAULT NULL,
  `zaplata` float DEFAULT NULL,
  `doplata` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Nr_karty_wypozyczajacego` (`Nr_karty_wypozyczajacego`),
  CONSTRAINT `Nr_karty_wypozyczajacego` FOREIGN KEY (`Nr_karty_wypozyczajacego`) REFERENCES `wypozyczajacy` (`Nr_karty_wypozyczajacego`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archiwum_wypozyczen`
--

LOCK TABLES `archiwum_wypozyczen` WRITE;
/*!40000 ALTER TABLE `archiwum_wypozyczen` DISABLE KEYS */;
/*!40000 ALTER TABLE `archiwum_wypozyczen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ceny_wypozyczen`
--

DROP TABLE IF EXISTS `ceny_wypozyczen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ceny_wypozyczen` (
  `nosnik_id` int(11) DEFAULT NULL,
  `kategoria_id` int(11) DEFAULT NULL,
  `na_ile_dni` int(11) DEFAULT NULL,
  `cena_wypozycznia` int(11) DEFAULT NULL,
  KEY `nosnik_id` (`nosnik_id`),
  KEY `kategoria_id` (`kategoria_id`),
  CONSTRAINT `kategoria_id` FOREIGN KEY (`kategoria_id`) REFERENCES `gatunki` (`id`) ON DELETE CASCADE,
  CONSTRAINT `nosnik_id` FOREIGN KEY (`nosnik_id`) REFERENCES `nosniki` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ceny_wypozyczen`
--

LOCK TABLES `ceny_wypozyczen` WRITE;
/*!40000 ALTER TABLE `ceny_wypozyczen` DISABLE KEYS */;
/*!40000 ALTER TABLE `ceny_wypozyczen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `egzemplarze`
--

DROP TABLE IF EXISTS `egzemplarze`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `egzemplarze` (
  `ID_egzemplarza` int(11) NOT NULL AUTO_INCREMENT,
  `film_ID` int(11) DEFAULT NULL,
  `stan` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_egzemplarza`),
  KEY `film_ID` (`film_ID`),
  CONSTRAINT `film_ID` FOREIGN KEY (`film_ID`) REFERENCES `filmy` (`ID_filmu`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `egzemplarze`
--

LOCK TABLES `egzemplarze` WRITE;
/*!40000 ALTER TABLE `egzemplarze` DISABLE KEYS */;
INSERT INTO `egzemplarze` VALUES (3,1,'sredni'),(4,1,'dobry'),(5,4,'zly');
/*!40000 ALTER TABLE `egzemplarze` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `film_aktorzy`
--

DROP TABLE IF EXISTS `film_aktorzy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `film_aktorzy` (
  `ID_filmu` int(11) NOT NULL,
  `ID_aktora` int(11) NOT NULL,
  KEY `ID_filmu` (`ID_filmu`),
  KEY `ID_aktora` (`ID_aktora`),
  CONSTRAINT `ID_aktora` FOREIGN KEY (`ID_aktora`) REFERENCES `aktorzy` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ID_filmu` FOREIGN KEY (`ID_filmu`) REFERENCES `filmy` (`ID_filmu`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `film_aktorzy`
--

LOCK TABLES `film_aktorzy` WRITE;
/*!40000 ALTER TABLE `film_aktorzy` DISABLE KEYS */;
INSERT INTO `film_aktorzy` VALUES (1,1),(1,3),(3,1),(4,1);
/*!40000 ALTER TABLE `film_aktorzy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filmy`
--

DROP TABLE IF EXISTS `filmy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filmy` (
  `ID_filmu` int(11) NOT NULL AUTO_INCREMENT,
  `tytul_filmu` varchar(255) DEFAULT NULL,
  `rok_wydania` year(4) DEFAULT NULL,
  `ID_rezysera` int(11) DEFAULT NULL,
  `ID_gatunku` int(11) DEFAULT NULL,
  `ID_produkcji` int(11) DEFAULT NULL,
  `ID_nosnika` int(11) DEFAULT NULL,
  `ID_kategorii` int(11) DEFAULT NULL,
  `cena_zakupu_filmu` int(11) DEFAULT NULL,
  `krotki_opis_filmu` text,
  `czas_trwania_filmu` time DEFAULT NULL,
  PRIMARY KEY (`ID_filmu`),
  KEY `ID_nosnika` (`ID_nosnika`),
  KEY `ID_kategorii` (`ID_kategorii`),
  KEY `ID_gatunku` (`ID_gatunku`),
  KEY `ID_produkcji` (`ID_produkcji`),
  KEY `ID_rezysera` (`ID_rezysera`),
  CONSTRAINT `ID_gatunku` FOREIGN KEY (`ID_gatunku`) REFERENCES `gatunki` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ID_kategorii` FOREIGN KEY (`ID_kategorii`) REFERENCES `kategorie` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ID_nosnika` FOREIGN KEY (`ID_nosnika`) REFERENCES `nosniki` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ID_produkcji` FOREIGN KEY (`ID_produkcji`) REFERENCES `produkcje` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ID_rezysera` FOREIGN KEY (`ID_rezysera`) REFERENCES `rezyserzy` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filmy`
--

LOCK TABLES `filmy` WRITE;
/*!40000 ALTER TABLE `filmy` DISABLE KEYS */;
INSERT INTO `filmy` VALUES (1,'Wykopki',2016,1,1,1,1,1,100,'Film o wykopkach','10:10:10'),(3,'Matrix',1995,1,1,1,1,1,200,'Film o matixie','01:30:00'),(4,'Chlopaki nie placza',1993,1,1,1,1,1,30,'Lorem impsum','02:00:00');
/*!40000 ALTER TABLE `filmy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gatunki`
--

DROP TABLE IF EXISTS `gatunki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gatunki` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gatunek_filmu` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gatunek_filmu` (`gatunek_filmu`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gatunki`
--

LOCK TABLES `gatunki` WRITE;
/*!40000 ALTER TABLE `gatunki` DISABLE KEYS */;
INSERT INTO `gatunki` VALUES (1,'Dramat'),(2,'Komedia'),(3,'Melodramat');
/*!40000 ALTER TABLE `gatunki` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kategorie`
--

DROP TABLE IF EXISTS `kategorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kategorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kategoria_filmu` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kategoria_filmu` (`kategoria_filmu`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategorie`
--

LOCK TABLES `kategorie` WRITE;
/*!40000 ALTER TABLE `kategorie` DISABLE KEYS */;
INSERT INTO `kategorie` VALUES (2,'+16'),(1,'+18');
/*!40000 ALTER TABLE `kategorie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nosniki`
--

DROP TABLE IF EXISTS `nosniki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nosniki` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nosnik_filmu` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nosnik_filmu` (`nosnik_filmu`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nosniki`
--

LOCK TABLES `nosniki` WRITE;
/*!40000 ALTER TABLE `nosniki` DISABLE KEYS */;
INSERT INTO `nosniki` VALUES (1,'DVD'),(2,'VHS');
/*!40000 ALTER TABLE `nosniki` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produkcje`
--

DROP TABLE IF EXISTS `produkcje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produkcje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produkcja_filmu` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `produkcja_filmu` (`produkcja_filmu`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produkcje`
--

LOCK TABLES `produkcje` WRITE;
/*!40000 ALTER TABLE `produkcje` DISABLE KEYS */;
INSERT INTO `produkcje` VALUES (1,'Film Media S.A'),(2,'Film Studio S.A');
/*!40000 ALTER TABLE `produkcje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rejestr_wypozyczen`
--

DROP TABLE IF EXISTS `rejestr_wypozyczen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rejestr_wypozyczen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nr_karty_wypozyczajacego` int(11) NOT NULL,
  `ID_egzemplarza` int(11) NOT NULL,
  `data_wypozyczenia` date NOT NULL,
  `na_ile_dni` int(11) DEFAULT NULL,
  `data_oddania` date DEFAULT NULL,
  `zaplata` float DEFAULT NULL,
  `doplata` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Nr_karty_wypozyczajacego` (`Nr_karty_wypozyczajacego`),
  KEY `ID_egzemplarza` (`ID_egzemplarza`),
  CONSTRAINT `ID_egzemplarza` FOREIGN KEY (`ID_egzemplarza`) REFERENCES `egzemplarze` (`ID_egzemplarza`) ON DELETE CASCADE,
  CONSTRAINT `rejestr_wypozyczen_ibfk_1` FOREIGN KEY (`Nr_karty_wypozyczajacego`) REFERENCES `wypozyczajacy` (`Nr_karty_wypozyczajacego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rejestr_wypozyczen`
--

LOCK TABLES `rejestr_wypozyczen` WRITE;
/*!40000 ALTER TABLE `rejestr_wypozyczen` DISABLE KEYS */;
/*!40000 ALTER TABLE `rejestr_wypozyczen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rezyserzy`
--

DROP TABLE IF EXISTS `rezyserzy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rezyserzy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rezyser_filmu` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rezyser` (`rezyser_filmu`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rezyserzy`
--

LOCK TABLES `rezyserzy` WRITE;
/*!40000 ALTER TABLE `rezyserzy` DISABLE KEYS */;
INSERT INTO `rezyserzy` VALUES (1,'Andrzej Wajda'),(2,'Krzysztof Kononowicz');
/*!40000 ALTER TABLE `rezyserzy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wojewodztwa`
--

DROP TABLE IF EXISTS `wojewodztwa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wojewodztwa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wojewodztwo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wojewodztwo` (`wojewodztwo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wojewodztwa`
--

LOCK TABLES `wojewodztwa` WRITE;
/*!40000 ALTER TABLE `wojewodztwa` DISABLE KEYS */;
INSERT INTO `wojewodztwa` VALUES (1,'malopolskie');
/*!40000 ALTER TABLE `wojewodztwa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wypozyczajacy`
--

DROP TABLE IF EXISTS `wypozyczajacy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wypozyczajacy` (
  `Nr_karty_wypozyczajacego` int(11) NOT NULL AUTO_INCREMENT,
  `nazwisko` varchar(255) NOT NULL,
  `imie` varchar(255) NOT NULL,
  `Nr_dokumentu` varchar(255) DEFAULT NULL,
  `PESEL` varchar(255) DEFAULT NULL,
  `ulica` varchar(255) DEFAULT NULL,
  `miejscowosc` varchar(255) DEFAULT NULL,
  `numer_domu` varchar(255) DEFAULT NULL,
  `kod_pocztowy` varchar(255) DEFAULT NULL,
  `numer_mieszkania` varchar(255) DEFAULT NULL,
  `ID_wojewodztwa` int(3) DEFAULT NULL,
  `telefon_domowy` varchar(255) DEFAULT NULL,
  `data_urodzenia` date DEFAULT NULL,
  `czy_jest_na_czarnej_liscie` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`Nr_karty_wypozyczajacego`),
  KEY `ID_wojewodztwa` (`ID_wojewodztwa`),
  CONSTRAINT `ID_wojewodztwa` FOREIGN KEY (`ID_wojewodztwa`) REFERENCES `wojewodztwa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wypozyczajacy`
--

LOCK TABLES `wypozyczajacy` WRITE;
/*!40000 ALTER TABLE `wypozyczajacy` DISABLE KEYS */;
INSERT INTO `wypozyczajacy` VALUES (1,'Krzysztof','Nowakowski','AWT229099','95090709850','Lesna','Szczekociny','2','42-445','NULL',1,'782185390','1995-09-07',0),(2,'Kopec','Wojciech','AWT19941004','930708190888','Szwai Jana','Krakow','7','32-337','51',1,'665887556','1993-07-08',0),(3,'Wasik','Adrian','ATW19994902','95092919995','Markowska','Krakow','9','45-009','7',1,'944934911','1995-09-09',0),(5,'Nowak','Marek','None','None','Lesna','Krakow','21','43-566','1',1,'20042456','2000-02-02',0),(6,'Adamowski','Adam','ADAMN1999','10908765876','Lesna','Krakow','2','34-224','123',1,'13344342','2000-02-02',0),(7,'Beatowska','Beata','AET123454','2453564','Bereta','Krakow','4','24-224','65',1,'235346457','1999-11-11',0);
/*!40000 ALTER TABLE `wypozyczajacy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-16 21:22:26
