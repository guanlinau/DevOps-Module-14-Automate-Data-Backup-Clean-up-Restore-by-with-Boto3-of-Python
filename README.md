### Project description
Automate data backup, clean up and restore with boto3 library of python

### Technologies used:
Python, Boto3, AWS, Schedule

### Project Description:
1-Write a Python script that automates creating backups for EC2 Volumes.

2-Write a Python script that cleans up old EC2 Volume snapshots.

3-Write a Python script that restores EC2 Volumes.

### Usage Description

###### Step 1: Create EC2 instance

1-Create two EC2 instance in sydney region via AWS console manually

2-Tag one EC2 instance as Name: production and another one as Name: development

3-Tag one EC2 instance's value as Name: production and another one as Name: development
 
###### Step 2: Install boto3 and schedule library

1-Create the requirement.txt file with boto3 and schedule version
```
pip freeze > requirements.txt
```

2-Install boto3 and schedule library
```
pip install -r requirements.txt
```

###### Step 3: Finish the backup logic function and run the program
```
python ec2-instance-volume-backup.py
```

![image](image/Screenshot%202023-04-15%20at%209.48.55%20pm.png?raw=true)
![image](image/Screenshot%202023-04-15%20at%209.57.11%20pm.png?raw=true)
![image](image/Screenshot%202023-04-15%20at%209.57.33%20pm.png?raw=true)

###### Step4: Finish the clean up logic function and run the program
```
python volume-snapshots-cleanup.py
```
#before cleanup
![image](image/Screenshot%202023-04-16%20at%2011.42.19%20am.png?raw=true)
#after cleanup
![image](image/Screenshot%202023-04-16%20at%2011.42.56%20am.png?raw=true)
###### Step5: Finish the restore logic function and run the program
```
python volume-restore.py
```
#before attach
![image](image/Screenshot%202023-04-16%20at%205.18.21%20pm.png?raw=true)
#after attach
![image](image/Screenshot%202023-04-16%20at%205.18.34%20pm.png?raw=true)