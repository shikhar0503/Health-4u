# importing the necessary tools
from flask import Flask, render_template, request,redirect, url_for, session
# to let flask interact easily while performing file and folder processes irrespective of operating system
import os
import sys
# load the model using joblib
import joblib
import numpy as np
import tensorflow.compat.v2 as tf
# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from tensorflow.keras.utils import load_img

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
# root directory
#webroot = 'src'
#static_dir = os.path.join(webroot,'static')
#template_dir = os.path.join(webroot,'templates')
# defining the flask app
app = Flask(__name__,static_folder='static',template_folder='templates')
# route for home page
@app.route('/')
def home():
    return render_template('index.html')

# route for about section
@app.route('/about')
def about():
    return render_template('about.html')

# Breast Cancer Section
@app.route('/cancer',methods=['GET','POST'])
def cancerhome():
    return render_template('cancer.html')

@app.route('/cancerpredict',methods=['GET','POST'])
def breastcancer():
    cancer_file = "Final_cancer_model.pkl"
    loaded_cancer_model = joblib.load(cancer_file)

    if request.method == "POST":
        try:
           Concave_Points_Mean = float(request.form["concave_points_mean"])
           Area_Mean = float(request.form["area_mean"])
           Radius_Mean = float(request.form["radius_mean"])
           Concavity_Mean = float(request.form["concavity_mean"])
           Perimeter_Mean = float(request.form["perimeter_mean"])


           cancer_pred = loaded_cancer_model.predict([[Radius_Mean, Area_Mean, Concavity_Mean, Concave_Points_Mean, Perimeter_Mean]])
           cancer_pred = round(100*cancer_pred[0])
           if(cancer_pred == 0):
               res = "Congratulations! you have no symptoms of Breast Cancer.Be Happy:)"
           else:
               res = "Sorry! you have symptoms of getting Breast Cancer. Please consult the doctor"
           return render_template('result1.html',prediction=res)


        except Exception as e:
            print(e)
            error=("Please fill all the fields for cancer prediction🤦🤦")
            error={"error":error}
            return render_template("404_error.html",error=error)
    else:
        return render_template('cancer.html')

# Diabetes Section
@app.route('/diabetes',methods=['GET','POST'])
def diabeteshome():
    return render_template('diabetes.html')

@app.route('/diabetespredict',methods=['GET','POST'])
def diabetes():
    diabetes_file = "Final_diabetes_model.pkl"
    loaded_diabetes_model = joblib.load(diabetes_file)

    if request.method == "POST":
        try:
            Pregnancies = float(request.form["Pregnancies"])
            Glucose = float(request.form["Glucose"])
            Bloodpressure = float(request.form["Bloodpressure"])
            BMI = float(request.form["BMI"])
            DiabetesPedigreeFunction = float(request.form["DiabetesPedigreeFunction"])
            Age = float(request.form["Age"])

            diabetes_pred = loaded_diabetes_model.predict([[Pregnancies,Glucose,Bloodpressure,BMI,DiabetesPedigreeFunction,Age]])
            diabetes_pred = round(100*diabetes_pred[0])
            if(diabetes_pred == 0):
                res = "Congratulations! you have no symptoms of Diabetes.Be Happy:)"
            else:
                res = "Sorry! you have symptoms of getting Diabetes. Please consult the doctor"
            return render_template('result2.html',prediction=res)

        except Exception as e:
            print(e)
            error=("Please fill all the fields for diabetes prediction🤦🤦")
            error={"error":error}
            return render_template("404_error.html",error=error)
    else:
        return render_template('diabetes.html')

# Heart Section
@app.route('/heart',methods=['GET','POST'])
def hearthome():
    return render_template('heart.html')

@app.route('/heartpredict',methods=['GET','POST'])
def heart():
    heart_file = "final_model.pkl"
    loaded_heart_model = joblib.load(heart_file)

    if request.method == 'POST':
        try:
            #chest pain
            chestpain = (request.form["chestpain"])
            if(chestpain == "Atypical Angina"):
                chestpain = 1
            elif (chestpain == "Non-Anginal Pain"):
                chestpain = 2
            elif (chestpain == "Typical Angina"):
                chestpain = 0
            else:
                chestpain = 3
            # resting bp
            restingbp = float(request.form["restingbp"])
            cholestrol = float(request.form["cholestrol"])
            fastingbs = float(request.form["fastingbs"])
            if (fastingbs == "Fasting Blood Sugar < 120 mg/dl"):
                fastingbs = 0
            else:
                fastingbs = 1
            restingecg = (request.form["restingecg"])
            if(restingecg == "having ST-T wave abnormality"):
                restingecg = 1
            elif (restingecg == "showing probable or definite left ventricular hypertrophy "):
                restingecg = 2
            else:
                restingecg = 0

            maxhr = float(request.form["maxhr"])
            exercise = (request.form["exercise"])
            if(exercise == "Yes"):
                exercise = 0
            else:
                exercise = 1


            heart_pred = loaded_heart_model.predict([[ chestpain, restingbp, cholestrol, fastingbs, restingecg, maxhr,
            exercise]])

            heart_pred = round(100*heart_pred[0])
            if(heart_pred == 0):
                res = "Congratulations! you have no symptoms of Heart diseases.Be Happy:)"
            else:
                res = "Sorry! you have symptoms of getting Heart diseases. Please consult the doctor"
            return render_template('result3.html',prediction = res)

        except Exception as e:
            print(e)
            error=("Please fill all the fields for heart disease prediction🤦🤦")
            error={"error":error}
            return render_template("404.html",error=error)
    else:
        return render_template('heart.html')

# Kidney Section
@app.route('/kidney',methods=['GET','POST'])
def kidneyhome():
    return render_template('kidney.html')

@app.route('/kidneypredict',methods=['GET','POST'])
def kidney():
    kidney_file = "Final_Kidney_model.pkl"
    loaded_kidney_model = joblib.load(kidney_file)

    if request.method == 'POST':
        try:
            bloodpressure = float(request.form["bloodpressure"])
            specific_gravity= float(request.form["specific_gravity"])
            albumin= float(request.form["specific_gravity"])
            sugar=  float(request.form["sugar"])
            rbc= float(request.form["rbc"])
            pus_cell_count= float(request.form["pus_cell_count"])
            pus_cell_clumps= float(request.form["pus_cell_clumps"])

            kidney_pred = loaded_kidney_model.predict([[ bloodpressure, specific_gravity,albumin,sugar, rbc,pus_cell_count ,pus_cell_clumps
            ]])

            kidney_pred = round(100*kidney_pred[0])
            if(kidney_pred == 0):
                res = "Congratulations! you have no symptoms of Kidney diseases.Be Happy:)"
            else:
                res = "Sorry! you have symptoms of getting Kidney diseases. Please consult the doctor"
            return render_template('result4.html',prediction = res)

        except Exception as e:
            print(e)
            error=("Please fill all the fields for kidney disease prediction🤦🤦")
            error={"error":error}
            return render_template("404_error.html",error=error)
    else:
        return render_template('kidney.html')

# Liver Section
@app.route('/liver',methods=['GET','POST'])
def liverhome():
    return render_template('liver.html')

@app.route('/liverpredict',methods=['GET','POST'])
def liver():
    liver_file = "Final_liver_model.pkl"
    loaded_liver_model = joblib.load(liver_file)

    if request.method == 'POST':
        try:
            total_bilirubin = float(request.form["total_bilirubin"])
            direct_bilirubin= float(request.form["direct_bilirubin"])
            alkaline_phosphotase= float(request.form["alkaline_phosphotase"])
            alamine_aminotransferase=  float(request.form["alamine_aminotransferase"])
            aspartate_aminotransferase= float(request.form["aspartate_aminotransferase"])
            total_proteins= float(request.form["total_proteins"])
            albumin= float(request.form["albumin"])
            albumin_and_globulin_ratio = float(request.form["albumin_and_globulin_ratio"])

            liver_pred = loaded_liver_model.predict([[ total_bilirubin, direct_bilirubin,alkaline_phosphotase,alamine_aminotransferase, aspartate_aminotransferase,total_proteins ,albumin,albumin_and_globulin_ratio
            ]])

            liver_pred = round(100*liver_pred[0])
            if(liver_pred == 0):
                res = "Congratulations! you have no symptoms of Liver diseases.Be Happy:)"
            else:
                res = "Sorry! you have symptoms of getting Liver diseases. Please consult the doctor"
            return render_template('result5.html',prediction = res)

        except Exception as e:
            print(e)
            error=("Please fill all the fields for liver disease prediction🤦🤦")
            error={"error":error}
            return render_template("404_error.html",error=error)
    else:
        return render_template('liver.html')

# Pneumonia Section

# load pneumonia model path
PNEUMONIA_MODEL_PATH = 'pneumonia.h5'

#Load your trained model
model1 = load_model(PNEUMONIA_MODEL_PATH)
# pneumonia detection
def pneumonia_predict(img_path, model1):
    img1 = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224)) #target_size must agree with what the trained model expects!!
    # Preprocessing the image
    img1 = tf.keras.preprocessing.image.img_to_array(img1)
    img1 = np.expand_dims(img1, axis=0)
    preds1 = model1.predict(img1)
    return preds1

@app.route('/pneumonia',methods=['GET','POST'])
def pneumonia():
    if request.method == 'POST':
        try:
            # Get the file from post request
            f = request.files['file']
            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
                basepath, '', secure_filename(f.filename))
            f.save(file_path)
            # Make prediction
            preds1 = pneumonia_predict(file_path, model)
            os.remove(file_path)#removes file from the server after prediction has been returned
            if preds1 == 1:
                res = "Sorry! you have symptoms of getting Pneumonia disease. Please consult the doctor"
            else:
                res = "Congratulations! you have no symptoms of Pneumonia disease.Be Happy:)"
            return render_template('pneumonia.html',prediction=res)
        except Exception as e:
            print(e)
            error=("Have you uploaded the image??🤔🤔")
            error={"error":error}
            return render_template("404_error.html",error=error)
    return render_template('pneumonia.html')

# Cataract Section

# load cataract model path
CATARACT_MODEL_PATH = 'cataract.h5'

#Load your trained model
model = load_model(CATARACT_MODEL_PATH)
# cataract detection
def cataract_predict(img_path, model):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224)) #target_size must agree with what the trained model expects!!
    # Preprocessing the image
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    preds = model.predict(img)
    return preds

@app.route('/cataract',methods=['GET','POST'])
def cataract():
    if request.method == 'POST':
        try:
            # Get the file from post request
            f = request.files['file']
            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
                basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
            # Make prediction
            preds = cataract_predict(file_path, model)
            os.remove(file_path)#removes file from the server after prediction has been returned
            if preds == 1:
                res = "Sorry! you have symptoms of getting Cataract disease. Please consult the doctor"
            else:
                res = "Congratulations! you have no symptoms of Cataract disease.Be Happy:)"
            return render_template('cataract.html',prediction=res)
        except Exception as e:
            print(e)
            error=("Have you uploaded the image??🤔🤔")
            error={"error":error}
            return render_template("404_error.html",error=error)
    return render_template('cataract.html')


# Driver code
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(debug=True, port=port, host="0.0.0.0")