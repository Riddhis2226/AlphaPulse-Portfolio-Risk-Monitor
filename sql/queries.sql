-- 1. DAILY PRICE CHANGE (WINDOW FUNCTION)
SELECT 
    Date,
    Stock,
    Price,
    Price - LAG(Price) OVER (
        PARTITION BY Stock 
        ORDER BY Date
    ) AS Daily_Change
FROM stock_prices;
-- 2. MOVING AVERAGE (30-DAY)
SELECT 
    Date,
    Stock,
    AVG(Price) OVER (
        PARTITION BY Stock 
        ORDER BY Date 
        ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
    ) AS Moving_Avg_30
FROM stock_prices;
-- 3. TOP PERFORMING STOCK
SELECT 
    Stock,
    AVG(Price) AS Avg_Price
FROM stock_prices
GROUP BY Stock
ORDER BY Avg_Price DESC;
-- 4. DAILY RANKING OF STOCKS
SELECT 
    Date,
    Stock,
    Price,
    RANK() OVER (
        PARTITION BY Date 
        ORDER BY Price DESC
    ) AS Rank
FROM stock_prices;
-- 5. VOLATILITY APPROX (STD DEV)
SELECT 
    Stock,
    AVG(Price) AS Mean_Price,
    SUM((Price - AVG(Price)) * (Price - AVG(Price))) / COUNT(*) AS Variance
FROM stock_prices
GROUP BY Stock;
