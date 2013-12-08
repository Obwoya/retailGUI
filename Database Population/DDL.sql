DROP TABLE flag; 
DROP TABLE transactiondetails; 
DROP TABLE pdumap; 
DROP table transaction; 
DROP TABLE manager; 
DROP TABLE cashier;
DROP TABLE promotion; 
DROP TABLE batch; 
DROP TABLE product;

CREATE TABLE IF NOT EXISTS `product` (
	`barcode` BIGINT UNSIGNED PRIMARY KEY,
	`name` VARCHAR (255) NOT NULL,
	`category` VARCHAR (255) ,
	`manufacturer` VARCHAR (255) ,
	`cost` NUMERIC (10,2) NOT NULL,
	`stocklevel` INTEGER NOT NULL,
	`active` BOOLEAN DEFAULT TRUE NOT NULL,
	CHECK(`cost`>0 AND `stocklevel`>=0 AND `barcode`>0)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `batch` (
	`barcode` BIGINT UNSIGNED,
	`batchdate` DATE,
	`stock` INT,
	`expiry` DATE,
	PRIMARY KEY (`barcode`, `batchdate`),
	FOREIGN KEY (`barcode`) REFERENCES `product`(`barcode`),
	CHECK(`stock`>=0 AND `barcode`>0)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `promotion` (
	`barcode` BIGINT UNSIGNED,
	`promoid` INT,
	`type`	  INT NOT NULL,
	`value`	  INT NOT NULL,
	`expiry`  DATE,
	`active` INT DEFAULT 1,
	PRIMARY KEY (`barcode`, `promoid`),
	FOREIGN KEY (`barcode`) REFERENCES `product`(`barcode`)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `cashier` (
	`id` INT,
	`pwd` INT NOT NULL,
	`active` INT DEFAULT 1,
	PRIMARY KEY (`id`)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `transaction`(
	`transactionid` INT,
	`cashierid` INT NOT NULL,
	`date` DATE,
	`price` NUMERIC(10,2),
	PRIMARY KEY (`transactionid`),
	FOREIGN KEY (`cashierid`) REFERENCES `cashier`(`id`)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `transactiondetails` (
	`transactionid` INT,
	`barcode` BIGINT UNSIGNED,
	`promoid` INT REFERENCES `promotion`(`promoid`),
	`unitsold` INT,
	`type` VARCHAR(20),
	PRIMARY KEY (`transactionid`,`barcode`),
	FOREIGN KEY (`transactionid`) REFERENCES `transaction`(`transactionid`),
	FOREIGN KEY (`barcode`) REFERENCES `product`(`barcode`),
	CHECK (`unitsold`>0)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `manager` (
	`id` INT,
	`pwd` VARCHAR(10) NOT NULL,
	PRIMARY KEY (`id`)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `pdumap` (
	`id` BIGINT,
	`port` INT,
	`barcode` BIGINT UNSIGNED NOT NULL,
	PRIMARY KEY (`id`, `port`),
	FOREIGN KEY (`barcode`) REFERENCES `product`(`barcode`)
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;

CREATE TABLE IF NOT EXISTS `flag` (
	`flag` INT DEFAULT 1
)  ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;
INSERT INTO flag(flag) VALUES(1);
INSERT INTO manager(id, pwd) VALUES(1001, 'password');
INSERT INTO manager(id, pwd) VALUES(1002, 'password');

INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,0,38997021);
INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,1,39077557);
INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,2,67238229);
INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,3,10100338);
INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,4,10127000);
INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,5,19266268);
INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,6,10005058);
INSERT INTO `pdumap`(`id`, `port`, `barcode`) VALUES (29474,7,19341702);
INSERT INTO `cashier` (`id`, `pwd`, `active`) VALUES ('0', '0', '1');
