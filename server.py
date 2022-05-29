from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'cheebo_is_beebo_elito'

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    else:
        session['visits'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    print(session)
    return redirect('/')

@app.route('/up_by_2')
def up_by_2():
    session['visits'] += 1
    return redirect('/')

@app.route('/up_by_x', methods=['POST'])
def up_by_x():
    print(request.form)
    session['visits'] += int(request.form['amount'])-1
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)