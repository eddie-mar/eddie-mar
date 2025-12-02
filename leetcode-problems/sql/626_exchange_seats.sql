with max_seat as (
    select max(id) as max_id from seat
),
e as (
    select s.id, s.student, 
    case 
        when s.id = m.max_id and s.id % 2 = 1 then s.id
        when s.id % 2 = 1 then s.id + 1
        else s.id - 1
    end as new_id
    from seat s 
    cross join max_seat m
)
select new_id as id, student
from e
order by id;