FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y default-jdk wget && \
    apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/default-java

ENV SPARK_VERSION=3.5.1

RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop3.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop3 /spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop3.tgz

ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["spark-submit", "app.py"]