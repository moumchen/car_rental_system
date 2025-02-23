import sqlite3
import threading

class DBConnectionManager:
    """
    Database connection manager class, using singleton pattern and supporting connection pool.
    """
    _instance = None
    # Thread lock to ensure thread safety for singleton pattern
    _lock = threading.Lock()

    def __new__(cls, db_path, pool_size=100):
        """
        Singleton pattern implementation to ensure only one instance.
        """
        with cls._lock:
            if not cls._instance:
                cls._instance = super(DBConnectionManager, cls).__new__(cls)
                cls._instance.db_path = db_path
                cls._instance.pool_size = pool_size
                cls._instance._connections = []  # Connection pool list
                cls._instance._available_connections = [] # Available connections list
                cls._instance._init_pool() # Initialize connection pool
        return cls._instance

    def _init_pool(self):
        """
        Initialize the connection pool by pre-creating a specified number of database connections.
        """
        for _ in range(self.pool_size):
            conn = self._create_connection()
            if conn:
                self._connections.append(conn)
                self._available_connections.append(conn)

    def _create_connection(self):
        """
        Create a database connection.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Database connection creation failed: {e}")
            return None

    def acquire_connection(self):
        """
        Acquire a database connection from the connection pool.
        If no available connection and pool is not full, create a new connection
        (connections beyond pool_size will be closed after use and not put back into the pool).
        If the connection pool is full and no available connection, return None.
        """
        if self._available_connections:
            # Return and remove from available connections list
            return self._available_connections.pop(0)
        elif len(self._connections) < self.pool_size:
            # If the connection pool is not full, but no available connection, create a new connection
            conn = self._create_connection()
            if conn:
                self._connections.append(conn) # Newly created connection added to connection pool management
                return conn
            else:
                return None # Connection creation failed
        else:
            print("Connection pool is full, no available connections.")
            return None # Connection pool is full and no available connection

    def release_connection(self, connection):
        """
        Release a database connection, put the connection back into the connection pool for reuse.
        """
        if connection in self._connections and connection not in self._available_connections:
            self._available_connections.append(connection)

    def get_cursor(self):
        """
        Get a cursor, and also return the connection object for subsequent release_connection.
        """
        conn = self.acquire_connection()
        if conn:
            return conn.cursor(), conn
        return None, None

    def close_connection(self, connection):
        """
        Close a database connection (not returning to the connection pool, suitable for connections not managed by the pool, or connections that need to be forcibly closed).
        """
        if connection:
            try:
                connection.close()
            except Exception as e:
                print(f"Error closing connection: {e}")

    def close_all_connections(self):
        """
        Close all database connections in the connection pool.
        """
        for conn in self._connections:
            try:
                conn.close()
            except Exception as e:
                print(f"Error closing connection: {e}")
        self._connections = []
        self._available_connections = []
        DBConnectionManager._instance = None # Reset singleton instance, allowing re-initialization

