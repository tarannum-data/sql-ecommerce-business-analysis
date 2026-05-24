SELECT
    "Product Name",
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM ecommerce_sales_data
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;
