use exercise;

Create table If Not Exists Person (id int primary key, email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'a@b.com');
insert into Person (id, email) values ('2', 'b@c.com');
insert into Person (id, email) values ('3', 'a@b.com');

drop table person;

select Email
from PERSON
group by EMAIL
having count(*) > 1;