SELECT
    "Product Name",
    SUM(Profit) AS total_profit
FROM ecommerce_sales_data
GROUP BY "Product Name"
ORDER BY total_profit DESC
LIMIT 10;
