# Project-Children_Bedtime_Stories_Search_Engine

## **Introduction**
-	Objective: this project aims to design an all-round children’s bedtime story search system to storage and retrieve 20.5MB of bedtime story txt file;
-	Process: used Postgres SQL to storage data effectively; processed story contents with Spark; designed a user-friendly webpage based on HTML;
-	Established a Flask framework to connect to Postgres SQL; read and processed data through Spark to improve the overall functionality of the search engine;

## **Important**
*This project requires Docker and pgAdmin

## **How To Open**
- Download all files;
- Open your Docker and pgAdmin;
- Run code Spark-JSON.ipynb first. **It will convert the original data into jason file.
- Then, run Postgre_query.ipynb. **It will automatically create a database in your pgAdmin and store the data into the database.
- Finally, run main.ipynb. **Create a HTML Website enable to retrive and search stories from the database.
