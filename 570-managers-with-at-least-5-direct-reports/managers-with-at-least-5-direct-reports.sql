# Write your MySQL query statement below
with cte as (
select e1.managerId,count(*) as cn from employee e1, employee e2 where e1.managerId = e2.id  group by e1.managerId
 having cn> 4)
 select e.name from cte c join employee e on c.managerId = e.id