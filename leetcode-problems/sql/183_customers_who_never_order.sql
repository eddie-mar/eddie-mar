select name as Customers
from Customers 
where id not in (
    select distinct customerId
    from Orders
);

select c.name as Customers
from Customers c left join Orders o
on c.id = o.customerId
where o.id is Null;