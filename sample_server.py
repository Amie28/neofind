from flask import Flask,render_template,request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/index.html")
def hello_world1():
    return render_template("index.html")


@app.route("/<string:file_name>")
def global_function(file_name):
    return render_template(file_name)

@app.route("/submit_form",methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv(data)
        return redirect("/thank-you.html")
    else:
        return "Invalid Action!!!"

def write_csv(data):
    with open('database.csv', newline='',mode ='a') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
        csv_write = csv_file.writerow([email,subject,message])  
'''
def write_file(data):
    with open("./database.txt",mode = "a+") as database:
        email = data['email']
        subject = data['subject']
        message = data['message'] 
        file = database.write(f'\n{email},{subject},{message}')  




@app.route("/templates/left-sidebar.html")
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route("/templates/right-sidebar.html")
def right_sidebar():
    return render_template("right-sidebar.html")

@app.route("/templates/no-sidebar.html")
def no_sidebar():
    return render_template("no-sidebar.html")
'''