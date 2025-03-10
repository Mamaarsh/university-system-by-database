create database university;
use university;
create table students (
	IdCounter INT AUTO_INCREMENT PRIMARY KEY,
    ids int,
    sfname varchar(100) unicode,
    slname varchar(100) unicode,
    gpa float
);

create table course (
	ids int,
	coname varchar(200) unicode,
    score int
);