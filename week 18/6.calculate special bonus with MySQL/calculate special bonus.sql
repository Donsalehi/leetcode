use exercise;

Create table If Not Exists Employees (employee_id int primary key, name varchar(30), salary int);
Truncate table Employees;
insert into Employees (employee_id, name, salary) values ('3', 'Meir', '3000');
insert into Employees (employee_id, name, salary) values ('2', 'Michael', '3800');
insert into Employees (employee_id, name, salary) values ('7', 'Addilyn', '7400');
insert into Employees (employee_id, name, salary) values ('8', 'Juan', '6100');
insert into Employees (employee_id, name, salary) values ('9', 'Kannon', '7700');

select * from Employees;

SELECT 
    employee_id,
    CASE
        WHEN
            employee_id % 2 = 1
                AND name NOT LIKE 'M%'
        THEN
            salary
        ELSE 0
    END AS bonus
FROM
    Employees
ORDER BY employee_id;