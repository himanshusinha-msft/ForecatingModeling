# Databricks notebook source
# DBTITLE 1,Connectting to the Blob storage to read the CSV file with the Historical data
import pandas as pd
from prophet import Prophet
# fit the model to historical data
dbutils.fs.mount(source = "wasbs://himanshu@analyticssharedblob.blob.core.windows.net/"
                 ,mount_point = "/mnt/ThreadData"
                 ,extra_configs = {"fs.azure.sas.himanshu.analyticssharedblob.blob.core.windows.net":dbutils.secrets.get(scope = 'SASKey', key = 'accesskey')})
df = spark.read.csv("/mnt/ThreadData/ThreadCount_Monthly.csv",header="True")


# COMMAND ----------

# DBTITLE 1,The prophet ML package expects the data to be in two columns ds ( data type datetime) and y ( data type int )
pd_df = df.toPandas()
pd_df['ds'] = pd.to_datetime(pd_df['ds'])
pd_df['y']=pd_df['y'].astype(str).astype(int)
pd_df1 =pd_df[['ds','y']]


# COMMAND ----------

# DBTITLE 1,Feeding the package with the historical data
m = Prophet(interval_width=0.95, daily_seasonality=False)
model = m.fit(pd_df1)


# COMMAND ----------

# DBTITLE 1,Getting the forecast for the next 12 months
future = m.make_future_dataframe(periods=12,freq='M')


# COMMAND ----------

# DBTITLE 1,Creating the visualization
forecast = m.predict(future)
plot1 = m.plot(forecast)


# COMMAND ----------

# DBTITLE 1,UnMountaing the file syetm 
dbutils.fs.unmount("/mnt/ThreadData")

# COMMAND ----------


