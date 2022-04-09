CREATE TABLE IF NOT EXISTS `clubs` (
`club_id`        int(11)       NOT NULL AUTO_INCREMENT 	COMMENT 'The organization id',
`type`           varchar(100)  NOT NULL                	COMMENT 'Organization Type; e.g. Academia, Industry, Government', 
`name`           varchar(100)  NOT NULL                	COMMENT 'The name of the club',
`eventName`     varchar(100)  DEFAULT NULL            	COMMENT 'The name of the event',
`start_date`         date          NOT NULL                 COMMENT 'event date',
`address`        varchar(100)  DEFAULT NULL            	COMMENT 'The address of the event',
`city`           varchar(100)  DEFAULT NULL            	COMMENT 'The city of the event.',
`state`          varchar(100)  DEFAULT NULL            	COMMENT 'The state of the event.',
`zip`            varchar(10)   DEFAULT NULL            	COMMENT 'The zip of teh event',  
PRIMARY KEY  (`club_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT="club events"