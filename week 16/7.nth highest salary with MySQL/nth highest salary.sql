use exercise;

CREATE TABLE IF NOT EXISTS Employee (
    Id INT PRIMARY KEY,
    Salary INT
);
Truncate table Employee;
insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');
insert into Employee (id, salary) values ('4', '200');

SELECT * FROM Employee;

SET DELIMITER $$
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN ( with cte as (
                    select *, dense_rank() over(order by salary desc) as r
                    from employee)
            select salary from cte 
            where r = N limit 1
  );
END
SET DELIMITER ;

SELECT getNthHighestSalary(2);