import sqlite3
from datetime import datetime
import os

currentPath = os.path.dirname(os.path.abspath(__file__))
class EstateDB:
    def __init__(self):
        # SQLite database file
        db_path = currentPath + '/estates.db'
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # Access rows as dictionaries
        self.cursor = self.conn.cursor()

        # SQL to create estates table
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS estates (
            estateId TEXT PRIMARY KEY NOT NULL,
            price REAL NOT NULL,
            transactionDate TEXT NOT NULL,
            type TEXT NOT NULL,
            area TEXT NOT NULL,
            state TEXT NOT NULL,
            residenceName TEXT NOT NULL
        )
        '''
        try:
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            print("Table 'estates' created successfully.")
        except sqlite3.Error as e:
            print(f"Database error during table creation: {e}")
            self.conn.rollback()
    
    def createEstate(self, estateObj):
        """Insert a new estate into the database."""
        sql = '''INSERT INTO estates (estateId, type, state, area, price, transactionDate, residenceName) 
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''
        try:
            self.cursor.execute(sql, estateObj)
            self.conn.commit()
            return estateObj[0]  # Return created estate ID
        except sqlite3.Error as e:
            print(f"Database error during createEstate: {e}")
            self.conn.rollback()
            return False

    def updateEstate(self, estateObj):
        """Update the amount of an existing estate by estateId."""
        sql = '''UPDATE estates
                 SET type = ?, state=?, area=?, price=?, transactionDate=?, residenceName=?
                 WHERE estateId = ?'''
        try:
            self.cursor.execute(sql, (estateObj['type'], estateObj['state'], estateObj['area'], estateObj['price'], estateObj['transactionDate'], estateObj['residenceName']))
            self.conn.commit()
            return self.cursor.rowcount  # Number of rows affected
        except sqlite3.Error as e:
            print(f"Database error during updateEstate: {e}")
            self.conn.rollback()
            return False

    def getAllEstate(self):
        try:
            sql = '''SELECT * FROM estates'''
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            if not rows:
                return None

            # Convert rows to a list of dictionaries with ISO 8601 timestamp strings
            estates = []
            for row in rows:
                row_dict = dict(row)
                estates.append(row_dict)
            sorted_rows = sorted(rows, key=lambda row: datetime.strptime(row['transactionDate'], "%d/%m/%Y"))
            return sorted_rows
        except sqlite3.Error as e:
            print(f"Database error during getEstate: {e}")
            return False
        
    def getEstate(self, state=None, residenceName=None, estate_type=None, date_range=None, price_range=None):
        """
        Fetch estates based on dynamic filters: state, residenceName, type, transactionDate range, and price range.
        
        Parameters:
        - state: Filter by state name
        - residenceName: Filter by residence name
        - estate_type: Filter by type ("Rent" or "Resale")
        - date_range: Tuple (start_date, end_date) in "DD/MM/YYYY" format
        - price_range: Tuple (min_price, max_price)
        
        Returns:
        - List of filtered estates or None if no records match
        """
        try:
            # Start SQL query and parameters list
            sql = "SELECT * FROM estates WHERE 1=1"
            params = []

            # Dynamic conditions based on provided filters
            if state:
                sql += " AND state = ?"
                params.append(state)
            
            if residenceName:
                sql += " AND residenceName = ?"
                params.append(residenceName)
            
            if estate_type:
                sql += " AND type = ?"
                params.append(estate_type)
            
            # Handle date range
            if date_range:
                start_date, end_date = date_range
                try:
                    # Convert dates from DD/MM/YYYY to YYYY-MM-DD format
                    # start_date = datetime.strptime(start_date, "%d/%m/%Y").strftime("%Y-%m-%d")
                    # end_date = datetime.strptime(end_date, "%d/%m/%Y").strftime("%Y-%m-%d")
                    sql += " AND (SUBSTR(transactionDate, 7, 4) || '-' || SUBSTR(transactionDate, 4, 2) || '-' || SUBSTR(transactionDate, 1, 2)) BETWEEN ? AND ?"
                    params.extend([start_date, end_date])
                except ValueError:
                    print("Date format error. Ensure dates are in DD/MM/YYYY format.")
                    return None
            
            # Handle price range
            if price_range:
                min_price, max_price = price_range
                sql += " AND price BETWEEN ? AND ?"
                params.append(min_price)
                params.append(max_price)
            
            # Execute the query
            self.cursor.execute(sql, tuple(params))
            rows = self.cursor.fetchall()

            # If no rows found, return None
            if not rows:
                return None

            # Convert rows to a list of dictionaries
            estates = []
            for row in rows:
                row_dict = dict(row)
                estates.append(row_dict)
            sorted_rows = sorted(rows, key=lambda row: datetime.strptime(row['transactionDate'], "%d/%m/%Y"))

            return sorted_rows
        
        except sqlite3.Error as e:
            print(f"Database error during getEstate: {e}")
            return False

    def deleteEstate(self, estateId):
        """Delete an estate by estateId."""
        sql = '''DELETE FROM estates WHERE estateId = ?'''
        try:
            self.cursor.execute(sql, (estateId,))
            self.conn.commit()
            return self.cursor.rowcount  # Number of rows affected
        except sqlite3.Error as e:
            print(f"Database error during deleteEstate: {e}")
            self.conn.rollback()
            return False

    def close(self):
        """Close the database connection."""
        self.cursor.close()
        self.conn.close()
