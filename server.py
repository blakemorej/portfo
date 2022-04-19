from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/', defaults={'page':None})
@app.route('/<page>')
def html_page(page):
    if page == None: 
        return render_template('index.html')
    else:
        return render_template(page+".html")

def txt_writer(data):
    with open ('database.txt', newline='', mode='a') as database:
        writer = open("database.txt", "a")
        entries = []
        entries.append(data["email"])
        entries.append(data["subject"])
        entries.append(data["message"])
        writer.write('\n'+','.join(entries))

def csv_writer(data):
    with open ('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            csv_writer(data)
            return redirect('/thanks')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'