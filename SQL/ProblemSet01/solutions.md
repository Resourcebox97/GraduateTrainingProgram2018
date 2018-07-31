-- ProblemSet<00>, July <31> <2018> -- 
Submission by srikantan.prakash@accenture.com

Hotel Table - Hotel_No, Name, City

CREATE TABLE HOTEL(HOTEL_NO VARCHAR(5) PRIMARY KEY,NAME VARCHAR(20),CITY VARCHAR(20));

Table Created.

INSERT INTO HOTEL VALUES("H111","EMPIRE HOTEL","NEW YORK");
INSERT INTO HOTEL VALUES("H235","PARK PLACE","NEW YORK");
INSERT INTO HOTEL VALUES("H432","BROWNSTONE HOTEL","TORONTO");
INSERT INTO HOTEL VALUES("H498","JAMES PLAZA","TORONTO");
INSERT INTO HOTEL VALUES("H193","DEVON HOTEL","BOSTON");
INSERT INTO HOTEL VALUES("H437","CLAIRMONT HOTEL","BOSTON");

Record Count - 6

Room Table - Room_no, Hotel_no, Type, Price

CREATE TABLE ROOM(ROOM_NO INTEGER PRIMARY KEY,HOTEL_NO VARCHAR REFERENCES HOTEL(HOTEL_NO),TYPE VARCHAR,PRICE DECIMAL(5,2));

INSERT INTO ROOM VALUES(313,'H111','S',145.00);
INSERT INTO ROOM VALUES(412,'H111','N',145.00);
INSERT INTO ROOM VALUES(1267,'H235','N',175.00);
INSERT INTO ROOM VALUES(1289,'H235','N',195.00);
INSERT INTO ROOM VALUES(876,'H432','S',124.00);
INSERT INTO ROOM VALUES(898,'H432','S',124.00);
INSERT INTO ROOM VALUES(345,'H498','N',160.00);
INSERT INTO ROOM VALUES(467,'H498','N',180.00);
INSERT INTO ROOM VALUES(1001,'H193','S',150.00);
INSERT INTO ROOM VALUES(1201,'H193','N',175.00);
INSERT INTO ROOM VALUES(257,'H437','N',140.00);
INSERT INTO ROOM VALUES(223,'H437','N',155.00);

Record Count - 12

Booking Table - Hotel_no, Guest_no, Date_from, Date_to, Room_no

CREATE TABLE BOOKING(HOTEL_NO VARCHAR(10),GUEST_NO VARCHAR(20) REFERENCES GUEST(GUEST_NO),DATE_FROM VARCHAR(20),DATE_TO VARCHAR(20),ROOM_NO REFERENCES ROOM(ROOM_NO),CONSTRAINT PK PRIMARY KEY(DATE_FROM,DATE_TO),FOREIGN KEY(HOTEL_NO,ROOM_NO) REFERENCES ROOM(HOTEL_NO,ROOM_NO));

INSERT INTO BOOKING VALUES('H111','G256','10-AUG-99','15-AUG-99',412);
INSERT INTO BOOKING VALUES('H111','G367','18-AUG-99','21-AUG-99',412);
INSERT INTO BOOKING VALUES('H235','G879','05-SEP-99','12-SEP-99',1267);
INSERT INTO BOOKING VALUES('H498','G230','15-SEP-99','18-SEP-99',467);
INSERT INTO BOOKING VALUES('H498','G256','30-NOV-99','02-DEC-99',345);
INSERT INTO BOOKING VALUES('H498','G467','03-NOV-99','05-NOV-99',345);
INSERT INTO BOOKING VALUES('H193','G190','15-NOV-99','19-NOV-99',1001);
INSERT INTO BOOKING VALUES('H193','G367','12-SEP-99','14-SEP-99',1001);
INSERT INTO BOOKING VALUES('H193','G367','01-OCT-99','06-OCT-99',1201);
INSERT INTO BOOKING VALUES('H437','G190','04-OCT-99','06-OCT-99',223);
INSERT INTO BOOKING VALUES('H437','G879','14-SEP-99','17-SEP-99',223);

Record Count - 11

Guest Table - Guest_no, Name, City

CREATE TABLE GUEST (GUEST_NO CHAR(4) PRIMARY KEY, NAME CHAR(20),CITY CHAR(20));

INSERT INTO GUEST VALUES('G256','ADAM WAYNE','PITTSBURGH');
INSERT INTO GUEST VALUES('G367','TARA CUMMINGS','BALTIMORE');
INSERT INTO GUEST VALUES('G879','VANESSA PARRY','PITTSBURGH');
INSERT INTO GUEST VALUES('G230','TOM HANCOCK','PHILADELPHIA');
INSERT INTO GUEST VALUES('G467','ROBERT SWIFT','ATLANTA');
INSERT INTO GUEST VALUES('G190','EDWARD CANE','BALTIMORE');

Record Count - 6

1) List full details of all hotels.

select h.hotel_no,h.name,h.city,r.room_no,r.hotel_no,r.type,r.price from hotel h inner join room r where h.hotel_no=r.hotel_no;

H437|CLAIRMONT HOTEL|BOSTON|223|H437|N|155
H437|CLAIRMONT HOTEL|BOSTON|257|H437|N|140
H111|EMPIRE HOTEL|NEW YORK|313|H111|S|145
H498|JAMES PLAZA|TORONTO|345|H498|N|160
H111|EMPIRE HOTEL|NEW YORK|412|H111|N|145
H498|JAMES PLAZA|TORONTO|467|H498|N|180
H432|BROWNSTONE HOTEL|TORONTO|876|H432|S|124
H432|BROWNSTONE HOTEL|TORONTO|898|H432|S|124
H193|DEVON HOTEL|BOSTON|1001|H193|S|150
H193|DEVON HOTEL|BOSTON|1201|H193|N|175
H235|PARK PLACE|NEW YORK|1267|H235|N|175
H235|PARK PLACE|NEW YORK|1289|H235|N|195

Record Count - 12

2. List full details of all hotels in New York.

select h.hotel_no,h.name,h.city,r.room_no,r.hotel_no,r.type,r.price from hotel h inner join room r on h.hotel_no=r.hotel_no where h.city='NEW YORK';

H111|EMPIRE HOTEL|NEW YORK|313|H111|S|145
H111|EMPIRE HOTEL|NEW YORK|412|H111|N|145
H235|PARK PLACE|NEW YORK|1267|H235|N|175
H235|PARK PLACE|NEW YORK|1289|H235|N|195

Record Count - 4

3. List the names and cities of all guests, ordered according to their cities.

select name,city from guest order by city asc;

ROBERT SWIFT|ATLANTA
TARA CUMMINGS|BALTIMORE
EDWARD CANE|BALTIMORE
TOM HANCOCK|PHILADELPHIA
ADAM WAYNE|PITTSBURGH
VANESSA PARRY|PITTSBURGH

Record Count - 6

4. List all details for non-smoking rooms in ascending order of price.

select h.hotel_no,h.name,r.room_no,r.price,h.city from hotel h inner join room r on h.hotel_no=r.hotel_no where r.type='N' order by price;

H437|CLAIRMONT HOTEL|257|140|BOSTON
H111|EMPIRE HOTEL|412|145|NEW YORK
H437|CLAIRMONT HOTEL|223|155|BOSTON
H498|JAMES PLAZA|345|160|TORONTO
H193|DEVON HOTEL|1201|175|BOSTON
H235|PARK PLACE|1267|175|NEW YORK
H498|JAMES PLAZA|467|180|TORONTO
H235|PARK PLACE|1289|195|NEW YORK

Record Count - 8

5. List the number of hotels there are.

select count(*) as nohotel from hotel;

6

Record Count - 1

6. List the cities in which guests live. Each city should be listed only once.

select distinct(city) from guest;

PITTSBURGH
BALTIMORE
PHILADELPHIA
ATLANTA

Record Count - 4

7. List the average price of a room.

select avg(price) from room;

155.666666666667

Record Count - 1

8. List hotel names, their room numbers, and the type of that room.

select h.name,r.room_no,r.type from hotel h inner join room r on h.hotel_no=r.hotel_no;

CLAIRMONT HOTEL|223|N
CLAIRMONT HOTEL|257|N
EMPIRE HOTEL|313|S
JAMES PLAZA|345|N
EMPIRE HOTEL|412|N
JAMES PLAZA|467|N
BROWNSTONE HOTEL|876|S
BROWNSTONE HOTEL|898|S
DEVON HOTEL|1001|S
DEVON HOTEL|1201|N
PARK PLACE|1267|N
PARK PLACE|1289|N

Record Count - 12

9. List the hotel names, booking dates, and room numbers for all hotels in New York.

select h.name,b.date_from,b.room_no from hotel h inner join booking b on h.hotel_no=b.hotel_no where h.city='NEW YORK';

EMPIRE HOTEL|10-AUG-99|412
EMPIRE HOTEL|18-AUG-99|412
PARK PLACE|05-SEP-99|1267

Record Count - 3

10. What is the number of bookings that started in the month of September?

select count(*) from booking where date_from like'%SEP%';

4

Record Count - 1

11. List the names and cities of guests who began a stay in New York in August.

select g.name,g.city from guest g inner join booking b on b.guest_no=g.guest_no inner join hotel h on b.hotel_no=h.hotel_no where date_from like'%AUG%' AND h.city='NEW YORK';

ADAM WAYNE|PITTSBURGH
TARA CUMMINGS|BALTIMORE

Record Count - 2

12. List the hotel names and room numbers of any hotel rooms that have not been booked.

select h.name,r.room_no from hotel h inner join room r on h.hotel_no=r.hotel_no where r.room_no not in(select room_no from booking);

CLAIRMONT HOTEL|257
EMPIRE HOTEL|313
BROWNSTONE HOTEL|876
BROWNSTONE HOTEL|898
PARK PLACE|1289

Record Count - 5

13. List the hotel name and city of the hotel with the highest priced room.

select h.name,h.city from hotel h inner join room r on r.hotel_no=h.hotel_no where price=(select max(price) from room);

PARK PLACE|NEW YORK

Record Count - 1

14. List hotel names, room numbers, cities, and prices for hotels that have rooms with prices lower than the lowest priced room in a Boston hotel.

select h.name,r.room_no,h.city,r.price from hotel h inner join room r on h.hotel_no=r.hotel_no where price<(select min(r.price) from hotel h inner join room r on h.hotel_no=r.hotel_no where h.city='BOSTON');

BROWNSTONE HOTEL|876|TORONTO|124
BROWNSTONE HOTEL|898|TORONTO|124

Record Count - 2

15. List the average price of a room grouped by city.

select h.city,avg(r.price) from hotel h inner join room r on h.hotel_no=r.hotel_no group by h.city;

BOSTON|155.0
NEW YORK|165.0
TORONTO|147.0

Record Count - 3
