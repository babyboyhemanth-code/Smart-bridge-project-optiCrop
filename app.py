from flask import Flask, render_template, request, redirect, url_for
from utils.prediction import predict_crop
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY


# ---------------- HOME ---------------- #

@app.route('/')
def home():
    return render_template('index.html')


# ---------------- LOGIN ---------------- #

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        print("Email:", email)
        print("Password:", password)

        # Database verification will be added later
        return redirect(url_for('dashboard'))

    return render_template('login.html')


# ---------------- REGISTER ---------------- #

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        print(fullname)
        print(email)
        print(phone)

        # Save into MySQL later

        return redirect(url_for('login'))

    return render_template('register.html')


# ---------------- DASHBOARD ---------------- #

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ---------------- CROP PAGE ---------------- #

@app.route('/crop')
def crop():
    return render_template('crop_prediction.html')


# ---------------- CROP PREDICTION ---------------- #

@app.route('/predict_crop', methods=['POST'])
def predict_crop_route():

    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])

    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    result = predict_crop(
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    )

    return render_template(
        'result.html',
        result=result
    )


# ---------------- FERTILIZER ---------------- #

@app.route('/fertilizer')
def fertilizer():
    return render_template('fertilizer.html')


@app.route('/fertilizer_predict', methods=['POST'])
def fertilizer_predict():

    result = "Urea"

    return render_template(
        'result.html',
        result=result
    )


# ---------------- IRRIGATION ---------------- #

@app.route('/irrigation')
def irrigation():
    return render_template('irrigation.html')


@app.route('/irrigation_predict', methods=['POST'])
def irrigation_predict():

    moisture = float(request.form['moisture'])

    if moisture < 30:
        result = "Irrigation Required"
    elif moisture < 60:
        result = "Monitor Soil Moisture"
    else:
        result = "No Irrigation Needed"

    return render_template(
        'result.html',
        result=result
    )


# ---------------- WEATHER ---------------- #

@app.route('/weather', methods=['GET', 'POST'])
def weather():

    if request.method == 'POST':

        city = request.form['city']

        result = f"Weather information for {city} will be available after API integration."

        return render_template(
            'result.html',
            result=result
        )

    return render_template('weather.html')


# ---------------- MARKET ---------------- #

@app.route('/market', methods=['GET', 'POST'])
def market():

    if request.method == 'POST':

        crop = request.form['crop']

        result = f"Market price for {crop} will be available after API integration."

        return render_template(
            'result.html',
            result=result
        )

    return render_template('market.html')


# ---------------- RESULT ---------------- #

@app.route('/result')
def result():
    return render_template('result.html')


# ---------------- LOGOUT ---------------- #

@app.route('/logout')
def logout():
    return redirect(url_for('home'))


# ---------------- MAIN ---------------- #

if __name__ == '__main__':
    app.run(debug=True)