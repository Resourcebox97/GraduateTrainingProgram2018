-- ProblemSet<00>, July <25> <2018>
-- Submission by <srikantan.prakash@accenture.com> 

1)Select the Employee with the top three salaries

select * from employee order by salary desc limit 3;

A142|TARA CUMMINGS|D04|99475|A187
A132|PAUL VINCENT|D01|94791|A120
A128|ADAM WAYNE|D05|94324|A165

Record Count - 3

2)Select the Employee with the least salary

select *from employee where salary=(select min(salary) from employee);

A111|JOHN HELLEN|D01|15380|A120

Record Count - 1

3)Select the Employee who does not have a manager in the department table

select * from employee where managerid not in(select e_id from employee e inner join dept d where d.dep_id=e.dep_id);

A178|BRUCE WILLS|D03|66861|A298
A120|TIM ARCHER|D01|48834|A298
A187|ADAM JUSTIN|D02|80543|A298
A165|NATASHA STEVENS|D05|37377|A298

Record Count - 4

4)Select the Employee who is also a Manager

select * from employee where name in(select depmanager from employee e inner join dept d where d.dep_id=e.dep_id);

A178|BRUCE WILLS|D03|66861|A298
A120|TIM ARCHER|D01|48834|A298
A187|ADAM JUSTIN|D02|80543|A298
A165|NATASHA STEVENS|D05|37377|A298

Record Count - 4

5)Select the Empolyee who is a Manager and has least salary

select name,min(salary) from (select * from employee e inner join employee e1 where e.e_id=e1.managerid);

NATASHA STEVENS|37377

Record Count - 1

6)Select the total number of Employees in Communications departments

select count(*) from employee where dep_id in(select dep_id from dept where depname='COMMUNICATIONS');

6

Record Count - 1

7)Select the Employee in Finance Department who has the top salary

i)select name,max(salary) from employee where dep_id in(select dep_id from dept where depname='FINANCE');

ADAM WAYNE|94324

Record Count - 1

ii)select name from employee where salary =(select max(salary) from employee where dep_id = (select dep_id from dept where depname='FINANCE'));

ADAM WAYNE

Record Count - 1

8)Select the Employee in product department who has the least salary

select name from employee where salary =(select min(salary) from employee where dep_id = (select dep_id from dept where depname='PRODUCT'));

NICK MARTIN

Record COunt - 1

9)Select the count of Employees in Health with maximum salary

select count(name) from employee where salary =(select max(salary) from employee where dep_id = (select dep_id from dept where depname='HEALTH'));

1

Record Count - 1

10)Select the Employees who report to Natasha Stevens

select * from employee where managerid in(select e_id from employee e inner join dept d where d.dep_id=e.dep_id and depmanager='NATASHA STEVENS');

A128|ADAM WAYNE|D05|94324|A165
A129|JOSEPH ANGELIN|D05|44280|A165

Record Count - 2

11)Display the Employee name,Employee count,Dep name,Dept manager in the Health department

select e.name,count(e.name),d.depname,d.depmanager from employee e inner join dept d where e.dep_id=d.dep_id and depname='HEALTH';

JOHN HELLEN|6|HEALTH|TIM ARCHER

Record Count - 1

12)Display the Department id,Employee ids and Manager ids for the Communications department

select d.dep_id,e.e_id,e.managerid from employee e inner join dept d where e.dep_id=d.dep_id and depname='COMMUNICATIONS';

D02|A116|A187
D02|A198|A187
D02|A187|A298
D02|A121|A187
D02|A194|A187
D02|A133|A187

Record Count - 6

13)Select the Average Expenses for Each dept with Dept id and Dept name


select d.dep_id,avg(e.salary) as average,d.depname from employee e inner join dept d where e.dep_id=d.dep_id group by e.dep_id;


D01|54527.6666666667|HEALTH
D02|48271.3333333333|COMMUNICATIONS
D03|58517.5|PRODUCT
D04|64020.0|INSURANCE
D05|58660.3333333333|FINANCE

Record Count - 5

14)Select the total expense for the department finance

select sum(salary) as Total from employee e inner join dept d where e.dep_id=d.dep_id and d.depname='FINANCE';

175981 ---------------Wrong value as I had inserted incorrect values

Record Count - 1

15)Select the department which spends the least with Dept id and Dept manager name

select d.dep_id,d.depname,sum(e.salary) as sum from employee e join dept d on e.dep_id=d.dep_id group by d.dep_id,d.depname order by sum limit 1;

D03|PRODUCT|117035

Record Count - 1

16)Select the count of Employees in each department


select count(*) as cou,d.depname from employee e inner join dept d on e.dep_id=d.dep_id group by d.depname;


6|COMMUNICATIONS
3|FINANCE
6|HEALTH
2|INSURANCE
2|PRODUCT

Record Count - 5

17)Select the count of Employees in each department having salary <10000

select count(*) as cou,d.depname from employee e inner join dept d on e.dep_id=d.dep_id where e.salary<10000 group by d.depname;

Record Count - 0

18)Select the total number of Employees in Dept id D04

select count(*) as cou,d.depname from employee e inner join dept d on e.dep_id=d.dep_id where d.dep_id='D04' group by d.depname;

2|INSURANCE

Record Count - 1

19)Select all department details of the Department with Maximum Employees

select max(count),depname,dep_id,depmanager from(select count(*) as count,d.depname,d.dep_id,d.depmanager from employee e inner join dept d on d.dep_id=e.dep_id group by e.dep_id);

6|HEALTH|D01|TIM ARCHER

Record Count - 1

20)Select the Employees who has Tim Cook as their manager

select e.name from employee e join dept d on e.dep_id=d.dep_id where d.depmanager='TIM COOK' and e.name!='TIM COOK';

Record Count - 0
