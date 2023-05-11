# connector and methods accessing s3

import os
import boto3


class s3BucketConnector():
    # class for interacting with s3 bucket

    def __init__(self, access_key: str, secert_key: str, endpoint_url: str, bucket: str):
        """constructor for s3bucket
        """
        self.access_key = access_key
        self.secert_key = secert_key
        self.endpoint_url = endpoint_url
        self.session = boto3.Session(
            aws_access_key_id=os.environ[access_key], aws_secret_access_key=os.environ[secert_key])

        self._s3 = self.session.resource('s3', endpoint_url=endpoint_url)
        self._bucket = self._s3.Bucket(bucket)

    def list_files_in_prefix(self):
        pass

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass
