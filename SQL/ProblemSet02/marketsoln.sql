-- ProblemSet<00>, August <14> <2018> -- Submission by srikantan.prakash@accenture.com

locationid,name,sunlight,water
Insert into location values(0, ‘East’, .28, .80); 
Insert into location values(1, ‘North’, .17, .84); 
Insert into location values(2, ‘West’, .38, .48); 
Insert into location values(3, ‘South’, .45, .66); 

/* Set-up for gardener Table */
gardenerid,name,age
Insert into gardener values(0, ‘Mother’, 36); 
Insert into gardener values(1, ‘Father’, 38); 
Insert into gardener values(2, ‘Tim’, 15); 
Insert into gardener values(3, ‘Erin’, 12); 

/* Set-up for plant Table */
plantid,name,sunlight,water,weight
Insert into plant values(0, ‘Carrot’, .26, .82, .08); 
Insert into plant values(1, ‘Beet’, .44, .80, .04); 
Insert into plant values(2, ‘Corn’, .44, .76, .26); 
Insert into plant values(3, ‘Tomato’, .42, .80, .16); 
Insert into plant values(4, ‘Radish’, .28, .84, .02); 
Insert into plant values(5, ‘Lettuce’, .29, .85, .03); 

/* Set-up for planted Table */

Plantfk,gardenerfk,locationfk,date1,seeds
Insert into planted values(0, 0, 0 , ‘18-APR-2012’, 28); 
Insert into planted values(0, 1, 1 , ‘14-APR-2012’, 14); 
Insert into planted values(1, 0, 2 , ‘18-APR-2012’, 36); 
Insert into planted values(2, 1, 3 , ‘14-APR-2012’, 20); 
Insert into planted values(2, 2, 2 , ‘19-APR-2012’, 12); 
Insert into planted values(3, 3, 3 , ‘25-APR-2012’, 38); 
Insert into planted values(4, 2, 0 , ‘30-APR-2012’, 30); 
Insert into planted values(5, 2, 0 , ‘15-APR-2012’, 30); 

/* Set-up for picked Table */
			Plantfk,gardenerfk,locationfk,			date1,			amount, 	weight
Insert into picked values(0, 		2, 		0 , 		‘18-AUG-2012’, 		28, 		2.32); 
Insert into picked values(0, 		3, 		1 , 		‘16-AUG-2012’, 		12, 		1.02); 
Insert into picked values(2, 1, 3 , ‘22-AUG-2012’, 52, 12.96); 
Insert into picked values(2, 2, 2 , ‘28-AUG-2012’, 18, 4.58); 
Insert into picked values(3, 3, 3 , ‘22-AUG-2012’, 15, 3.84); 
Insert into picked values(4, 2, 0 , ‘16-JUL-2012’, 23, 0.52); 

1. Write a valid SQL statement that calculates the total weight of all corn cobs that were picked from the garden

select sum(p1.weight) from plant p inner join picked p1 on p.plantid=p1.plantFK group by p.name having p.name='Corn';

17.54

2. For some reason Erin has change his location for picking the tomato to North. Write the corresponding query.



3. Insert a new column 'Exper' of type Number (30) to the 'gardener' table which stores Experience of the of person. How will you modify this to varchar2(30).

alter table gardener add column exper number(30);

alter table gardener modify column exper varchar2(30);

4.Write a query to find the plant name which required seeds less than 20 which plant on 14-APR

select p.name from plant p inner join planted p1 on p1.plantFK=p.plantid where p1.date1="14-APR-2012" and p1.seeds<20;

Carrot

5. List the amount of sunlight and water to all plants with names that start with letter 'c' or letter 'r'.

select sum(sunlight),sum(water) from plant where name like 'C%' or 'R%';

0.7|1.58

6. Write a valid SQL statement that displays the plant name and the total amount of seed required for each plant that were plant in the garden. The output should be in descending order of plant name.

select p.name,sum(p1.seeds) from plant p inner join planted p1 on p.plantid=p1.plantFK group by p1.plantFK order by p.name desc;

Tomato|38
Radish|30
Lettuce|30
Corn|32
Carrot|42
Beet|36

7. Write a valid SQL statement that calculates the average number of items produced per seed planted for each plant type:( (Average Number of Items = Total Amount Picked / Total Seeds Planted.)

select p.name,p2.amount/p1.seeds as avg from plant p inner join planted p1 on p.plantid=p1.plantFK inner join picked p2 on p.plantid=p2.plantFK group by p.name;

Carrot|2
Corn|4
Radish|0
Tomato|0

8. Write a valid SQL statement that would produce a result set like the following:

 name |  name  |    date    | amount 
------|--------|------------|-------- 
 Tim  | Radish | 2012-07-16 |     23 
 Tim  | Carrot | 2012-08-18 |     28 

select g.name,p.name,p1.date1,p1.amount from picked p1 inner join Gardener g on p1.gardenerFK=g.gardenerid inner join plant p on p1.plantFK=p.plantid where g.name="Tim" and p1.amount>20 order by p1.amount;

Tim|Radish|16-JUL-2012|23
Tim|Carrot|18-AUG-2012|28

9. Find out persons who picked from the same location as he/she planted.

