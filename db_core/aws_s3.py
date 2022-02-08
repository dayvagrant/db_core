"""
Tools for AWS S3.
"""
import codecs
import logging
import os
import pickle
from dataclasses import dataclass
from io import BytesIO
from typing import Any

from botocore.exceptions import ClientError

from db_core.connections import get_aws_s3_client


@dataclass
class S3ClientTools:
    """
     Client tools for S3 AWS.
    """
    s3_client: Any = None
    if not s3_client:
        s3_client = get_aws_s3_client()

    def download_object(self, bucket_name, object_name):
        """
        Downloads an object from an S3 bucket.
        """
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=object_name)
        except ClientError as err:
            print(err)
            return None
        body = response["Body"].read()
        _bytes = bytearray(codecs.decode(pickle.loads(body), "base64"))
        obj = pickle.loads(_bytes)
        return obj


    def upload_object(self, bucket_name, obj, object_name):
        """
        Uploads an object to an S3 bucket.
        """
        binary = codecs.encode(pickle.dumps(obj), encoding="base64")
        buffer = BytesIO()
        pickle.dump(binary, buffer)
        buffer.seek(0)
        try:
            response = self.s3_client.upload_fileobj(
                buffer, Bucket=bucket_name, Key=object_name
            )
        except ClientError as err:
            print(err)
        return response


    def get_objects_list(self, bucket_name):
        """
        Returns a list with all objects info in a S3 bucket.
        """
        response = self.s3_client.list_objects(Bucket=bucket_name)
        return response["Contents"]

    def download_file_s3(self, bucket_name: str, object_name: str, download_directory: str = None):
        """
        download_file_s3 Download fie from s3 to terget directory.

        :param bucket_name: Bucket name from S3
        :type bucket_name: str
        :param object_name: path to file from S3
        :type object_name: str
        :param download_directory: File path directory,default save to current folder
        :type download_directory: str
        """
        file_name = os.path.split(object_name)[1]
        if not download_directory:
            download_directory = '.'
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        download_path = os.path.join(download_directory, file_name)

        with open(download_path, 'wb') as f:
            try:
                self.s3_client.download_fileobj(bucket_name, object_name, f)
                print('Loading is successful')
                return download_path
            except ClientError as err:
                print(err)

    def upload_file_s3(self, bucket, object_name, file_name):
        """
        upload_file_s3 Upload file to s3 to terget directory.

        :param bucket_name: Bucket name from S3
        :type bucket_name: str
        :param object_name: path to file from S3
        :type object_name: str
        :param file_name: File name
        :type file_name: str
        """
        object_name = os.path.join(object_name, file_name)
        try:
            response = self.s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
