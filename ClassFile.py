import sqlite3


class Database:
    def __init__(self,exampledata):
        self.con = sqlite3.connect(exampledata)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS customer(id integer PRIMARY KEY, fname txext, lname text, city text, tel integer)")
        self.con.commit()
    
    def insert(self,fname,lname,city,tel):
        self.cur.execute("""INSERT INTO customer VALUES(NULL, ?, ?, ?, ?)""",(fname,lname,city,tel))
        self.con.commit()


    def show(self):
        self.cur.execute("SELECT * FROM customer")
        self.records = self.cur.fetchall()

        for self.field in self.records:
            self.datafromdatabase = (f"{self.field[0]}\t\t,{self.field[1]}\t\t,{self.field[2]}\t\t,{self.field[3]}\t\t,{self.field[4]}")
        
        return self.datafromdatabase
    
    
    def showinlistbox(self):
        self.cur.execute("SELECT * FROM customer")
        self.allpeopleindatabase = self.cur.fetchall()
        return f"{self.allpeopleindatabase}"
        

    def remove(self,id):
        self.cur.execute("DELETE FROM customer WHERE id = ?", (id,))
        self.con.commit()