import mysql.connector
class BloodAddReadRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",
                                        password="root",
                                        host="localhost",
                                        database="blood_db")
        self.cursor=self.con.cursor()
    def add(self,name,blood_group,phone,city,last_donation):
        query="insert into donor(name,blood_group , phone,city,last_donation ) values(%s,%s,%s,%s,%s)"
        data=(name ,blood_group , phone,city,last_donation)
        self.cursor.execute(query,data)
        self.con.commit()
        print("Data Added Successfully")
    def read(self):
        query="select* from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            return records
        else:
            return False
    def retrieve(self,id):
        query="select* from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        records=self.cursor.fetchone()
        if records:
            return records
        else:
            return False
    def update(self,id,name ,blood_group , phone,city,last_donation):
        query="update donor set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data=(name,blood_group ,phone,city,last_donation,id)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False
    def delete(self,id):
        query="delete from donor where id=%s";
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False
#b=BloodAddReadRetrieveUpdateDelete()
#b.add("Fathima","O+ve","7556889934","Mumbai","2024-12-26")
# b.read()
# b.retrieve()
# b.update()
#b.delete(5)

    

     





