-- Write your MySQL query statement below
WITH date_ranked as (
    SELECT player_id,
    event_date,
    ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
    FROM Activity
)
SELECT player_id, event_date as first_login
FROM date_ranked 
WHERE rn = 1;


SELECT player_id, min(event_date) as first_login
FROM Activity 
GROUP BY player_id;