-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS forex_db;
-- 切换到该数据库
USE forex_db;

-- 创建汇率表（如果不存在）
CREATE TABLE IF NOT EXISTS exchange_rates (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 自增主键ID
    currency_pair VARCHAR(10) NOT NULL,       -- 货币对（如 "USD/CNY"）
    rate DECIMAL(10,4) NOT NULL,              -- 汇率（保留4位小数）
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- 记录时间（默认当前时间）
    UNIQUE KEY unique_rate (currency_pair, DATE(timestamp)) -- 唯一键：同一天同一货币对仅存一条
);