from pyspark import SparkContext
import shutil
import os

sc = SparkContext("local", "EmployeeRDDProject")

lines = sc.textFile("data/employees.csv")

header = lines.first()

employees = lines.filter(lambda x: x != header)

employees_rdd = employees.map(lambda x: x.split(","))

sorted_employees = employees_rdd.sortBy(
    lambda x: int(x[3]),
    ascending=False
)

print("\n===== Employees Sorted by Salary =====")

for emp in sorted_employees.collect():
    print(emp)

dept_salary = (
    employees_rdd
    .map(lambda x: (x[2], int(x[3])))
    .reduceByKey(lambda a, b: a + b)
)

print("\n===== Department Salary Totals =====")

for dept in dept_salary.collect():
    print(dept)

top3 = sorted_employees.take(3)

output_path = "output/top3_employees"

if os.path.exists(output_path):
    shutil.rmtree(output_path)

top3_rdd = sc.parallelize(
    [",".join(emp) for emp in top3]
)

top3_rdd.saveAsTextFile(output_path)

print(f"\nTop 3 employees saved to {output_path}")

sc.stop()