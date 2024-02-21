import sqlite3


class Database:
    def __init__(self,exampledata):
        self.con = sqlite3.connect(exampledata)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS customer(fname txext, lname text, city text, tel integer)")
        self.con.commit()
    
    def insert(self,fname,lname,city,tel):
        self.cur.execute("""INSERT INTO customer VALUES(?,?,?,?)""",(fname,lname,city,tel))
        self.con.commit()


    def show(self):
        self.cur.execute("SELECT * FROM customer")
        records = self.cur.fetchall()

        for field in records:
            datafromdatabase = (f"{field[0]}\t\t,{field[1]}\t\t,{field[2]}\t\t,{field[3]}\t\t")
        
        return datafromdatabase
        