
# docker exec -it test-mysql mysql -u root -p
# ALTER USER 'rpa'@'%' IDENTIFIED WITH mysql_native_password BY 'rpa!1111';
# GRANT SELECT ON performance_schema.* TO 'rpa'@'%';
# FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS test_accounts (
    Seq INT AUTO_INCREMENT PRIMARY KEY,
    Id VARCHAR(50),
    Username VARCHAR(50),
    Password VARCHAR(50)
);
