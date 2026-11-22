-- Lists all records of second_table that have a name, top score first
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;
