from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession \
    .builder \
    .appName("test") \
    .config("spark.some.config.option", "setting") \
    .getOrCreate()

train = spark.read.csv('data_csv/presences.csv', header=True, inferSchema=True)

a = train.groupBy("aula", "sede", "polo").count().collect()
print(len(a))

data = train.filter(train['aula'] == '1').filter(train['sede'] == '1').filter(train['polo'] == '1')


data = data.withColumn('id', F.monotonically_increasing_id())

data = data.select(F.date_format('date', 'yyyy/MM/dd').alias('date'))
data = data.groupBy(data.date).agg(F.count('date').alias('amount')).sort('date')
data.toPandas().to_csv('data_csv/timeseries3.csv')
data.show()
