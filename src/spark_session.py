import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env_example'))

def create_Sparksession() -> SparkSession:

    DELTA_SPARK_VERSION = '3.1.0'
    DELTA_PACKAGE_VERSION = f'delta-spark_2.12:{DELTA_SPARK_VERSION}'
    spark = SparkSession.builder \
        .appName("nyann") \
        .config("spark.jars.packages", f"io.delta:{DELTA_PACKAGE_VERSION}") \
        .config("spark.driver.defaultJavaOptions", "-Divy.cache.dir=/tmp -Divy.home=/tmp") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.eventLog.enabled", "true")\
        .config("spark.eventLog.dir", "./Log/spark-logs")\
        .enableHiveSupport() \
        .getOrCreate()

    return spark