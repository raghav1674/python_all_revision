import mysql.connector
def update(id,sal):
    conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='!Raghav.81')

    if conn.is_connected():
        print("connected")
        cur=conn.cursor()
        str="update emp set sal=%d where id=%d"
        args=(sal,id)
# cur.execute("select name from emp where name like'%R%'")
    try:
        cur.execute(str %args)
        print("no. of  rows selected:",cur.rowcount)
        conn.commit()
        print("updated successfully")


    except:
        print("update unsuccessfull")

        conn.rollback()
    else:
        cur.execute("select * from emp")
        row = cur.fetchall()
        for  row in row:
            print(row)

    finally:
        cur.execute("desc emp")
        print("Table description:")
        row =cur.fetchall()
        print(row)
        cur.close()
        conn.close()

id,sal=[int(x) for x in input("id and sal:").split()]
update(id,sal)