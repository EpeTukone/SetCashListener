import postgresql
import postgresql.driver as pg_driver

db = pg_driver.connect(
    user='postgres',
    password='postgres',
    host='192.168.1.253',
    database='set',
    port=5432
    )
cash = db.query("SELECT shop_number, number, trim(fiscalnum) FROM cash_cash WHERE status = 'ACTIVE'"
                " ORDER BY shop_number, number ")
for i in cash:
    print(str(i))
db.close()