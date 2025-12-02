select name from SalesPerson 
where sales_id not in (
    select sales_id from Orders
    where com_id in (
        select com_id from Company
        where name = 'RED'
    )
);

with p as (
    select s.name,
        sum(case when c.name = 'RED' then 1 else 0 end) as red_hits
    from SalesPerson s
    left join Orders o on s.sales_id = o.sales_id
    left join Company c on o.com_id = c.com_id
    group by s.name
)
select name from p where red_hits = 0;
