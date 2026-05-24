SELECT
    DATE(order_date) AS order_day,
    SUM(sales) AS total_revenue
FROM ecommerce_sales_data
GROUP BY order_day
ORDER BY order_day;
