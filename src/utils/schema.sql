
CREATE TABLE reference_types (
    id INTEGER PRIMARY KEY,
    type_name TEXT UNIQUE
);

CREATE TABLE latex_references (
    id INTEGER PRIMARY KEY,
    ref_key TEXT UNIQUE,
    type_id INTEGER REFERENCES reference_types ON DELETE CASCADE
);

CREATE TABLE field_types (
    id INTEGER PRIMARY KEY,
    type_name TEXT,
    ref_type_id INTEGER REFERENCES reference_types ON DELETE CASCADE,
    required INTEGER --stored as value 0 or 1. Sqlite v3.23.0 accepts also True/False but stores values as 0 or 1.
);

CREATE TABLE reference_entries (
    id INTEGER PRIMARY KEY,
    type_id INTEGER REFERENCES field_types ON DELETE CASCADE,
    ref_id INTEGER REFERENCES latex_references ON DELETE CASCADE,
    value TEXT
);

INSERT INTO reference_types (type_name) VALUES ("book"); 
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("address", 1, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author", 1, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("edition", 1, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("editor", 1, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("month", 1, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("note", 1, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("number", 1, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("publisher", 1, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("series", 1, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("title", 1, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("volume", 1, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("year", 1, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_firstname", 1, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_lastname", 1, 1);

INSERT INTO reference_types (type_name) VALUES ("article");
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author", 2, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("journal", 2, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("month", 2, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("note", 2, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("number", 2, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("pages", 2, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("title", 2, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("volume", 2, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("year", 2, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_firstname", 2, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_lastname", 2, 1);


INSERT INTO reference_types (type_name) VALUES ("misc");
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author", 3, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_firstname", 3, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_lastname", 3, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("howpublished", 3, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("month", 3, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("note", 3, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("title", 3, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("year", 3, 0);

INSERT INTO reference_types (type_name) VALUES ("phdthesis");
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("address", 4, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author", 4, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_firstname", 4, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author_lastname", 4, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("month", 4, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("note", 4, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("school", 4, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("title", 4, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("type", 4, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("year", 4, 1);

INSERT INTO reference_types (type_name) VALUES ("incollection");
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("address", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("author", 5, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("booktitle", 5, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("chapter", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("edition", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("editor", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("month", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("note", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("number", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("pages", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("publisher", 5, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("series", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("title", 5, 1);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("type", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("volume", 5, 0);
INSERT INTO field_types (type_name, ref_type_id, required) VALUES ("year", 5, 1);

