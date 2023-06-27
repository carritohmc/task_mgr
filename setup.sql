--Table definition:
CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0,
    archived BOOLEAN DEFAULT 0
);

--Dummy data (for testing purposes)

INSERT INTO task (
    summary,
    description
) VALUES (
    "wash car",
    "take the car to the car wash or wash it yourself"
),
(
    "make dinner",
    "prepare ingredients and prepare a meal"
); 