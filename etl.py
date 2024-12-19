import os
import glob
import psycopg2
import pandas as pd
from io import StringIO
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType


def extract(spark_session:SparkSession, data_path:str) -> DataFrame:
    schema = StructType([
        StructField("user_id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("email", StringType(), True),
        StructField("signup_date", TimestampType(), True)
    ])
    
    df = spark_session.read.format("csv").option("header", "true").schema(schema).load(data_path)
    return df


def transform(df:DataFrame) -> DataFrame:
    # Dropping email duplicates
    df = df.dropDuplicates(["email"])
    
    # Converting the `signup_date` field to a standard format (`YYYY-MM-DD`).
    df = df.withColumn("signup_date", F.col("signup_date").cast(DateType()))

    # Filtering out invalid emails
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    df_valid = df.filter(F.col("email").rlike(pattern))

    # Creating 'domain' column
    df_valid = df_valid.withColumn("domain", F.split(F.col("email"), "@")[1])
    return df_valid


def load():
    data_dir = os.environ['SAVE_DIR']
    csv_path = glob.glob(os.path.join(data_dir, 'part-00000*.csv')).pop()
    df = pd.read_csv(csv_path)

    conn = psycopg2.connect(
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

    cur = conn.cursor()

    buffer = StringIO()
    df.to_csv(buffer, header=False, index=False)
    buffer.seek(0)

    cur.copy_from(buffer, os.environ['TABLE'], sep=',')
    conn.commit()

    cur.close()
    conn.close()