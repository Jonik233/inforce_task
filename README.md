# ETL Application with PostgreSQL Setup

This setup uses Docker Compose to run an ETL application with a PostgreSQL database. The `etl-app` service depends on the `postgres` service and interacts with the database using the environment variables defined in the configuration.

## Steps to Build and Run the Services

1. **Navigate to your project directory** where the `docker-compose.yml` file is located. Open a terminal and run the following command to build and start the services:

    ```bash
    docker-compose up --build

This will:
Build the etl-app container.
Start the postgres container.
Set up the network and volume for the PostgreSQL database.
Link the etl-app container to the postgres container.
Make PostgreSQL accessible on port 5432.


2. **Access the Containers**
After running the docker-compose up command, you can access the etl-container as follows:
    ```bash
    docker exec -it etl-app bash

3. **Generate data**
Using the following command generate a dataset:
    ```bash
    python3 generate.py

    You will be given an option to choose the quantity and level of corruption or leave default values


4. **Create table**
Using the following command connect to the psql:
    ```bash
    psql -h $DB_HOST -U $DB_USER -d $DB_NAME

    Then enter password: mypassword

    Run the following sql script to create a table:
    ```bash
    \i scripts_sql/create_table.sql


5. **Run pyspark script**
    Quit the database using \q
    Using the following command run the spark script:
    ```bash
    spark-submit main.py

    After running it, transformed data will be loaded into the database.
    To run other sql scripts - connect to the database and experiment with data