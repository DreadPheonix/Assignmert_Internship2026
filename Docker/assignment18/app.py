from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PartitionManagement") \
    .getOrCreate()

df = spark.range(5000000)

print("\n===== Initial Partitions =====")
print(df.rdd.getNumPartitions())

df_repartitioned = df.repartition(12)

print("\n===== Partitions After Repartition =====")
print(df_repartitioned.rdd.getNumPartitions())

df_coalesced = df_repartitioned.coalesce(3)

print("\n===== Partitions After Coalesce =====")
print(df_coalesced.rdd.getNumPartitions())

spark.stop()