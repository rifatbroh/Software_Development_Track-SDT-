CREATE DATABASE student;
USE student;

CREATE TABLE card(
	Roll CHAR(4) PRIMARY KEY,
    Name VARCHAR(50),
    Marks DOUBLE
    );
    
    /* insert part */
    
    INSERT INTO card
    (Roll, Name, Marks) VALUES (1, 'Rifat', 99);
    
    SET SQL_SAFE_UPDATES = 0;
    UPDATE card
    SET Name = 'Rifat Hosain'
    WHERE Roll = 1;
    SET SQL_SAFE_UPDATES = 1;
    
    /* delete part and enable/disable safe mode */
    
    SET SQL_SAFE_UPDATES = 0;
    DELETE from card
    WHERE Roll = 1;
	SET SQL_SAFE_UPDATES = 1;
    
/*
	Now we start another sql;
*/

CREATE DATABASE teacher;
USE teacher;

CREATE TABLE attendence(
	Serial CHAR(4),
    Name VARCHAR(50),
    Marks DOUBLE
    );
    
    INSERT INTO attendence
    (Serial, Name, Marks) VALUES (1, 'prome', 67);
    INSERT INTO attendence
    (Serial, Name, Marks) VALUES (2, 'rifat', 44);
    INSERT INTO attendence
    (Serial, Name, Marks) VALUES (3, 'moneem', 43);
    INSERT INTO attendence
    (Serial, Name, Marks) VALUES (4, 'salman', 44);
    INSERT INTO attendence
    (Serial, Name, Marks) VALUES (5, 'mustifiz', 37);
    
    /* use update query */
    
    SET SQL_SAFE_UPDATES = 0;
    UPDATE attendence
    SET Name = 'Bangladesh '
    WHERE Serial = 4;
    SET SQL_SAFE_UPDATES = 1;
    
    /* delate method */
    
    SET SQL_SAFE_UPDATES = 0;
    DELETE from attendence
    WHERE Serial = 1;
    SET SQL_SAFE_UPDATES = 1;
    
   