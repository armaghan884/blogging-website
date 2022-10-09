-- friends.`user` definition

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `e_mail` varchar(100) NOT NULL,
  `phone` int(11) NOT NULL,
  `gender` varchar(5) NOT NULL,
  `password` varchar(30) NOT NULL,
  `friends` varchar(100) DEFAULT NULL,
  `warning` int(1) DEFAULT 0,
  `is_active` tinyint(1) DEFAULT 1,
  `user_picture` varchar(100) DEFAULT 'picture/default_picture.png',
  `date_of_birth` date NOT NULL,
  UNIQUE KEY `user_id_IDX` (`user_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4;


-- friends.address definition

CREATE TABLE `address` (
  `user_id` int(11) DEFAULT NULL,
  `street_name` varchar(100) NOT NULL,
  `street_number` int(11) DEFAULT NULL,
  `city` varchar(100) NOT NULL,
  `post_code` int(11) NOT NULL,
  `country` varchar(100) NOT NULL,
  KEY `address_FK` (`user_id`),
  CONSTRAINT `address_FK` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- friends.post definition

CREATE TABLE `post` (
  `user_id` int(11) DEFAULT NULL,
  `post` varchar(100) NOT NULL,
  `datetime` timestamp NULL DEFAULT NULL,
  `friends_like` varchar(100) DEFAULT NULL,
  KEY `message_FK` (`user_id`),
  CONSTRAINT `message_FK` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
