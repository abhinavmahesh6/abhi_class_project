Logging into github
-------------------
Go to www.github.com
If you do not have a github id, create one
Then you can either download the code or clone the project. 
For cloning the project, you need to install git client on your laptop.

Setting up project
--------------------
You can setup all the source code as follows:
1. Create workspace directory under C:\
cd\
mkdir workspace

2. Extract the abhi_class_project.zip file into abhi_class_project folder under c:\workspace

3. If you have git client, you can do
cd\workspace
git clone https://github.com/abhinavmahesh6/abhi_class_project.git

mysql Setting
---------------------
Add this to your environment variable PATH:
C:\Program Files\MySQL\MySQL Workbench 8.0 CE
Then mysql will run from command prompt.

If the above directory does not exist, search for mysql in Windows 10 Search bar and then do "Open file Location" to get the file locations.

To add to environment variable, type environment in windows 10 search box and click on "Edit system environment variables".
Then click on Environment Variables, locate PATH and then add the mysql location to PATH.


Logging into mysql
----------------------
mysql --local-infile -u root -p
<password to be entered>

Create database and global setting in mysql
--------------------------
If project database does not exist, run this command
create database project;

Then, to open the project
use project;

To create tables and load data
---------------------------------
source C:\workspace\abhi_class_project\data\setup_tables_and_data.sql
-- Change the file path if it is different in your machine


To load data separately
--------------------------
You have to now setup the global variables
SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = true;

Load data
----------
load data local infile 'c:/workspace/abhi_class_project/data/aeroplane2.csv' into table aeroplane
fields terminated by ',' enclosed by '"' lines terminated by '\r\n'
(Plane_ID, Company, Type, Place_of_Departure, Destination, Time_of_Dep, Duration);

load data local infile 'C:/workspace/abhi_class_project/mysql/aeroplane_cost.csv' into table aeroplane_cost
fields terminated by ',' enclosed by '"'
lines terminated by '\r\n'
(Plane_ID, Class, Cost);

Exporting data from mysql
---------------------------
You have to disable secure-file-prev in my.ini
Location of my.ini: C:\ProgramData\MySQL\MySQL Server 8.0\my.ini
Comment out original line and make it a space like this:
Comment this out: secure-file-priv="C:/ProgramData/MySQL/MySQL Server 8.0/Uploads"
Include this: secure-file-priv=""
You have to restart mysql after doing this change.

Then open database:
use project

Now run this command:
SELECT * FROM aeroplane 
INTO OUTFILE 'c:\\workspace\\abhi_class_project\\data\\aeroplane.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

SELECT * FROM aeroplane_cost
INTO OUTFILE 'c:\\workspace\\abhi_class_project\\data\\aeroplane_cost.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

How to export only table structure from mysql (no data)
mysqldump -d -u root -p<pwd> -h localhost project > c:\temp\table_structure.txt

How to export table structure and data from mysql (remove the -d option)
mysqldump -u root -p<pwd> -h localhost project > c:\workspace\abhi_class_project\data\setup_tables_and_data.sql
