FROM apache/spark:3.4.0

WORKDIR /app

ENV PATH="$PATH:/opt/spark/bin"
ENV PATH="$PATH:/app/sql_scripts"

# PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_NAME=mydb
ENV DB_USER=postgres
ENV DB_PASSWORD=mypassword
ENV TABLE=users
ENV DATA_PATH=data/data.csv
ENV SAVE_DIR=result

COPY . .

CMD ["bash"]