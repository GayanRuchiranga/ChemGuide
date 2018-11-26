import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="",
                           db="chem_guide")

    c = conn.cursor()

    return c, conn
