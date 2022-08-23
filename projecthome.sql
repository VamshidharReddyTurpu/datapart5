-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.3.13-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table projecthome.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `customer_id` varchar(56) DEFAULT NULL,
  `customer_name` varchar(56) DEFAULT NULL,
  `product_name` varchar(56) DEFAULT NULL,
  `delivery_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table projecthome.customer: ~3 rows (approximately)
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
REPLACE INTO `customer` (`customer_id`, `customer_name`, `product_name`, `delivery_date`) VALUES
	('customer1', 'Linnea', 'Oven and drain cleaners', '2022-01-01'),
	('customer2', 'Amara', 'Laundry powder', '2022-01-02'),
	('customer3', 'jacky', 'Floor polish', '2022-01-03');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

-- Dumping structure for table projecthome.payment
CREATE TABLE IF NOT EXISTS `payment` (
  `payment_id` varchar(56) DEFAULT NULL,
  `total_cost` int(18) DEFAULT NULL,
  `total_pay_amount` int(18) DEFAULT NULL,
  `method_of_pay` varchar(56) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table projecthome.payment: ~3 rows (approximately)
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
REPLACE INTO `payment` (`payment_id`, `total_cost`, `total_pay_amount`, `method_of_pay`) VALUES
	('payment1', 1000, 500, 'offline'),
	('payment2', 2000, 2000, 'online'),
	('payment3', 3000, 3000, 'offline');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;

-- Dumping structure for table projecthome.product
CREATE TABLE IF NOT EXISTS `product` (
  `product_id` varchar(56) DEFAULT NULL,
  `product_name` varchar(56) DEFAULT NULL,
  `quantity` varchar(56) DEFAULT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table projecthome.product: ~3 rows (approximately)
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
REPLACE INTO `product` (`product_id`, `product_name`, `quantity`, `price`) VALUES
	('product1', 'Oven and drain cleaners', '1 pices', 1000),
	('product2', 'Laundry powder', '2 pack', 120),
	('product3', 'savlon', '6 pices', 280);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- Dumping structure for table projecthome.product_order
CREATE TABLE IF NOT EXISTS `product_order` (
  `order_id` varchar(56) DEFAULT NULL,
  `customer_name` varchar(56) DEFAULT NULL,
  `product_name` varchar(56) DEFAULT NULL,
  `delivery_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table projecthome.product_order: ~3 rows (approximately)
/*!40000 ALTER TABLE `product_order` DISABLE KEYS */;
REPLACE INTO `product_order` (`order_id`, `customer_name`, `product_name`, `delivery_date`) VALUES
	('order1', 'Linnea', 'Oven and drain cleaners', '2022-02-10'),
	('order2', 'Amara', 'Laundry powder', '2022-03-11'),
	('order3', 'jaccky', 'Floor polish', '2022-04-02');
/*!40000 ALTER TABLE `product_order` ENABLE KEYS */;

-- Dumping structure for table projecthome.supplier
CREATE TABLE IF NOT EXISTS `supplier` (
  `supplier_id` varchar(56) DEFAULT NULL,
  `supplier_name` varchar(56) DEFAULT NULL,
  `product_id` varchar(56) DEFAULT NULL,
  `customer_name` varchar(56) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table projecthome.supplier: ~3 rows (approximately)
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
REPLACE INTO `supplier` (`supplier_id`, `supplier_name`, `product_id`, `customer_name`) VALUES
	('supplier1', 'bond', 'product1', 'customer1'),
	('supplier2', 'bond', 'product2', 'customer2'),
	('supplier', 'tom jack', 'product3', 'customer3');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
