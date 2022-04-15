# Databricks notebook source
# TODO

dbutils.widgets.text("n_estimators", "100")
dbutils.widgets.text("learning_rate", ".1")
dbutils.widgets.text("max_depth", "1")

# COMMAND ----------

# TODO
n_estimators = int(dbutils.widgets.get("n_estimators").strip())
learning_rate = float(dbutils.widgets.get("learning_rate").strip())
max_depth = int(dbutils.widgets.get("max_depth").strip())

# COMMAND ----------

# TODO
Train and log the results from a model.  Try using Gradient Boosted Trees
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor

# COMMAND ----------

# TODO
Report the model output path to the parent notebook


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>
