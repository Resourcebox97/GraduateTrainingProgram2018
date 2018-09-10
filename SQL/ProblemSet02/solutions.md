-- ProblemSet<00>, July <31> <2018> -- Submission by srikantan.prakash@accenture.com
1) What are the most important sql commands?

	Create database, create table, alter table, drop table, insert, select, update, delete

2)What is an Entity,Attribute,Record,operator?

	Entity is the object for which the table is created. If the table contains employee details, then the employee is the entity.
	An attribute is a component of database, it  depends on the levels. On a db level, the attribute is a table, on a table level the attribute is a field.
	A record is an entry in the table. Several fields joint together forms a record.
	An operator is used in the where clause of a query, the operators are arithmetic, logical and comparison operators.

3)Why is it essential to select columns in a resultset instead of doing a select *.What is the use of distinct?

	The distinct is used to return distinct values, it eliminates the duplicate values and returns the result.

4)What is the difference between Where and Having?

	Where clause is a filter for all the records in the table, while having is a filter for the groups created using group by statement.

5)What are the different operators used in Where.difference between And not and OR

	The different operators used in where are logical and comparison operators. The operators are =,!=,<>,>,<,>=,<=, ALL, AND, ANY, BETWEEN, EXISTS, IN, LIKE, NOT, OR, IS NULL, and UNIQUE. The NOT is a negation operaor while OR is used to combine the conditions.

6)what is the difference between Group by and order by when do we use them?

	Group by is used to group the resultset based on a like columns into a single row, while order by is used to sort the result.

7)What is an aggregate function? Specify the different types of aggregate functions.

	An aggregate function is used to perform calculation on a set of values and return a single result. The various aggregate functions are AVG, COUNT, MIN, MAX, SUM.

8)What is a constraint? What is a primary key,Foreign key? Why do we use them?

	A constraint is used to limit the entries into a table by specifying rules. They can be done at a column level and table level. The column level constraints are not null, unique, and default. The table level constraints are primary key, foreign key, and check. A primary key is a combination of unique and not null and it is used to uniquely identify each records in a table. Foreign key refers to the unique and not null records of another referred table.

9)What is an index? Why do we use indexing?

	An index is a copy of selected data from a table. Indexes are used to retrieve the data in a fast way from a database.

10)What is a view?

	A view is a searchable object which cannot store new values, but holds existing rows and columns. Several columns from different tables can be combined together to form a single view in a database. It is a virtual table.

11)Specify the different type of joins with an example?

Inner join - Used to combine two tables and return the matching value from both the tables.
Left outer join - Returns all data from left table and matching records from the right table.
Right outer join - Returns all data from right table and matching records from the left table.
Full outer join - Returns all data when there is match in left or right table.
