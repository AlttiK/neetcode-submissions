-- Write your query below
WITH combined AS (
    SELECT 
        c.customer_id AS customer_id,
        c.customer_name AS customer_name,
        o.product_name AS product_name
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
)
(SELECT
    customer_id,
    customer_name
FROM combined
WHERE product_name = 'A'
INTERSECT
SELECT
    customer_id,
    customer_name
FROM combined
WHERE product_name = 'B'
EXCEPT
SELECT
    customer_id,
    customer_name
FROM combined
WHERE product_name = 'C')
ORDER BY customer_name

