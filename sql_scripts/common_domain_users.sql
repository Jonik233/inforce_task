-- Find the user(s) with the most common email domain
SELECT * FROM users 
WHERE domain = (
    -- Subquery to find the most common email domain
    SELECT domain FROM users
    -- Group users by their email domain
    GROUP BY domain
    -- Order the domains by their frequency (count of users) in descending order
    ORDER BY COUNT(*) DESC
    -- Limit the result to the most frequent domain
    LIMIT 1
);