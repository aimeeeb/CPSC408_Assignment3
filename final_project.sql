create table EventAttendees
(
    AttendeeName varchar(50) null,
    Event        int         null
);


create table Events
(
    EventId int auto_increment
        primary key,
    Name    varchar(32) null,
    Date    datetime    null
);


create table ListItems
(
    ItemID      int auto_increment
        primary key,
    ItemName    varchar(32)          null,
    Description varchar(140)         null,
    DueDate     datetime             null,
    List        int                  null,
    Deleted     datetime             null,
    Complete    tinyint(1) default 0 null
);


create table Lists
(
    ListId   int auto_increment
        primary key,
    ListName varchar(12) null
);


create table Users
(
    UserId   int auto_increment
        primary key,
    Username varchar(32) null
);

