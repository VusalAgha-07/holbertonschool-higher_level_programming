-- Lists all records with a score >=10 in the table second_table
-- Results display both the score and the name, ordered by score (top first)
SELECT score, name FROM second_table Where score >= 10 ORDER BY score DESC;
