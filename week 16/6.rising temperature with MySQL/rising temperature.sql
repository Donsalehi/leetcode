use exercise;

Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30');
insert into Weather (id, recordDate, temperature) values ('5', '2015-01-06', '35');

select * from Weather;

# method 1
select w1.id
from Weather as w1
join Weather as w2 on date_sub(w1.recordDate, interval 1 day) = w2.recordDate
where w1.temperature > w2.temperature;

# method 2
select w1.id
from Weather as w1
join Weather as w2 on w1.recordDate = w2.recordDAte + interval 1 day
where w1.temperature > w2.temperature;