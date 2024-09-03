create schema exercise;
use exercise;

Create table If Not Exists Employee (Id int primary key, Salary int);
Truncate table Employee;
insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');

select * from Employee;

drop table Employee;

# method 1
select max(salary) as SecondHighestSalary 
from Employee
where salary < (select max(salary) from Employee);

#method 2
select distinct salary
from Employee
order by salary desc
limit 1 offset 1;