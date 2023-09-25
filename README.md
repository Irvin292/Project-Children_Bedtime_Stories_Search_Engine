# Project-Children_Bedtime_Stories_Search_Engine

## **Introduction**
-	Objective: this project aims to design an all-round children’s bedtime story search system to storage and retrieve 20.5MB of bedtime story txt file;
-	Process: used Postgres SQL to storage data effectively; processed story contents with Spark; designed a user-friendly webpage based on HTML;
-	Established a Flask framework to connect to Postgres SQL; read and processed data through Spark to improve the overall functionality of the search engine;

## **Important**
*This project requires Docker and pgAdmin

## **How To Open**
1. Download all files, including folders.

2. Open Docker and pgAdmin.

3. Begin by executing the Spark-JSON.ipynb code; it will convert the original data into a JSON file.

4. Next, run the Postgre_query.ipynb script, which will automatically establish a connection to your default PostgreSQL database, creating a new database and initiating queries.

5. Lastly, execute the main.ipynb script to create an HTML website that enables you to retrieve and search stories from the database.
