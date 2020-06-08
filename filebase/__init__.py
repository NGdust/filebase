import os

UPLOAD_FOLDER = os.getcwd() + '/transient'  # папка для временно скачанных видео
ALLOWED_EXTENSIONS = ['mp4', 'mov', 'm4v', 'MP4', 'MOV', 'm4v']  # ограничение по расширению
MAX_CONTENT_LENGTH = 1024  # ограничение в мегабайтах

EXCHANGE = ''
QUEUE_EXTRACTOR = 'video'
QUEUE_RECOGNIZE = 'rec'
QUEUE_EDITOR = 'edit'


if 'DEBUG' in os.environ:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@videodb:5432/{}'.format(os.environ.get('v_POSTGRES_USER'),
                                                                          os.environ.get('v_POSTGRES_PASSWORD'),
                                                                          os.environ.get('v_POSTGRES_DB'))

    RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
    RABBITMQ_PORT = 5672
    RABBITMQ_LOGIN = os.environ.get('RABBITMQ_DEFAULT_USER')
    RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_DEFAULT_PASS')

    WEBSOCKET_HOST = os.environ.get('WEBSOCKET_HOST')

    WEBSITE_URL = 'https://index.kvando.tech'
    ENDPOINT = '/video/updata/'

    IP = '0.0.0.0'
    PORT = 6001

else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:nigative32@localhost:5432/video'

    RABBITMQ_HOST = '0.0.0.0'
    RABBITMQ_PORT = 5672
    RABBITMQ_LOGIN = 'rabbitmq'
    RABBITMQ_PASSWORD = 'rabbitmq'

    WEBSOCKET_HOST = 'ws://0.0.0.0:6002/'

    WEBSITE_URL = 'http://0.0.0.0:6001'
    ENDPOINT = '/video/updata/'

    IP = '0.0.0.0'
    PORT = 6002