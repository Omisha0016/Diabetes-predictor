from flask import Flask, render_template, request
import pickle 
import numpy as np
import smtplib


#Initialize the flask App
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    name = request.form['name']
    email = request.form['email']
    #int_features = [float(x) for x in request.form.values()]
    #print(int_features)
    data1 = request.form['preg']
    data2 = request.form['glucose']
    data3 = request.form['BP']
    data4 = request.form['ST']
    data5 = request.form['insulin']
    data6 = request.form['BMI']
    data7 = request.form['DPF']
    data8 = request.form['age']
    final_features = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    #final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)
    print(prediction)
    output = '{0:.{1}f}'.format(10*prediction[0][1],2)
    if output>str(5):
        predictText = "You are at high risk {}".format(output)
    else:
        predictText = "You are at low risk {}".format(output)
    
    SUBJECT = 'This is subject of the email'
    TEXT = name + ", " + predictText + "\nHope you will take care of yourself"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("Diadictor@gmail.com", "Alpha@123")
    server.sendmail("Diadictor@gmail.com", email, message)
   
    if output>str(5):
        return render_template('result.html', output = predictText)
    else:
        return render_template('result.html', output = predictText)
    
    
#    mail.send_message('New Message, Test', 
#                      sender='thesocialtrail85@gmail.com', 
#                      recipients = 'guptabakul21@gmail.com' ,
#                      body = predict_text + "\n" + "Hope you are in pink of your health"
#                    )

if __name__ == "__main__":
    app.run(debug = True)