import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0663e258618e4aa8e').stop()