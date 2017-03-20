import xlrd
import sqlite3

excel=xlrd.open_workbook("example.xlsx")

print excel.sheets()[1].name

table=excel.sheets()[1]

conn=sqlite3.connect('z.db')
cursor = conn.cursor()
cursor.execute('create table %s (%s %s primary key)' % (table.name,table.row_values(0)[0],table.row_values(1)[0]))

for (key1,key2) in (table.row_values(0)[1:],table.row)values(1)[1:]):
    cursor.execute('alter table %s add column %s %s ' % (table.name,key1,key2))

