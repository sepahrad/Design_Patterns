# In programming, we create a Base Interface (using the ABC or Abstract Base Class module) to set a strict "contract" 
# for any future database we might add.
# Without it, your Factory is like a wild west where every database might use different names for the same action 
# (one uses .connect(), another uses .open_connection(), another uses .start()).

from abc import ABC, abstractmethod

# The base Interface for the Factory Method
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL Database"
    
class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL Database"
    
class DatabaseFactory:
    @staticmethod
    def get_database(db_type):
        databases = {
            "MySQL": MySQLDatabase,
            "PostgreSQL": PostgreSQLDatabase
        }
        
        db_class = databases.get(db_type)

        if db_class:
            return db_class()
        
        raise ValueError(f"Unknown database type: {db_type}")

# Client code
if __name__ == "__main__":
    database = DatabaseFactory.get_database("MySQL")
    print(database.connect())

    database = DatabaseFactory.get_database("PostgreSQL")
    print(database.connect())