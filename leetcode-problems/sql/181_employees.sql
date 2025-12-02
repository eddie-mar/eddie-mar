with mngr_salary as (
    select e.name, e.salary, m.salary as manager_salary
    from employee e inner join employee m
    on e.managerID = m.id
)
select name as Employee from mngr_salary
where salary > manager_salary;



select e.name as Employee
from employee e inner join employee m
on e.managerID = m.id
where e.salary > m.salary;