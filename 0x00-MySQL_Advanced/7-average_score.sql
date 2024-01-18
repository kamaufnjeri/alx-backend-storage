-- Write a SQL script that creates a stored procedure
-- AddBonus that adds a new correction for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT AVG(score) FROM corrections as c WHERE c.user_id = user_id);
    UPDATE users SET average_score = avg_score WHERE id = user_id; 
END //
DELIMITER ;