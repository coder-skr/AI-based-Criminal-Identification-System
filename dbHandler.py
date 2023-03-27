import pymysql

def createDatabase():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS criminal_db")
        print("Database created successfully")
    except:
        print("Error creating database")

    db.close()
    print("Connection closed")

createDatabase()

def createTable():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         database='criminal_db',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS criminaldata (id INT(11) AUTO_INCREMENT PRIMARY KEY,\
                        name VARCHAR(255), father_name VARCHAR(255), mother_name VARCHAR(255),\
                        gender VARCHAR(10), dob DATE, blood_group VARCHAR(5), id_mark VARCHAR(255),\
                        nationality VARCHAR(50), religion VARCHAR(50), crimes VARCHAR(255))")
        print("Table created successfully")
    except:
        print("Error creating table")

    db.close()
    print("Connection closed")

createTable()

def insertData(data):
    rowId = 0

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         database='criminal_db',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()
    print("Database connected")

    query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
             data["Nationality"], data["Religion"], data["Crimes Done"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("Data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")

    db.close()
    print("Connection closed")
    return rowId

def retrieveData(name):
    id = None
    crim_data = None

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         database='criminal_db',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()
    print("Database connected")

    query = "SELECT * FROM criminaldata WHERE name='%s'"%name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id=result[0]
        crim_data = {
            "Name" : result[1],
            "Father's Name" : result[2],
            "Mother's Name" : result[3],
            "Gender" : result[4],
            "DOB(yyyy-mm-dd)" : result[5],
            "Blood Group" : result[6],
            "Identification Mark" : result[7],
            "Nationality" : result[8],
            "Religion" : result[9],
            "Crimes Done" : result[10]
        }

        print("Data retrieved")
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("Connection closed")

    return (id, crim_data)
