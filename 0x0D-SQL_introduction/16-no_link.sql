-- lists where name is not null and arranges in descenind score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
