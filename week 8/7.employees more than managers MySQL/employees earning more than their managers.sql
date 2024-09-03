use exercise;

Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int);
Truncate table Employee;
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3');
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4');
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', null);
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', null);

drop table employee;

select * from employee;

select e.name as Employee
from employee as e
join employee as m on e.managerId = m.id
where e.salary > m.salary
 