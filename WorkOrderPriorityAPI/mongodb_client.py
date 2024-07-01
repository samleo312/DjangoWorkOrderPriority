from pymongo import MongoClient

class MongoDBClient:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBClient, cls).__new__(cls)
            cls._client = MongoClient('mongodb+srv://samleo312:Welcome#312@workorderprioritycluste.mr7w0kg.mongodb.net/?retryWrites=true&w=majority&appName=WorkOrderPriorityCluster')
        return cls._instance

    def get_client(self):
        return self._client

    def get_database(self, db_name='WorkOrderPriorityCluster'):
        return self._client[db_name]

mongodb_client = MongoDBClient()
