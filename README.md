第一步就是，把glue script https://github.com/BestGigaCat/airflow/blob/master/glue/glue_etl.py copy到任意一个S3路径里，但是记住这个路径，之后需要再你的airflow DAG里修改。

第二步，把我的airflow github弄到local一个path，然后创建一个venv（virtual python environment），然后再这里python版本我用的是3.8还是3.7应该都行。然后安装Requirements.txt  https://github.com/BestGigaCat/airflow/blob/master/requirements.txt 就直接pip install -r requirements.txt。这样环境就配置好了。

第三步，确定你的AWS local credential配置好，同时设置airflow的connection。点击admin -> connection，然后设置aws_default的connection，login是你的从你IAM里面拿下来的aws_access_key_id，然后密码是aws_secret_access_key。

第四步，把你的glue路径在本地airflow配置好，主要是这两行 https://github.com/BestGigaCat/airflow/blob/master/dags/config.py#L13 和 https://github.com/BestGigaCat/airflow/blob/master/dags/config.py#L14

第五步，是博客里有提到的，你要把customer-churn.csv 复制到任何一个S3 路径下。https://github.com/aws-samples/amazon-mwaa-examples/tree/main/dags/xgboost-ml-pipeline#setup 

第六步，创建两个路径，一个存储training data，一个存储validation data （glue会负责帮你准备好data），把这两个S3路径配置在 https://github.com/BestGigaCat/airflow/blob/master/dags/config.py#L19 和 https://github.com/BestGigaCat/airflow/blob/master/dags/config.py#L20

第七步，设置一个你希望存储模型的位置，创建S3路径，配置在这一行 https://github.com/BestGigaCat/airflow/blob/master/dags/config.py#L24

第八步，DAG和airflow应该都没问题了，然后如果你没有airflow 创建db，就是没有运行这行代码， airflow db init 运行这行代码。

第九步，在一个界面运行 airflow scheduler，在另一个Terminal 界面（新开一个）运行airflow webserver，实际设置airflow的在第一堂课的博客链接里有讲，https://towardsdatascience.com/an-introduction-to-apache-airflow-21111bf98c1f 我就是跟着这个设置和启动的。Airflow启动完毕。

第十步，进入http://localhost:8080/ 也就是本地的airflow用户管理界面，尝试运行你的DAG，如果顺利的话就都绿了。



