
-- 1. Overall performance by experiment group
SELECT
    "group",
    COUNT(DISTINCT user_id) AS total_users,
    SUM(purchases) AS total_purchases,
    ROUND(
        100.0 * SUM(purchases)
        / COUNT(DISTINCT user_id),
        2
    ) AS conversion_rate_pct,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(AVG(revenue), 2) AS revenue_per_user
FROM ab_test_users
GROUP BY "group";

-- 2. Device-level conversion comparison
SELECT
    device,
    "group",
    COUNT(DISTINCT user_id) AS total_users,
    SUM(purchases) AS purchasers,
    ROUND(100.0 * AVG(purchases), 2)
        AS conversion_rate_pct
FROM ab_test_users
GROUP BY device, "group"
ORDER BY device, "group";

-- 3. Group allocation
SELECT
    "group",
    COUNT(DISTINCT user_id) AS total_users
FROM ab_test_users
GROUP BY "group";

-- 4. Revenue summary
SELECT
    "group",
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(AVG(revenue), 2) AS average_revenue_per_user,
    ROUND(MAX(revenue), 2) AS maximum_user_revenue
FROM ab_test_users
GROUP BY "group";
