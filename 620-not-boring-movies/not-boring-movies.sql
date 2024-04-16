# Write your MySQL query statement below
with cte as(
select * , case when id%2 !=0 then 1 else 0 end as flag from cinema)
select id, movie, description, rating from cte where flag = 1 and description <> 'boring' order by rating desc