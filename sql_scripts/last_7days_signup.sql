-- Retrieve the details of users whose `signup_date` is within the last 7 days.
SELECT * FROM users 
WHERE signup_date >= CURRENT_DATE - INTERVAL '7 days';