from abc import ABC, abstractmethod

class DataStorageSystem(ABC):
    @abstractmethod
    def save(self, key, data):
        pass

    @abstractmethod
    def load(self, key):
        pass

    @abstractmethod
    def delete(self, key):
        pass

class FileStorage(DataStorageSystem):
    def save(self, key, data):
        with open(key, 'w') as file:
            file.write(data)

    def load(self, key):
        with open(key, 'r') as file:
            data = file.read()
        return data

    def delete(self, key):
        import os
        os.remove(key)


class DatabaseStorage(DataStorageSystem):
    def __init__(self):
        self._db = {}

    def save(self, key, data):
        self._db[key] = data

    def load(self, key):
        return self._db[key]

    def delete(self, key):
        del self._db[key]