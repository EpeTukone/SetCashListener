import postgresql
import postgresql.driver as pg_driver

db = pg_driver.connect(
    user='postgres',
    password='postgres',
    host='192.168.1.222',
    database='set',
    port=5432
    )
cash = db.query("SELECT shop_number, number, trim(fiscalnum), trim(fwversion) FROM cash_cash WHERE status = 'ACTIVE'"
                " ORDER BY shop_number, number ")
count_cash = 0
for i in cash:
    print(str(i))
    count_cash += 1
db.close()
print(count_cash)