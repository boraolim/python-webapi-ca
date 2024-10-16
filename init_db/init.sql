CREATE DATABASE IF NOT EXISTS `mydb` DEFAULT CHARACTER SET UTF8;

CREATE TABLE IF NOT EXISTS `mydb`.`tbl_cat_parameters`
(
    `id`                      INT(11)       NOT NULL AUTO_INCREMENT,
    `parameter_description`   VARCHAR(255)  NOT NULL,
    `value_parameter`         TEXT          NOT NULL,
    `flag_state`              ENUM('ACTIVE','LOCKED','DELETED') NOT NULL DEFAULT 'ACTIVE',
    `added_at`                DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `user_add_date`           VARCHAR(40)   NOT NULL,
    `updated_at`              DATETIME      NULL,
    `user_update_date`        VARCHAR(40)   NULL,
    `deleted_at`              DATETIME      NULL,
    `user_delete_date`        VARCHAR(40)   NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `id_parameter_unique` (`id` ASC) VISIBLE
) ENGINE = InnoDB DEFAULT CHARACTER SET = UTF8;

CREATE TABLE IF NOT EXISTS `mydb`.`tbl_cat_users` 
(
    `id`                      int(11)       NOT NULL AUTO_INCREMENT,
    `name`                    varchar(255)  NOT NULL,
    `email`                   varchar(255)  NOT NULL,
    `flag_state`              ENUM('ACTIVE','LOCKED','DELETED') NOT NULL DEFAULT 'ACTIVE',
    `added_at`                DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `user_add_date`           VARCHAR(40)   NOT NULL,
    `updated_at`              DATETIME      NULL,
    `user_update_date`        VARCHAR(40)   NULL,
    `deleted_at`              DATETIME      NULL,
    `user_delete_date`        VARCHAR(40)   NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_user_unique` (`id` ASC) VISIBLE
) ENGINE = InnoDB DEFAULT CHARACTER SET = UTF8;

-- Store procedures.
DROP PROCEDURE IF EXISTS mydb.proc_add_new_user;

DELIMITER $$
$$
CREATE PROCEDURE mydb.proc_add_new_user(IN `p_name_user` varchar(255),
                                        IN `p_email_user` VARCHAR(255),
                                        IN `p_created_user_by` VARCHAR(255))
BEGIN
    DECLARE max_user_id INTEGER DEFAULT 0;
     SELECT count(*) INTO max_user_id 
       FROM mydb.tbl_cat_users t1 
      WHERE (t1.name = p_name_user) 
        AND (t1.flag_state = 'ACTIVE');

    IF (max_user_id = 0) THEN
        INSERT INTO mydb.tbl_users(name, email, user_add_date)
        VALUES (p_name_user, p_email_user, p_created_user_by);
    ELSE
        SIGNAL sqlstate '10002' SET message_text = "A client with a this name already exists.";
    END IF;
END$$
DELIMITER ;

DROP PROCEDURE IF EXISTS mydb.proc_get_user;

DELIMITER $$
$$
CREATE PROCEDURE mydb.proc_get_user(IN `p_id_user` INT(11))
BEGIN
    SELECT t1.id, 
           t1.name, 
           t1.email, 
           t1.flag_state, 
           t1.added_at, 
           t1.user_add_date,
           t1.updated_at,
           t1.user_update_date,
           t1.deleted_at,
           t1.user_delete_date
      FROM mydb.tbl_cat_users t1 
     WHERE (t1.flag_state = 'ACTIVE')
       AND (t1.id = p_id_user);
END$$
DELIMITER ;
