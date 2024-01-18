-- Write a SQL script that lists all bands with
-- Glam rock as their main style, ranked by their longevity.
CREATE TEMPORARY TABLE IF NOT EXISTS temp_band_lifespan AS
    SELECT band_name AS band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%';

SELECT band_name, lifespan FROM temp_band_lifespan
ORDER BY lifespan DESC;

DROP TEMPORARY TABLE IF EXISTS temp_band_lifespan;
