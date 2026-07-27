-- Write your query below
select s.seller_name from seller s where s.seller_id not in (
    select seller_id from orders o where extract(year from sale_date) = 2020
)order by s.seller_name ;