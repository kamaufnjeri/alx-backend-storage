-- create indexing for table names on colum name on the first letter.
CREATE INDEX idx_name_first ON names(name(1));