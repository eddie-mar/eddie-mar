with ranked as (
    select e.id, e.name, e.salary, d.name as department,
    rank() over (partition by d.name order by e.salary desc) as rn
    from Employee e inner join Department d
    on e.departmentID = d.id
)
select department as Department, name as Employee, salary as Salary
from ranked
where rn = 1