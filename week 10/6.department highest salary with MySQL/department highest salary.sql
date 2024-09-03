use exercise;

Create table If Not Exists Employee (id int primary key, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int primary key, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Jim', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('3', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('5', 'Max', '90000', '1');
Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');

select * from Employee;

select * from Department;

#method 1
select d.name as Department, e.name as Employee, e.Salary
from  Employee as e
join Department as d on e.departmentId = d.id
where e.Salary = (
	select max(salary)
    from Employee
    where departmentId = e.departmentId
);

#method 2
select Department, Employee, Salary
from (select d.name as Department, e.name  as Employee, e.Salary,
dense_rank() over (partition by d.id order by e.salary desc) as rnk
from Employee as e
left outer join Department as d
on e.departmentId = d.id) as t
where t.rnk = 1