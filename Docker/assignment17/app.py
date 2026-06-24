from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesDataFrameProject") \
    .getOrCreate()

df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("\n===== Products Sorted By Sales =====")

sorted_df = df.orderBy(
    col("sales").desc()
)

sorted_df.show()

print("\n===== Top 3 Products =====")

top3 = sorted_df.limit(3)

top3.show()

print("\n===== Products With Sales Greater Than 80000 =====")

high_sales = df.filter(
    col("sales") > 80000
)

high_sales.show()

high_sales.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/high_sales_products")

print("Filtered data saved successfully!")

spark.stop()