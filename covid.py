import sqlite3 
from sqlite3 import error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    try:
        serve = [
            """"CREATE TABLE hospital (
                h_name char(32) NOT NULL,
                h_doctors decimal (8,0) NOT NULL,
                h_patients decimal (8,0) NOT NULL,
                h_riskLevel decimal (1,0) NOT NULL,
                h_address char (32) NOT NULL,
                h_comments varchar (128) NOT NULL
            );""",
            """CREATE TABLE NeedsHospital (
                nh_address char(32) NOT NULL,
                nh_riskLevel decimal(1,0) NOT NULL,
                nh_fever char(8) NOT NULL,
                nh_tiredness char(8) NOT NULL,
                nh_dryCough char(8) NOT NULL,
                nh_breathingDifficulty char(8) NOT NULL,
                nh_soreThroat char(8) NOT NULL,
                nh_severity decimal(1, 0) NOT NULL,
                nh_decision char(8) NOT NULL
            );""",
            """"CREATE TABLE Symptoms (
                s_caseID decimal(8,0) NOT NULL,
                s_fever char(8) NOT NULL,
                s_tiredness char(8) NOT NULL,
                s_dryCough char(8) NOT NULL,
                s_breathingDifficulty char(8) NOT NULL,
                s_soreThroat char(8) NOT NULL,
                s_severity decimal(1,0) NOT NULL
            );""",
            """CREATE TABLE Outcome (
                o_caseID decimal(8,0) NOT NULL,
                o_dayspositive decimal(4,0) NOT NULL,
                o_status char(16) NOT NULL,
                o_comments varchar(128) NOT NULL
            );""",
            """CREATE TABLE TestingAvailability (
                ta_personID decimal(8,0) NOT NULL,
                ta_type char(16) NOT NULL,
                ta_units decimal(12,0) NOT NULL,
                ta_givenTest char(8) NOT NULL,
                ta_comment varchar(128) NOT NULL
            );""",
            """CREATE TABLE Testing (
                t_type char(16) NOT NULL,
                t_units decimal(12,0) NOT NULL,
                t_requests decimal(12,0) NOT NULL
            );""",
            """CREATE TABLE Results (
                r_caseID decimal(8,0) NOT NULL,
                r_personID decimal(8,0) NOT NULL,
                r_date date NOT NULL,
                r_result char(16) NOT NULL
            );""",
            """CREATE TABLE Person (
                p_ID decimal(8,0) NOT NULL,
                p_name char(32) NOT NULL,
                p_address char(32) NOT NULL,
                p_dob date NOT NULL,
                p_comment varchar(128)
            );""",
            """CREATE TABLE Location (
                l_city char(32) NOT NULL,
                l_country char(32) NOT NULL,
                l_state char(32) NOT NULL,
                l_lockdown char(8)
            );"""
        ]
        for i in serve:
            sql = i
            _conn.execute(sql)

            _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("DROP TABLE")
    try:
        serve = [
            "DROP TABLE hospital;",
            "DROP TABLE NeedsHospital;",
            "DROP TABLE Symptoms;",
            "DROP TABLE Outcome;",
            "DROP TABLE TestingAvailability;",
            "DROP TABLE Testing;",
            "DROP TABLE Results;",
            "DROP TABLE Person;",
            "DROP TABLE Location;"]
        for i in serve:
            sql = i
            _conn.execute(sql)
            _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Table")
    try:
        hospital = []
        Location = []
        NeedsHospital = []
        Outcome = []
        Person = []
        Results = []
        Symptoms = []
        Testing = []
        TestingAvailability = []


        sql = "INSERT INTO hospital VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, hospital)

        sql = "INSERT INTO Location VALUES(?, ?, ?, ?)"
        _conn.executemany(sql, Location)

        sql = "INSERT INTO NeedsHospital VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, NeedsHospital)

        sql = "INSERT INTO Outcome VALUES(?, ?, ?, ?)"
        _conn.executemany(sql, Outcome)

        sql = "INSERT INTO Person VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, Person)

        sql = "INSERT INTO Results VALUES(?, ?, ?, ?)"
        _conn.executemany(sql, Results)

        sql = "INSERT INTO Symptoms VALUES(?, ?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, Symptoms)

        sql = "INSERT INTO Testing VALUES(?, ?, ?)"
        _conn.executemany(sql, Testing)

        sql = "INSERT INTO TestingAvailability VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, TestingAvailability)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")



def makeOutcome(_conn, o_caseID = "", o_status = ""):

    print("++++++++++++++++++++++++++++++++++")
    print("make Outcome")


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def makePerson(_conn, p_ID = "", p_name = ""):

    print("++++++++++++++++++++++++++++++++++")
    print("make Person")


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def makeResults(_conn, r_caseID = "", r_personID = "")

    print("++++++++++++++++++++++++++++++++++")
    print("make Results")


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")


def makeSymptoms(_conn, s_caseID = "")

    print("++++++++++++++++++++++++++++++++++")
    print("make Symptoms")


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")


def makeTestingAvailability(_conn, ta_personID = "", ta_type = "")

    print("++++++++++++++++++++++++++++++++++")
    print("make TestingAvailability")


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")


def setOutcome(_conn, o_caseID, o_status):

    print("++++++++++++++++++++++++++++++++++")
    print("set Outcome")
    try:
        """ UPDATE results
        SET o_caseID = ?,
        """
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def setPerson(_conn, p_ID = "", p_name = ""):

    print("++++++++++++++++++++++++++++++++++")
    print("set Person")
     try:
        """ UPDATE results
        SET p_ID = ?,
        """
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def setResults(_conn, r_caseID = "", r_personID = "")

    print("++++++++++++++++++++++++++++++++++")
    print("set Results")
     try:
        """ UPDATE results
        SET r_caseID = ?,
        """
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")


def setSymptoms(_conn, s_caseID = "")

    print("++++++++++++++++++++++++++++++++++")
    print("set Symptoms")
     try:
        """ UPDATE results
        SET s_caseID = ?,
        """
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")


def setTestingAvailability(_conn, ta_personID = "", ta_type = "")

    print("++++++++++++++++++++++++++++++++++")
    print("make TestingAvailability")
     try:
        """ UPDATE results
        SET ta_personID = ?,
        """
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)


    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")








        


