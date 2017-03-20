import xlrd
import sqlite3
import zDatabase


excel=xlrd.open_workbook("example.xlsx")

table=excel.sheets()[1]
rcol=table.ncols
rown=table.nrows

print (rown,rcol)

for table in excel.sheets():
    print table.name
    a=zDatabase.zDatabase()
    a.Create("abc.db",table)



