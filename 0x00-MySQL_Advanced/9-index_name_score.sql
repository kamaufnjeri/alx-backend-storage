-- create indexing for table names on colum name on the first letter and score
CREATE INDEX idx_name_first ON names(name(1), score);