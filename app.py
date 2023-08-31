from flask import Flask,render_template,request,redirect,url_for
import mysql.connector
app=Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="coderprem",
  database="studentdatabase"
)
mycursor = mydb.cursor()

@app.route('/',methods=["get","post"])
def home():
    mycursor = mydb.cursor()
    sql = "select id,student_name,student_class,section,academic_year from studentinfo"
    mycursor.execute(sql)
    students = mycursor.fetchall()
    sql2 = "SELECT count(id),COUNT(CASE WHEN gender = 'male' THEN 1 END) AS male,COUNT(CASE WHEN gender = 'female' THEN 1 END) AS female FROM studentinfo"
    mycursor.execute(sql2)
    count = mycursor.fetchall()

    return render_template("Dashboard.html",students=students,count=count)

@app.route('/dashboard')
def dash():
    return render_template("Dashboard.html")
@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/contact')
def con():
    return render_template("contact.html")

@app.route('/view')
def view():
    return render_template("view.html")

@app.route('/edit/<string:id>',methods=["GET","POST"])
def edit(id):
    if request.method=="POST":
        name = request.form['sname']
        class1 = request.form['stc']
        dob = request.form['dob']
        acy = request.form['acy']
        father = request.form['fan']
        mother = request.form['mon']
        parentphone = request.form['pcn']
        address = request.form['addr']
        gender = request.form.get('gender')
        section = request.form.get('section')
        mycursor = mydb.cursor()
        sql = "update studentinfo set student_name=%s,student_class=%s,father_name=%s,mother_name=%s,parent_contact_number=%s,address=%s,date_of_birth=%s,gender=%s,section=%s,academic_year=%s where id=%s"
        val = (name, class1, father, mother, parentphone, address, dob, gender, section, acy,id)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for("home"))
    mycursor = mydb.cursor()
    sql = "select student_name,student_class,section,gender,date_of_birth,mother_name,father_name,parent_contact_number,academic_year,address from studentinfo where id=%s"
    val = (id,)
    mycursor.execute(sql,val)
    students = mycursor.fetchone()
    return render_template("edit.html", student=students)

@app.route('/delete<string:id>',methods=["get","post"])
def delete(id):
    sql = "delete from studentinfo where id=%s"
    val=(id,)
    mycursor.execute(sql,val)
    mydb.commit()
    return redirect(url_for("home"))

@app.route('/view3<string:id>',methods=["get","post"])
def view3(id):

    sql = "select student_name,student_class,section,gender,date_of_birth,mother_name,father_name,parent_contact_number,academic_year,address,id from studentinfo where id=%s"
    val = (id,)
    mycursor.execute(sql, val)
    students=mycursor.fetchall()
    mydb.commit()
    return render_template("view.html",students=students)


@app.route('/view2',methods=["get","post"])
def view2():
    name = request.form['name']
    std = request.form['stc']
    section = request.form['section']
    sql = "select student_name,student_class,section,gender,date_of_birth,mother_name,father_name,parent_contact_number,academic_year,address,id from studentinfo where student_name=%s and student_class=%s and section=%s"
    val = (name,std,section)
    mycursor.execute(sql, val)
    students=mycursor.fetchall()
    mydb.commit()
    print(students)

    if not students:
        message = "Please Enter correct Details!"
        return render_template("view.html", students=students, message=message)
    else:
        message="Scroll down to see Student Details!"
        return render_template("view.html", students=students, message=message)

@app.route('/savedetails',methods=["get","post"])
def sd():
    name = request.form['sname']
    class1 = request.form['stc']
    dob = request.form['dob']
    acy = request.form['acy']
    father = request.form['fan']
    mother = request.form['mon']
    parentphone = request.form['pcn']
    address = request.form['addr']
    gender = request.form.get('gender')
    section = request.form.get('section')
    mycursor = mydb.cursor()
    sql = "insert into studentinfo(student_name,student_class,father_name,mother_name,parent_contact_number,address,date_of_birth,gender,section,academic_year) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name, class1, father, mother, parentphone, address, dob, gender, section, acy)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True,port=5000)