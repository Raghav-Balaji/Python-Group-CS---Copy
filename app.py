from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy database (in-memory)
users = {}
bookings = []

# Real-time location suggestions (you may need to implement this)
locations = ['Jayanagar', 'JP Nagar', 'Banashankari','Vijayanagar']

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        pickup_location = request.form.get('pickup_location')
        drop_location = request.form.get('drop_location')
        bookings.append({'pickup': pickup_location, 'drop': drop_location})
        return redirect(url_for('confirmation'))
    return render_template('booking.html', locations=locations)

@app.route('/confirmation')
def confirmation():
    latest_booking = bookings[-1] if bookings else None
    return render_template('confirmation.html', booking=latest_booking)

@app.route('/show_bookings')
def show_bookings():
    return render_template('show_bookings.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
