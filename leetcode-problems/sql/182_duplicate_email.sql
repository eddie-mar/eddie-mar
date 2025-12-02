with duplicate as (
    select email, 
    row_number() over (partition by email) as rn
    from Person
)
select distinct email as Email
from duplicate
where rn > 1;


select email as Email from Person
group by email having count(email) > 1;