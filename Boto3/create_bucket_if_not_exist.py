"""
## Run the Program like Below
## python create_bucket_if_not_exist.py <Bucket_Name> <Region>
## Ex :
       python create_bucket_if_not_exist.py anand-839-babu ap-south-1
"""


import boto3
from pprint import pprint
from botocore.exceptions import ClientError
import logging
import sys


def create_bucket(bucket_name, region=None):
    try:
        if bucket_name in list_of_buckets:
            print("Bucket '{}' already Exits !!".format(bucket_name))
        else:
            if region is None:
                session = boto3.session.Session()
                s3_cli = session.client('s3')
                s3_cli.create_bucket(Bucket=bucket_name)
                print("Bucket '{}' Created Successfully !!".format(bucket_name))
            else:
                session = boto3.session.Session(region_name=region)
                s3_cli = session.client('s3')
                location = {'LocationConstraint': region}
                s3_cli.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
                print("Bucket '{}' Created Successfully !!".format(bucket_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True


# With Client Object
session = boto3.session.Session()
s3_cli = session.client('s3')
buckets = s3_cli.list_buckets()
list_of_buckets = []
for bucket in buckets['Buckets']:
    list_of_buckets.append(bucket['Name'])

# Create Bucket
create_bucket(sys.argv[1], sys.argv[2])
# print("List of Exist Buckets are : ", list_of_buckets)


#
# # # with Resource Object
# # s3_res = session.resource('s3')
# # for bucket in s3_res.buckets.all():
# #     print(bucket.name)
#
# # #With Client Object
# # session = boto3.session.Session()
# # s3_cli = session.client('s3')
# # buckets = s3_cli.list_buckets()
# # for bucket in buckets['Buckets']:
# #     print(bucket['Name'])


# import logging
# import boto3
# from botocore.exceptions import ClientError
#
#
# def create_bucket(bucket_name, region=None):
#     """Create an S3 bucket in a specified region
#
#     If a region is not specified, the bucket is created in the S3 default
#     region (us-east-1).
#
#     :param bucket_name: Bucket to create
#     :param region: String region to create bucket in, e.g., 'us-west-2'
#     :return: True if bucket created, else False
#     """
#
#     # Create bucket
#     try:
#         if region is None:
#             s3_client = boto3.client('s3')
#             s3_client.create_bucket(Bucket=bucket_name)
#         else:
#             s3_client = boto3.client('s3', region_name=region)
#             location = {'LocationConstraint': region}
#             s3_client.create_bucket(Bucket=bucket_name,
#                                     CreateBucketConfiguration=location)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True
#
#
# create_bucket("anand-839-babu","ap-south-1")
