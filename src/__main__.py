from .spark_session import create_SparkSession

def main():
    spark = create_SparkSession()

if __name__ == '__main__':
    main()