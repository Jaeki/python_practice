create table Building(
    id int auto_increment Primary key,
    name varchar(200) not null,
    location varchar(200) not null,
    capacity int,
    check (capacity >= 1));

create table Performance(
    id int auto_increment Primary key,
    name varchar(200),
    type varchar(200),
    price int,
    check (PPrice >= 0)
);

create table Audience(
    id int auto_increment Primary key,
    name varchar(200),
    gender char(1),
    age int,
    check (gender in ('M', 'F')),
    check (age >=1)
);
