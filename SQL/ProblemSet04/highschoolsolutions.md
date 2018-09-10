
create table Highschooler(ID int, name text, grade int);

create table Friend(ID1 int, ID2 int);

create table Likes(ID1 int, ID2 int);



insert into Highschooler values (1510, 'Jordan', 9);

insert into Highschooler values (1689, 'Gabriel', 9);

insert into Highschooler values (1381, 'Tiffany', 9);

insert into Highschooler values (1709, 'Cassandra', 9);

insert into Highschooler values (1101, 'Haley', 10);

insert into Highschooler values (1782, 'Andrew', 10);

insert into Highschooler values (1468, 'Kris', 10);

insert into Highschooler values (1641, 'Brittany', 10);

insert into Highschooler values (1247, 'Alexis', 11);

insert into Highschooler values (1316, 'Austin', 11);

insert into Highschooler values (1911, 'Gabriel', 11);

insert into Highschooler values (1501, 'Jessica', 11);

insert into Highschooler values (1304, 'Jordan', 12);

insert into Highschooler values (1025, 'John', 12);

insert into Highschooler values (1934, 'Kyle', 12);

insert into Highschooler values (1661, 'Logan', 12);


insert into Friend values (1510, 1381);

insert into Friend values (1510, 1689);

insert into Friend values (1689, 1709);

insert into Friend values (1381, 1247);

insert into Friend values (1709, 1247);

insert into Friend values (1689, 1782);

insert into Friend values (1782, 1468);

insert into Friend values (1782, 1316);

insert into Friend values (1782, 1304);

insert into Friend values (1468, 1101);

insert into Friend values (1468, 1641);

insert into Friend values (1101, 1641);

insert into Friend values (1247, 1911)

insert into Friend values (1247, 1501);

insert into Friend values (1911, 1501);

insert into Friend values (1501, 1934);

insert into Friend values (1316, 1934);

insert into Friend values (1934, 1304);

insert into Friend values (1304, 1661);

insert into Friend values (1661, 1025);

insert into Friend select ID2, ID1 from Friend;

insert into Likes values(1689, 1709);

insert into Likes values(1709, 1689);

insert into Likes values(1782, 1709);

insert into Likes values(1911, 1247);

insert into Likes values(1247, 1468);

insert into Likes values(1641, 1468);

insert into Likes values(1316, 1304);

insert into Likes values(1501, 1934);

insert into Likes values(1934, 1501);
insert into Likes values(1025, 1101);



1.Find the names of all students who are friends with someone named Gabriel. (1 point possible)
sqlite> select name from Highschooler where ID in (select ID2 from  Friend where ID1 in(select ID from Highschooler where name='Gabriel'));
Jordan
Cassandra
Andrew
Alexis
Jessica

2.For every student who likes someone 2 or more grades younger than themselves, return that student's name and grade, and the name and grade of the student they like. (1 point possible)
sqlite> select  name1, grade1, name2, grade2 from
   ...> (select h1.name as name1 , h1.grade as grade1 , h2.name as name2 , h2.grade as grade2, h1.grade-h2.grade as gradeDiff
   ...>  from Highschooler h1
   ...>  inner join likes on likes.ID1=h1.ID
   ...> inner join Highschooler h2 on h2.ID=likes.ID2) where gradeDiff>1;
John|12|Haley|10

3.For every pair of students who both like each other, return the name and grade of both students. Include each pair only once, with the two names in alphabetical order. (1 point possible)
sqlite> select h1.name,h1.grade,h2.name,h2.grade from Highschooler h1           
   ...> inner join likes l1 on l1.ID1=h1.ID
   ...> inner join Highschooler h2 on h2.ID=l1.ID2
   ...> inner join likes l2 on l1.ID1=l2.ID2 and l1.ID2=l2.ID1
   ...> where h1.ID<h2.ID order by h1.name,h2.name;
Gabriel|9|Cassandra|9
Jessica|11|Kyle|12


4.Find all students who do not appear in the Likes table (as a student who likes or is liked) and return their names and grades. Sort by grade, then by name within each grade. (1 point possible)
sqlite> select name,grade from Highschooler where ID not in ( select ID1 from likes union select ID2 from likes);
Jordan|9
Tiffany|9
Logan|12
sqlite>
5.For every situation where student A likes student B, but we have no information about whom B likes (that is, B does not appear as an ID1 in the Likes table), return A and B's names and grades. (1 point possible)

sqlite> select h1.name,h1.grade,h2.name,h2.grade from Highschooler h1
   ...> inner join likes l1 on l1.ID1=h1.ID
   ...> inner join Highschooler h2 on h2.ID=l1.ID2
   ...> where l1.ID2 not in (select ID1 from likes);
Alexis|11|Kris|10
Brittany|10|Kris|10
Austin|11|Jordan|12
John|12|Haley|10

6.Find names and grades of students who only have friends in the same grade. Return the result sorted by grade, then by name within each grade. (1 point possible)
sqlite> select h1.name,h1.grade,h2.name,h2.grade from friend
   ...> inner join Highschooler h1 on h1.ID=friend.ID1
   ...> inner join Highschooler h2 on h2.ID=friend.ID2
   ...> where h1.grade=h2.grade and h1.ID<h2.ID;
Jordan|9|Gabriel|9
Gabriel|9|Cassandra|9
Kris|10|Brittany|10
Haley|10|Brittany|10
Alexis|11|Gabriel|11
Alexis|11|Jessica|11
Jordan|12|Logan|12
Tiffany|9|Jordan|9
Kris|10|Andrew|10
Haley|10|Kris|10
Jessica|11|Gabriel|11
Jordan|12|Kyle|12
John|12|Logan|12

7.For each student A who likes a student B where the two are not friends, find if they have a friend C in common (who can introduce them!). For all such trios, return the name and grade of A, B, and C. (1 point possible)
sqlite> select h1.name,h1.grade,h2.name,h2.grade,h3.name,h3.grade from likes l1
   ...>  inner join Highschooler h1 on h1.ID=l1.ID1
   ...>  inner join Highschooler h2 on h2.ID=l1.ID2
   ...> inner join friend f1 on f1.ID1=h1.ID
   ...> inner join friend f2 on f2.ID2=h2.ID
   ...> inner join Highschooler h3 on h3.ID= f1.ID2
   ...>  where l1.ID1= f1.ID1 and l1.ID2<>f1.ID2  and l1.ID1<>f2.ID1 and f2.ID2=l1.ID2 and f1.ID2=f2.ID1;
Andrew|10|Cassandra|9|Gabriel|9
Gabriel|11|Alexis|11|Jessica|11
Brittany|10|Kris|10|Haley|10
Austin|11|Jordan|12|Andrew|10
Austin|11|Jordan|12|Kyle|12

8.Find the difference between the number of students in the school and the number of different first names. (1 point possible)
sqlite> select (select count(ID) from  Highschooler) -(select count(distinct name) from Highschooler);
2

9.Find the name and grade of all students who are liked by more than one other student. (1 point possible)
sqlite> select name,grade from Highschooler where ID in ( select ID2 from likes group by ID2 having count(ID2)>1);
Cassandra|9
Kris|10

10.For every situation where student A likes student B, but student B likes a different student C, return the names and grades of A, B, and C. (1 point possible)
sqlite> select h3.name,h3.grade,h1.name,h1.grade,h2.name,h2.grade from Highschooler h1
   ...>  inner join likes l1 on l1.ID1=h1.ID
   ...> inner join Highschooler h2 on h2.ID=l1.ID2
   ...> inner join likes l2 on l1.ID1=l2.ID2 and l1.ID2<>l2.ID1
   ...> inner join Highschooler h3 on h3.ID=l2.ID1;
Andrew|10|Cassandra|9|Gabriel|9
Gabriel|11|Alexis|11|Kris|10

11.Find those students for whom all of their friends are in different grades from themselves. Return the students' names and grades.(1 point possible)
sqlite> select h1.name,h1.grade,h2.name,h2.grade from friend f1
   ...> inner join Highschooler h1 on h1.ID=f1.ID1
   ...> inner join Highschooler h2 on h2.ID=f1.ID2
   ...> where h1.grade<>h2.grade;
Tiffany|9|Alexis|11
Cassandra|9|Alexis|11
Gabriel|9|Andrew|10
Andrew|10|Austin|11
Andrew|10|Jordan|12
Jessica|11|Kyle|12
Austin|11|Kyle|12
Alexis|11|Tiffany|9
Alexis|11|Cassandra|9
Andrew|10|Gabriel|9
Austin|11|Andrew|10
Jordan|12|Andrew|10
Kyle|12|Jessica|11
Kyle|12|Austin|11

12.What is the average number of friends per student? (Your result should be just one number.) (1 point possible)
sqlite> select avg(cnt) from(select ID1,count(ID2) as cnt from friend group by ID1);
2.5

13.Find the number of students who are either friends with Cassandra or are friends of friends of Cassandra. Do not count Cassandra, even though technically she is a friend of a friend.
sqlite> select h1.name ,h2.name from Highschooler h1
   ...>    inner join friend f1 on f1.ID1=h1.ID
   ...>    inner join Highschooler h2 on h2.ID=f1.ID2
   ...>      where ID1 in ( select ID2 from (select * from friend where ID1 in (select ID from Highschooler where name='Cassandra'))) and h1.name<>'Cassandra' and h2.name<>'Cassandra';
Gabriel|Jordan
Gabriel|Andrew
Alexis|Tiffany
Alexis|Jessica
Alexis|Gabriel


14.Find the name and grade of the student(s) with the greatest number of friends. (1 point possible)


Andrew|10
sqlite> select h1.name,h1.grade from friend f1
   ...> inner join Highschooler h1 on h1.ID=f1.ID1
   ...> group by f1.ID1 having count(f1.id2)=(select max(cnt) from (select count(ID2) as cnt from friend group by ID1));
Alexis|11
Andrew|10






sqlite> select * from likes l1
     inner join Highschooler h1 on h1.ID=l1.ID1
    inner join Highschooler h2 on h2.ID=l1.ID2
    inner join friend f1 on f1.ID1=h1.ID
    inner join friend f2 on f2.ID2=h2.ID
     inner join Highschooler h3 on h3.ID= f1.ID2
    where l1.ID1= f1.ID1 and l1.ID2<>f1.ID2  and f1.ID2=f2.ID1;
   
