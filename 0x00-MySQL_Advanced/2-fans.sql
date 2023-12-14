-- Create a temporary table to store the aggregated fan counts per country
CREATE TEMPORARY TABLE IF NOT EXISTS temporary_origin_fans AS
    SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin;

-- Rank the countries based on the total number of fans in descending order
SELECT origin, nb_fans
FROM temporary_origin_fans
ORDER BY nb_fans DESC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS temporary_origin_fans;
