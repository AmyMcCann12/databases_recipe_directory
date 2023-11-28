-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(255),
    average_cooking_time INTEGER,
    recipe_rating INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, average_cooking_time, recipe_rating) VALUES ('Cottage Pie', 60, 5);
INSERT INTO recipes (recipe_name, average_cooking_time, recipe_rating) VALUES ('Cheese on Toast', 5, 3);
INSERT INTO recipes (recipe_name, average_cooking_time, recipe_rating) VALUES ('Beef Stew', 90, 4);
INSERT INTO recipes (recipe_name, average_cooking_time, recipe_rating) VALUES ('Tomatoe Soup', 7, 3);
INSERT INTO recipes (recipe_name, average_cooking_time, recipe_rating) VALUES ('Pasta Bake', 30, 4);
