-- ==========================================
-- AlphaPulse Database Schema
-- ==========================================

CREATE TABLE IF NOT EXISTS stock_prices (
    Date DATE,
    Stock TEXT,
    Price REAL
);
