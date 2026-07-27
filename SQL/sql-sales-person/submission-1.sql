-- Write your query below
SELECT
   s.name
FROM 
    sales_person s
LEFT JOIN orders o
    ON o.sales_id = s.sales_id
LEFT JOIN company c
    ON c.com_id = o.com_id
    AND c.name = 'CRIMSON'
GROUP BY s.sales_id
HAVING SUM(CASE WHEN c.name IS NULL THEN 0 ELSE 1 END) = 0