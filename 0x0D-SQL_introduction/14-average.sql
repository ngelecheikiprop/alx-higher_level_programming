-- gets the score average and puts it in a new column called average
-- ALTER TABLE second_table ADD average FLOAT;
-- INSERT INTO second_table (average)
SELECT AVG(score) AS average FROM second_table;
