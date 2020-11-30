from flask import Flask, render_template, request
import pickle
import numpy as np
#------------------------------------------------------------
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
#------------------------------------------------------------

@app.route('/', methods=['GET']) 
def Home():
    return render_template('index.html')

#------------------------------------------------------------
@app.route("/predict", methods=['POST'])
def predict():

        Year = int(request.form['Year'])
    
        Kms_Driven=int(request.form['Kms_Driven'])
        
        seller_type=request.form['seller_type']
        if(seller_type=="Dealer"):
            seller_type=0
        else:
            seller_type=1
        
        transmission=request.form['transmission']
        if(transmission=='Manual'):
            transmission=0
        else:
            transmission=1
            
        Owner=int(request.form['Owner'])
        
        
        fuel_Petrol=request.form['fuel_Petrol']
        if(fuel_Petrol=='Petrol'):
            fuel_Petrol=1
            fuel_Diesel=0
            
        else:
            fuel_Petrol=0
            fuel_Diesel=1

        pred_agrs = [Year , Kms_Driven , seller_type , transmission , 
                     Owner , fuel_Petrol , fuel_Diesel]

        pred_agrs_arr = np.array(pred_agrs)
        pred_agrs_arr = pred_agrs_arr.reshape(1 , -1)
            
        model_pred = model.predict(pred_agrs_arr)
        model_pred = round(float(model_pred))
        return render_template('predict.html' , prediction = model_pred)

if __name__=="__main__":
    app.run(debug=True)

