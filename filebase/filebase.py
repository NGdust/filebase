import os
import boto3
from botocore.client import Config
from google.cloud import storage


class FirebaseTransport:
    def upload(self):
        raise NotImplementedError


class FirebaseStorageTransport(FirebaseTransport):

    def __init__(self, user_email=None, from_filename=None, to_filename=None):
        self.user_email = user_email
        self.to_filename = to_filename
        self.from_filename = from_filename
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config-google.json'
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(os.environ.get('FIREBASE_STORAGE_BUCKET')


    async def upload(self):
        blob = self.bucket.blob(self.user_email + '/' + self.to_filename)
        blob.upload_from_filename(self.from_filename)
        return f"gs://{os.environ.get('FIREBASE_STORAGE_BUCKET')}/{self.user_email}/{self.to_filename}"


class WassabiStorageTransport:
    def __init__(self, user_email=None, from_filename=None):
        self.user_email = user_email
        self.endpoint_url = 'https://s3.us-west-1.wasabisys.com'
        self.from_filename = from_filename
        self.bucket = 'suptitle'
        self.s3 = boto3.resource(
                                    's3',
                                    endpoint_url=self.endpoint_url,
                                    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                                    aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
                                    config=Config(signature_version='s3v4')
                                )


    async def upload(self):
        data = open(self.from_filename, 'rb')
        key_file = self.user_email + '/' + self.from_filename.split('/')[-1]

        self.s3.Bucket(self.bucket).put_object(ACL='public-read', Key=key_file, Body=data)
        return f'https://{self.bucket}.s3.us-west-1.wasabisys.com/{key_file}'


    def list_files(self):
        listObjSummary = self.s3.Bucket(self.bucket).objects.all()
        for obj in listObjSummary:
            print(f'https://{self.bucket}.s3.us-west-1.wasabisys.com/{obj.key}')


    def clear_bucket(self):
        listObjSummary = self.s3.Bucket(self.bucket).objects.all()
        for obj in listObjSummary:
            obj.delete()
            print(f'https://{self.bucket}.s3.us-west-1.wasabisys.com/{obj.key}')

if __name__ == '__main__':
    transport = WassabiStorageTransport(from_filename='1.txt')
    test = transport.list_files()