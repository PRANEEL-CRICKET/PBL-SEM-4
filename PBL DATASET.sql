-- ============================================
-- 🏥 CREATE DATABASE
-- ============================================
CREATE DATABASE IF NOT EXISTS health_tracking_system;
USE health_tracking_system;

-- ============================================
-- 🧹 DROP TABLES (CLEAN START)
-- ============================================
DROP TABLE IF EXISTS activity_data;
DROP TABLE IF EXISTS heart_data;
DROP TABLE IF EXISTS mood_data;
DROP TABLE IF EXISTS phone_usage_data;
DROP TABLE IF EXISTS sleep_data;
DROP TABLE IF EXISTS users;

-- ============================================
-- 👤 USERS TABLE
-- ============================================
CREATE TABLE users (
    user_id INT PRIMARY KEY,    
    user_names VARCHAR(100),
    email VARCHAR(150),
    user_password VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ============================================
-- 🚶 ACTIVITY DATA
-- ============================================
CREATE TABLE activity_data (
    activity_id INT PRIMARY KEY,    
    user_id INT,
    recorded_at DATETIME,
    steps INT,
    calories INT,                   
    distance FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================
-- ❤️ HEART DATA
-- ============================================
CREATE TABLE heart_data (
    heart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    recorded_at DATETIME,
    heart_rate INT,
    max_heart_rate INT,
    min_heart_rate INT,
    heart_rate_variability FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================
-- 😊 MOOD DATA
-- ============================================
CREATE TABLE mood_data (
    mood_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    recorded_at DATETIME,
    mood_rating INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================
-- 📱 PHONE USAGE DATA
-- ============================================
CREATE TABLE phone_usage_data (
    usage_id INT PRIMARY KEY,    
    user_id INT,
    recorded_at DATETIME,
    screen_time FLOAT,           
    app_usage_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================
-- 😴 SLEEP DATA (FIXED 🔥)
-- ============================================
CREATE TABLE sleep_data (
    sleep_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,

    sleep_start DATETIME,
    sleep_end DATETIME,

    total_sleep_hours FLOAT,   -- ✅ ADDED (ONLY CHANGE)

    sleep_efficiency FLOAT,
    movement_level FLOAT,
    sleep_rating INT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================
-- 📊 VIEWS (UNCHANGED)
-- ============================================

CREATE OR REPLACE VIEW v_user_activity_summary AS
SELECT 
    u.user_id,
    u.user_names,
    COUNT(a.activity_id) AS total_sessions,
    SUM(a.steps) AS total_steps,
    AVG(a.steps) AS avg_steps,
    SUM(a.calories) AS total_calories,
    SUM(a.distance) AS total_distance
FROM users u
LEFT JOIN activity_data a ON u.user_id = a.user_id
GROUP BY u.user_id, u.user_names;

CREATE OR REPLACE VIEW v_user_health_summary AS
SELECT 
    u.user_id,
    u.user_names,
    u.age,
    u.gender,
    AVG(h.heart_rate) AS avg_heart_rate,
    AVG(m.mood_rating) AS avg_mood,
    AVG(s.sleep_rating) AS avg_sleep_rating,
    AVG(TIMESTAMPDIFF(MINUTE, s.sleep_start, s.sleep_end)/60) AS avg_sleep_hours
FROM users u
LEFT JOIN heart_data h ON u.user_id = h.user_id
LEFT JOIN mood_data m ON u.user_id = m.user_id
LEFT JOIN sleep_data s ON u.user_id = s.user_id
GROUP BY u.user_id, u.user_names;

SELECT*FROM activity_data;
SELECT*FROM heart_data;
SELECT*FROM mood_data;
SELECT*FROM phone_usage_data;
SELECT*FROM sleep_data;
SELECT*FROM users;

CREATE OR REPLACE VIEW v_user_overview AS
SELECT 
    u.user_id,
    u.user_names,
    u.age,
    u.gender,
    COUNT(a.activity_id) AS total_activity_sessions,
    SUM(a.steps) AS total_steps,
    AVG(a.steps) AS avg_steps
FROM users u
LEFT JOIN activity_data a ON u.user_id = a.user_id
GROUP BY u.user_id;

CREATE OR REPLACE VIEW v_activity_summary AS
SELECT 
    user_id,
    COUNT(*) AS sessions,
    SUM(steps) AS total_steps,
    AVG(steps) AS avg_steps,
    SUM(calories) AS total_calories,
    SUM(distance) AS total_distance
FROM activity_data
GROUP BY user_id;

CREATE OR REPLACE VIEW v_heart_summary AS
SELECT 
    user_id,
    AVG(heart_rate) AS avg_heart_rate,
    MAX(max_heart_rate) AS peak_heart_rate,
    MIN(min_heart_rate) AS lowest_heart_rate,
    AVG(heart_rate_variability) AS avg_hrv
FROM heart_data
GROUP BY user_id;

CREATE OR REPLACE VIEW v_mood_summary AS
SELECT 
    user_id,
    AVG(mood_rating) AS avg_mood,
    MIN(mood_rating) AS lowest_mood,
    MAX(mood_rating) AS highest_mood
FROM mood_data
GROUP BY user_id;

CREATE OR REPLACE VIEW v_sleep_summary AS
SELECT 
    user_id,
    AVG(TIMESTAMPDIFF(MINUTE, sleep_start, sleep_end)/60) AS avg_sleep_hours,
    AVG(sleep_efficiency) AS avg_efficiency,
    AVG(movement_level) AS avg_movement,
    AVG(sleep_rating) AS avg_sleep_rating
FROM sleep_data
GROUP BY user_id;

CREATE OR REPLACE VIEW v_phone_usage_summary AS
SELECT 
    user_id,
    AVG(screen_time) AS avg_screen_time,
    AVG(app_usage_time) AS avg_app_usage,
    MAX(screen_time) AS max_screen_time
FROM phone_usage_data
GROUP BY user_id;

CREATE OR REPLACE VIEW v_full_health_dashboard AS
SELECT 
    u.user_id,
    u.user_names,

    AVG(a.steps) AS avg_steps,
    AVG(a.calories) AS avg_calories,

    AVG(h.heart_rate) AS avg_heart_rate,

    AVG(m.mood_rating) AS avg_mood,

    AVG(TIMESTAMPDIFF(MINUTE, s.sleep_start, s.sleep_end)/60) AS avg_sleep_hours,
    AVG(s.sleep_rating) AS avg_sleep_rating,

    AVG(p.screen_time) AS avg_screen_time

FROM users u
LEFT JOIN activity_data a ON u.user_id = a.user_id
LEFT JOIN heart_data h ON u.user_id = h.user_id
LEFT JOIN mood_data m ON u.user_id = m.user_id
LEFT JOIN sleep_data s ON u.user_id = s.user_id
LEFT JOIN phone_usage_data p ON u.user_id = p.user_id

GROUP BY u.user_id;

CREATE OR REPLACE VIEW v_sleep_mood_correlation AS
SELECT 
    s.user_id,
    AVG(TIMESTAMPDIFF(MINUTE, s.sleep_start, s.sleep_end)/60) AS avg_sleep,
    AVG(m.mood_rating) AS avg_mood
FROM sleep_data s
JOIN mood_data m ON s.user_id = m.user_id
GROUP BY s.user_id;

CREATE OR REPLACE VIEW v_screen_sleep_analysis AS
SELECT 
    p.user_id,
    AVG(p.screen_time) AS avg_screen_time,
    AVG(TIMESTAMPDIFF(MINUTE, s.sleep_start, s.sleep_end)/60) AS avg_sleep
FROM phone_usage_data p
JOIN sleep_data s ON p.user_id = s.user_id
GROUP BY p.user_id;

CREATE OR REPLACE VIEW v_activity_levels AS
SELECT 
    user_id,
    AVG(steps) AS avg_steps,
    CASE 
        WHEN AVG(steps) > 10000 THEN 'Active'
        WHEN AVG(steps) BETWEEN 5000 AND 10000 THEN 'Moderate'
        ELSE 'Low Activity'
    END AS activity_level
FROM activity_data
GROUP BY user_id;

CREATE OR REPLACE VIEW v_heart_risk AS
SELECT 
    user_id,
    AVG(heart_rate) AS avg_hr,
    CASE 
        WHEN AVG(heart_rate) > 100 THEN 'High Risk'
        WHEN AVG(heart_rate) < 60 THEN 'Low'
        ELSE 'Normal'
    END AS heart_status
FROM heart_data
GROUP BY user_id;

