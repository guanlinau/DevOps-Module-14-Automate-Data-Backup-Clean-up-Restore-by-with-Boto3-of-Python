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

2-Tag one of two EC2 instance as Name: production

###### Step 2: Install boto3 and schedule library

1-Create the requirement.txt file with boto3 and schedule version
```
pip freeze > requirements.txt
```

2-Install boto3 and schedule library
```
pip install -r requirements.txt
```