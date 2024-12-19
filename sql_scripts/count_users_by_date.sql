-- Retrieve the count of users who signed up on each day
SELECT signup_date, COUNT(*) AS user_count 
FROM users 
-- Group the results by the 'signup_date' to count users per day
GROUP BY signup_date;