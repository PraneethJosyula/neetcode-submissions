-- Write your query below
with cte as(
  select user_id, time_stamp,
  rank() over(partition by user_id 
  order by time_stamp desc) as rnk
  from logins
  where time_stamp >= '2020-01-01' and time_stamp <= '2021-01-01'
)

select user_id, time_stamp as last_stamp
from cte 
where rnk =1;