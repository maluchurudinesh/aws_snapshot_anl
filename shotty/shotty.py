import boto3

#session = boto3.Session(profile = 'dinesh-amaze')
session = boto3.Session(profile_name = 'dinesh-amaze')
ec2 = session.resource('ec2')
for i in ec2.instances.all():
    print(i)