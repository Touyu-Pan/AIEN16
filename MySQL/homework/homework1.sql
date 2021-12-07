CREATE TABLE food (
    foodid      char(5)     PRIMARY KEY,
    fname       varchar(30) ,
    expiredate  date,
    placeid     int unsigned,
    catalog     varchar(20)
);

CREATE TABLE place(
    placeid     char(2)     PRIMARY KEY,
    pname       varchar(20)
);