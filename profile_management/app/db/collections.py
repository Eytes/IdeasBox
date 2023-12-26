from pymongo import MongoClient
# from pymongo.collection import Collection

_client = MongoClient(
    'mongodb://mongo:27017/',
    UuidRepresentation='standard',  # чтобы uuid генерировалось синхронизировано с python
)  # cluster

# TODO: подключиться к базе данных IdeasBox
# TODO: создать коллекции в IdeasBox через Dockerfile
# TODO: создать переменные Collection для более удобного дальнейшего взаимодействия с IdeasBox
