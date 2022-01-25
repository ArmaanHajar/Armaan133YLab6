import pyodbc

class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            cls.__connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

    @classmethod
    def fetch_names(cls, year, gender):
        from Name import Name
        cls.connect()
        cursor = cls.__connection.cursor()

        sql = """
        SELECT TOP 50 NameCount, Name, Year, Gender
        FROM all_data
        WHERE Year = ?
        AND Gender = ?
        ORDER BY NameCount DESC;
        """

        cursor.execute(sql, year, gender)
        names = []
        for row in cursor:
            names.append(Name(row[0], row[1], row[2], row[3]))
        return names