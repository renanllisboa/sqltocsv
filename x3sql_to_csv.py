import pyodbc
import csv

def x3sql_to_csv():

    connection = pyodbc.connect("DRIVER={SQL Server}; server=SPON010113665; database=P12117MNTDB;uid=sa;pwd=totvs@1234")
    cursor = connection.cursor()
    cursor.execute("select X3_CAMPO, X3_TIPO, X3_TAMANHO, X3_TITULO, X3_TITSPA, X3_TITENG from SX3T10")
    data = cursor.fetchall()

    with open("c:\\temp\\sx3.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        for line in data:
            csv_writer.writerow(line)

    cursor.close()
    connection.close()