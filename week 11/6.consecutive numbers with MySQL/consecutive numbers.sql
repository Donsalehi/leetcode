use exercise;

Create table If Not Exists Logs (id int, num int);
Truncate table Logs;
insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');
insert into Logs (id, num) values ('8', '1');

select * from Logs;

SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.Num = l2.Num
JOIN Logs l3 ON l1.Num = l3.Num
where l2.id - l1.id = l3.id - l2.id
AND l2.Id > l1.Id
AND l3.Id > l2.Id;

# ----------------------------------------------------------------------------------------------------------------------------

select distinct l1.num as ConsecutiveNums
from Logs as l1
inner join Logs as l2 on l1.id + 1 = l2.id
inner join Logs as l3 on l2.id + 1 = l3.id
where l2.num = l3.num and l1.num = l2.num











