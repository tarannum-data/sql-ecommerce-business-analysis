SELECT
    Category,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM ecommerce_sales_data
GROUP BY Category
ORDER BY total_sales DESC;
