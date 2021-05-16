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

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/form')
def form():
    return render_template('form.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    name = request.form['name']
    email = request.form['email']
    #int_features = [float(x) for x in request.form.values()]
    #print(int_features)
    data8 = request.form['age']
    data7 = request.form['fnc']
    data1 = request.form['pregnancies']
    data2 = request.form['glucose']
    data3 = request.form['bp']
    data4 = request.form['thick']
    data5 = request.form['insulin']
    data6 = request.form['bmi']
    
    
    final_features = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    #final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)
    print(prediction)
    output = '{0:.{1}f}'.format(10*prediction[0][1],2)
    predictText = "Greetings from DiaDictor\nOn the basis of the information provided by you , our predictor has calculated the risk of you getting diabetes. Rating on scale of 10 you have a rating of {}".format(output)
    if output>str(7):
        content = "We suggest you to get an appointment with a doctor. Our appointment scheduler can help you get an appointment in your city."
    else:
        content = "We suggest you to maintain your health. If in case you want to consult a doctor our appointment scheduler can help you get an appointment in your city."
    
    SUBJECT = 'Reg diabetes prediction by DiaDictor'
    TEXT = predictText + "\n" + content + "For further reference visit our webpage www.abc.com\nThanks\nRegards\nDiadictor team"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("Diadictor@gmail.com", "Alpha@123")
    server.sendmail("Diadictor@gmail.com", email, message)
    
    if output>str(7):
        result_web = "Thank you " + name + " for using our Diabetes predictor.\nOn the basis of the information provided by you\nwe predict that the chances of you having diabetes is {}. We suggest you to consult a doctor".format(output)
    else:
        result_web = "Thank you " + name + " for using our Diabetes predictor.\nOn the basis of the information provided by you\nwe predict that the chances of you having diabetes is {}".format(output)
    
    return render_template('result.html', output = result_web)

if __name__ == "__main__":
    app.run(debug = True, port=8000)
