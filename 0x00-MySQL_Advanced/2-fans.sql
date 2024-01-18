-- Write a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans.
CREATE TEMPORARY TABLE IF NOT EXISTS temporary_origin_fans AS
    SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin;

SELECT origin, nb_fans
FROM temporary_origin_fans
ORDER BY nb_fans DESC;

DROP TEMPORARY TABLE IF EXISTS temporary_origin_fans;
