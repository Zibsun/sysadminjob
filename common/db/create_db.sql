CREATE TABLE hh_vacancy ( 
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    salary_from REAL,
    salary_to REAL,
    currency TEXT,
    gross TEXT,
    name TEXT,
    area_name TEXT,
    responsibility TEXT,
    requirement TEXT,
    hh_id INT,
    employer_name TEXT
    );

CREATE TABLE vacancy (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    salary_from REAL,
    salary_to REAL,    
)

CREATE TABLE responsibility (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    description TEXT
)

CREATE TABLE requirement (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    description TEXT
)

CREATE TABLE vacancy_responsibility (
    vacancy_id INTEGER,
    responsibility_id INTEGER
)

CREATE TABLE vacancy_requirement (
    vacancy_id INTEGER,
    requirement_id INTEGER
)