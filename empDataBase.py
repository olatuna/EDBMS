import sqlite3


def employee_data():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS employee(
              id INTEGER PRIMARY KEY,
              empID text,
              firstname text,
              lastname text,
              dob text,
              age text,
              gender text,
              address text,
              mobile text,
              )""")
    c.commit()
    c.close()

def add_emp_rec(empID, firstname, lastname, dob, age, gender, address, mobile):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    c.execute("INSERT INTO employee VALUES(NULL, ?,?,?,?,?,?,?,?", (empID, firstname, lastname, dob, age, gender, address, mobile))
    c.commit()
    c.close()

def view_data():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    c.execute("SELECT * FROM employee")
    rows = c.fetchall()
    c.close()
    return rows

def delete_rec(id):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    c.execute("DELETE FROM employee WHERE id=?", (id,))
    c.commit()
    c.close()

def search(empID="", firstname="", lastname="", dob="", age="", gender="", address="", mobile=""):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    c.execute("SELECT * FROM employee WHERE empID=? OR firstname=? OR lastname=? OR dob=? OR age=? OR gender=? OR address=? OR \
              mobile=? ", (empID, firstname, lastname, dob, age, gender, address, mobile))
    rows = c.fetchall()
    c.close()
    return rows

def update(id,empID="", firstname="", lastname="", dob="", age="", gender="", address="", mobile=""):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    c.execute("UPDATE employee SET empID=?, firstname=?, lastname=?,dob=?, age=?, gender=?, address=?, \
                  mobile=?, WHERE id=?", (empID, firstname, lastname, dob, age, gender, address, mobile, id))
    rows = c.fetchall()
    c.commit()
    c.close()





