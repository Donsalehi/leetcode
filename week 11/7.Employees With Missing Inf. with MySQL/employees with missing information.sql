use exercise;

Create table If Not Exists Employees (employee_id int primary key, name varchar(30));
Create table If Not Exists Salaries (employee_id int primary key, salary int);
Truncate table Employees;
insert into Employees (employee_id, name) values ('2', 'Crew');
insert into Employees (employee_id, name) values ('4', 'Haven');
insert into Employees (employee_id, name) values ('5', 'Kristian');
Truncate table Salaries;
insert into Salaries (employee_id, salary) values ('5', '76071');
insert into Salaries (employee_id, salary) values ('1', '22517');
insert into Salaries (employee_id, salary) values ('4', '63539');

select * from Employees;

select * from Salaries;

select e.employee_id, s.employee_id
from Employees as e
left join Salaries as s on e.employee_id = s.employee_id
union
select e.employee_id,  s.employee_id
from Employees as e
right join Salaries as s on e.employee_id = s.employee_id
where  e.employee_id is null or s.employee_id is null;

select e.employee_id
from Employees as e
left Join Salaries as s on e.employee_id = s.employee_id
where s.salary is null
union
select s.employee_id
from Employees as e
right Join Salaries as s on e.employee_id = s.employee_id
where e.name is null
order by employee_id asc














