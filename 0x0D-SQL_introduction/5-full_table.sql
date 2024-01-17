-- prints the full description of the table
SELECT COLUMN_NAME AS 'Field',
DATA_TYPE AS 'Type',
CHARACTER_MAXIMUM_LENGTH AS 'Length',
IS_NULLABLE AS 'Null'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';
