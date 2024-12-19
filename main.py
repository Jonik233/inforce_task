import os
from pyspark.sql import SparkSession
from etl import extract, transform, load

def main():
    data_path = os.environ['DATA_PATH']
    save_dir = os.environ['SAVE_DIR']
    
    spark = SparkSession.builder.getOrCreate()
    df = extract(spark, data_path)
    df = transform(df)
    df.coalesce(1).write.mode("overwrite").format("csv").option("header", "true").save(save_dir)
    spark.stop()

    # Loading transformed data into database
    load()


if __name__ == "__main__":
    main()