/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - cloud
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`cloud` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cloud`;

/*Table structure for table `coluduser` */

DROP TABLE IF EXISTS `coluduser`;

CREATE TABLE `coluduser` (
  `username` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `coluduser` */

insert  into `coluduser`(`username`,`email`,`password`) values ('dyanand','a@gmail.com','123'),('dyanand','a@gmail.com','123'),('admin','aa@gmail.com','123'),('admin','aa@gmail.com','123');

/*Table structure for table `fog` */

DROP TABLE IF EXISTS `fog`;

CREATE TABLE `fog` (
  `sl no` int(100) NOT NULL AUTO_INCREMENT,
  `filename` varchar(200) DEFAULT NULL,
  `name` text,
  `username` varchar(100) DEFAULT NULL,
  UNIQUE KEY `sl no` (`sl no`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `fog` */

insert  into `fog`(`sl no`,`filename`,`name`,`username`) values (15,'abc','hi i am from hyd','dnd'),(16,'new','welcomr in india','dnd'),(17,'innn','welcomr in india','dnd');

/*Table structure for table `foguser` */

DROP TABLE IF EXISTS `foguser`;

CREATE TABLE `foguser` (
  `username` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `foguser` */

insert  into `foguser`(`username`,`email`,`password`) values ('chotu','f@gmail.com','123');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `username` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`username`,`email`,`password`) values ('dnd','a@gmail.com','123'),('admin','z@gmail.com','123');

/*Table structure for table `user_data` */

DROP TABLE IF EXISTS `user_data`;

CREATE TABLE `user_data` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `filename` varchar(200) DEFAULT NULL,
  `name` text,
  `username` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `user_data` */

insert  into `user_data`(`id`,`filename`,`name`,`username`) values (9,'jh','hi i am from hyd','dnd'),(10,'jh','satish giridih jharkhand from  kqr','dnd'),(11,'','welcomr in india','dnd');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
