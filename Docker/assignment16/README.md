# Employee PySpark RDD Assignment

## Objective

Process employee data using PySpark RDDs.

## Operations

1. Sort employees by salary descending
2. Calculate total salary department-wise
3. Save top 3 highest-paid employees

## Project Structure

assignment1/
│
├── data/
│   └── employees.csv
│
├── output/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

## Build Docker Image

docker build -t assignment16 .

## Run Docker Container

docker run assignment16

## Output

Top 3 employees are stored inside:

output/top3_employees