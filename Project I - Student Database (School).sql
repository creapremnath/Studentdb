create database studentdatabase;
use studentdatabase;
create table studentinfo(
id int not null auto_increment,
primary key(id),
Student_Name varchar(50) not null,
Student_Class varchar(4) not null,
Parent_Name varchar(50) not null, 
Parent_Contact_Number bigint not null, 
Address varchar(200) not null, 
Date_Of_Birth varchar(10) not null, 
Gender varchar (10) not null, 
section varchar(1) not null,
Academic_Year varchar(9) not null
)


