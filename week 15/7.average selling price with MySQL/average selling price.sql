use exercise;

Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int, primary key(product_id, start_date, end_date));
Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);
Truncate table Prices;
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');
insert into Prices (product_id, start_date, end_date, price) values ('3', '2019-02-21', '2019-03-31', '10');
Truncate table UnitsSold;
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-23', '20');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');

select * from Prices;

select * from UnitsSold;

select p.product_id, ifnull(round(sum(us.units * p.price) / sum(us.units), 2), 0) as average_price
from Prices as p
left Join UnitsSold as us
	on p.product_id = us.product_id
    and us.purchase_date between p.start_date and end_date
group by p.product_id;