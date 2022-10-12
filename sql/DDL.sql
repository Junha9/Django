CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
<<<<<<< HEAD
  email TEXT NOT NULL UNIQUE,
);
=======
  email TEXT NOT NULL UNIQUE
);

ALTER TABLE contacts RENAME TO new_contacts;

ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

ALTER TABLE new_contacts DROP COLUMN address;
>>>>>>> f79b33047728bd9951840602aae69fce7f1a4e77
