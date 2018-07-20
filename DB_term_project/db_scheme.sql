create table Building(
    BID int auto_increment primary key,
    BName varchar(200) not null,
    BLocation varchar(200) not null,
    BMax int,
    check (BMax >= 1)
);

create table Performance (
    PID int auto_increment primary key,
    PName varchar(200),
    PType varchar(200),
    PPrice int,
    check (PPrice >= 0)
);

create table Audience(
    AID int auto_increment Primary key,
    AName varchar(200),
    AGender char(1),
    AAge int ,
    check (AGender in ('M', 'F')),
    check (AAge >=1)
);

create table Booking(
    PID int ,
    AID int ,
    SeatNo int,
    foreign key (PID) references Performance on delete cascade,
    foreign key (AI) references Audience on delete cascade
);

create table Assign(
    PID int,
    AID int,
    foreign key (PID) references Performance on delete cascade,
    foreign key (AI) references Audience on delete cascade
);
