USE Exercise;

Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int, PRIMARY KEY(sale_id, year));
Create table If Not Exists Product (product_id int PRIMARY KEY, product_name varchar(10));
Truncate table Sales;
insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000');
Truncate table Product;
insert into Product (product_id, product_name) values ('100', 'Nokia');
insert into Product (product_id, product_name) values ('200', 'Apple');
insert into Product (product_id, product_name) values ('300', 'Samsung');

SELECT * FROM Sales;

SELECT * FROM Product;

SELECT product_name, year, price
FROM Sales AS s
LEFT JOIN Product AS p
ON s.product_id = p.product_id;