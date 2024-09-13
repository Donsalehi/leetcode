use exercise;

Create table If Not Exists Department (id int, revenue int, month varchar(5), primary key(id, month));
Truncate table Department;
insert into Department (id, revenue, month) values ('1', '8000', 'Jan');
insert into Department (id, revenue, month) values ('2', '9000', 'Jan');
insert into Department (id, revenue, month) values ('3', '10000', 'Feb');
insert into Department (id, revenue, month) values ('1', '7000', 'Feb');
insert into Department (id, revenue, month) values ('1', '6000', 'Mar');

select * from Department;

select
	id,
	max(case when month = 'Jan' then revenue end) as Jan_revenue,
    max(case when month = 'Feb' then revenue end) as Feb_revenue,
    max(case when month = 'Mar' then revenue end) as Mar_revenue,
    max(case when month = 'Apr' then revenue end) as Apr_revenue,
    max(case when month = 'May' then revenue end) as May_revenue,
    max(case when month = 'Jun' then revenue end) as Jun_revenue,
    max(case when month = 'Jul' then revenue end) as Jul_revenue,
    max(case when month = 'Aug' then revenue end) as Aug_revenue,
    max(case when month = 'Sep' then revenue end) as Sep_revenue,
    max(case when month = 'Oct' then revenue end) as Oct_revenue,
    max(case when month = 'Nov' then revenue end) as Nov_revenue,
    max(case when month = 'Dec' then revenue end) as Dec_revenue
from Department
group by id;