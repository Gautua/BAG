import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename
from computation import run
import pandas as pd
import re
from word2number import w2n
import xlrd 
import numbers
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, colors

UPLOAD_FOLDER = 'C:/Users/Rakesh/Desktop/CS Project/App/Upload_Folder'
app = Flask(__name__)
# Setting up where the uploaded files go
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def clear():
    if os.path.exists("C:/Users/Rakesh/Desktop/CS Project/App/Upload_Folder/two.xlsx"):
        os.remove("C:/Users/Rakesh/Desktop/CS Project/App/Upload_Folder/two.xlsx")
    if os.path.exists("C:/Users/Rakesh/Desktop/CS Project/App/final.xlsx"):
        os.remove("C:/Users/Rakesh/Desktop/CS Project/App/final.xlsx")
    if os.path.exists("C:/Users/Rakesh/Downloads/final.xlsx"):
        os.remove("C:/Users/Rakesh/Downloads/final.xlsx")
    if os.path.exists("C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error.txt"):
        os.remove("C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error.txt")
    if os.path.exists("C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error_final.txt"):
        os.remove("C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error_final.txt")
    if os.path.exists("C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error_summary.txt"):
        os.remove("C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error_summary.txt")

@app.route('/')
def Home():
    return render_template('Home_Page.html')



@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    clear()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'excel_file' not in request.files:
            #print('No file part')
            return redirect(request.url)
            return 'No file part!'
        file = request.files['excel_file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            #return redirect(request.url)
            return 'No selected file!'
        if file :
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #return redirect(url_for('uploaded_file',filename=filename))
            missing_values_list = ["n/a", "na", "--","NaN", "nan","-","!","@","#","$","%","^","&","*","?"]
            data_file=pd.read_excel(file)
            run(data_file)
            return send_file(os.path.join('C:/Users/Rakesh/Desktop/CS Project/App/final.xlsx'),as_attachment=True)    
    return render_template("Loading_page.html")
    

@app.route('/Error_Report')
def Error_Report():
    try:

        text = open('C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error_final.txt', 'r+')
        content = text.read()
        text.close()
        Sum=open('C:/Users/Rakesh/Desktop/CS Project/App/Error_Report/Error_summary_final.txt', 'r+')
        summary=Sum.read()
        Sum.close()
        return render_template('Error_Display_Page.html',text=content,summary=summary)
    except:
        return redirect(url_for('upload_file'))

if __name__=='__main__':
    app.run(debug=True)