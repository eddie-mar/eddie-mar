-- Write your MySQL query statement below
with distinct_city as (
    select lat, lon
    from insurance
    group by lat, lon
    having count(*) = 1
),
same_2015 as (
    select tiv_2015
    from Insurance 
    group by tiv_2015 
    having count(*) > 1
)
select round(sum(tiv_2016), 2) as tiv_2016
from Insurance
where tiv_2015 in (
    select tiv_2015 from same_2015
) and 
(lat, lon) in (
    select lat, lon from distinct_city
)

