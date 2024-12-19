CREATE TABLE users (
    -- Unique identifier for each user, automatically incremented
    user_id SERIAL PRIMARY KEY,

    -- Full name of the user, cannot be null
    name VARCHAR(100) NOT NULL,

    -- Email address of the user, must be unique and cannot be null
    email VARCHAR(100) NOT NULL UNIQUE,

    -- Date when the user signed up, automatically set to the current date if not provided
    signup_date DATE NOT NULL DEFAULT CURRENT_DATE,

    -- Domain associated with the user, cannot be null
    domain VARCHAR(100) NOT NULL
);