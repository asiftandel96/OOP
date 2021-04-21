
import sqlite3

class DataBaseOperations:

    def __init__(self, databasename):

        self.databasename = databasename

    def createDatabase(self):
        try:
            conn = sqlite3.connect(self.databasename)
        except ConnectionError:
            raise ConnectionError
        return conn

    def createTable(self, tablename, dictionaryOfcolumnNamesAndcolumnDatatypes):
        try:
            conn = self.createDatabase()
            c = conn.cursor()
            for key in dictionaryOfcolumnNamesAndcolumnDatatypes.keys():
                datatype = dictionaryOfcolumnNamesAndcolumnDatatypes[key]
                try:
                    conn.execute(
                        'ALTER TABLE {tableName} ADD COLUMN "{column_name}" {dataType}'.format(tableName=tablename,
                                                                                               column_name=key,
                                                                                               dataType=datatype))
                except:
                    conn.execute('CREATE TABLE {tableName} ({column_name} {dataType})'.format(tableName=tablename,
                                                                                              column_name=key,
                                                                                              dataType=datatype))
            print("Table {0} created in database {1}".format(tablename, self.databasename))
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
        except Exception as e:
            conn.rollback()
            self.closeDbConnection(conn)
            print("Connection to database closed!!")

            print("Exception occured: " + str(e))

    def insertIntoTable(self, tablename, listOfvaluesToInsert):
        try:
            conn = self.createDatabase()
            conn.execute(
                'INSERT INTO {tablename}  values ({values})'.format(tablename=tablename, values=(listOfvaluesToInsert)))
            conn.commit()
            print("Values Inserted Successfully!!!")
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
        except Exception as e:
            conn.rollback()
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
            print("Error occured: " + str(e))

        # self.closeDbconnection()

    def selectFromTable(self, tablename):

        try:
            conn = self.createDatabase()
            c = conn.cursor()
            c.execute("SELECT *  FROM {table}".format(table=tablename))
            print("values in table : ", c.fetchall())
            self.closeDbConnection(conn)
            print("Connection to database closed!!")

        except Exception as e:
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
            print("Error occured: " + str(e))

    def closeDbConnection(self, connection):

        connection.close()


# creating an object of class databaseOperations
db = DataBaseOperations("test9")

# creating database
db.createDatabase()

tableDetails = {"studentId": "INTEGER", "studentRoll": "INTEGER", "studentMarks": "FLOAT"}

db.createTable("table9", tableDetails)

valuesToisnert = ('1,1,97')

db.insertIntoTable("table9", valuesToisnert)

db.selectFromTable("table9")

class StudentMarks(DataBaseOperations):

    def __init__(self, ID, RollNumber, Marks):
        self.ID = ID
        self.RollNumber = RollNumber
        self.Marks = Marks
        self.databasename = "Student Details"


student = StudentMarks(23, 34, 76)

student.createDatabase()

tableDetails = {"studentID": "Integer", "studentRoll": "Integer", "StudentMarks": "Float"}

student.createTable("StudentMarks", tableDetails)

valuesToInsert = ("{0},{1},{2}".format(student.ID, student.RollNumber, student.Marks))

student.insertIntoTable("StudentMarks", valuesToInsert)

student.selectFromTable("StudentMarks")




