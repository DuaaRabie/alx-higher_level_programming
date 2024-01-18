-- creates the MySQL server user user_0d_1
IF NOT EXISTS (SELECT * FROM mysql.user WHERE USER = 'user_0d_1') THEN
	CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
