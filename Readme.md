https://mariadb.com/kb/en/how-to-convert-datetime-format-while-importing-xml/

dbschema.com

LOAD XML INFILE "C:/Users/adminuser/Desktop/GEO_7095_5539_8_1_2020_8_31_2020.XML" INTO TABLE dmlicensedata.geo ROWS IDENTIFIED BY '<item>';


CREATE TABLE `geo` (
	`Id` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'latin1_swedish_ci',
	`ComputerID` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`City` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Region` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Country` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`CountryID` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`ZipCode` MEDIUMINT(9) NULL DEFAULT NULL,
	`Long` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Location` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Lat` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Date` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Created` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Modified` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`LicenseCodeID` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`LicenseCode` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`IPAddress` CHAR(13) NULL DEFAULT '' COLLATE 'latin1_swedish_ci',
	`GeoProcessed` BIT(1) NULL DEFAULT b'0',
	`CompanyID` SMALLINT(6) NULL DEFAULT NULL,
	`ProductID` SMALLINT(6) NULL DEFAULT NULL,
	PRIMARY KEY (`Id`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;


----------
CREATE TABLE `GEO` (
	`Id` TINYTEXT NOT NULL,
	`ComputerID` TINYTEXT NULL,
	`City` TINYTEXT NULL,
	`Region` TINYTEXT NULL,
	`Country` TINYTEXT NULL,
	`CountryID` TINYTEXT NULL,
	`ZipCode` MEDIUMINT NULL DEFAULT NULL,
	`Long` TINYTEXT NULL DEFAULT NULL,
	`Location` TINYTEXT NULL DEFAULT NULL,
	`Lat` TINYTEXT NULL DEFAULT NULL,
	`Date` DATETIME NULL DEFAULT NULL,
	`Created` DATETIME NULL DEFAULT NULL,
	`Modified` DATETIME NULL DEFAULT NULL,
	`LicenseCodeID` TINYTEXT NULL,
	`LicenseCode` TINYTEXT NULL,
	`IPAddress` CHAR(13) NULL DEFAULT '',
	`GeoProcessed` BIT NULL DEFAULT 0,
	`CompanyID` SMALLINT NULL DEFAULT NULL,
	`ProductID` SMALLINT NULL DEFAULT NULL
)
COLLATE='latin1_swedish_ci'
;

ALTER TABLE `geo`
	CHANGE COLUMN `Id` `Id` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'latin1_swedish_ci' FIRST,
	ADD PRIMARY KEY (`Id`);

ALTER TABLE `geo`
	ADD PRIMARY KEY (`Id`);

-------
CREATE TABLE `geo` (
	`Id` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'latin1_swedish_ci',
	`ComputerID` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`City` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Region` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Country` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`CountryID` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`ZipCode` MEDIUMINT(9) NULL DEFAULT NULL,
	`Long` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Location` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Lat` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`Date` DATETIME NULL DEFAULT NULL,
	`Created` DATETIME NULL DEFAULT NULL,
	`Modified` DATETIME NULL DEFAULT NULL,
	`LicenseCodeID` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`LicenseCode` TINYTEXT NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`IPAddress` CHAR(13) NULL DEFAULT '' COLLATE 'latin1_swedish_ci',
	`GeoProcessed` BIT(1) NULL DEFAULT b'0',
	`CompanyID` SMALLINT(6) NULL DEFAULT NULL,
	`ProductID` SMALLINT(6) NULL DEFAULT NULL,
	PRIMARY KEY (`Id`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;
