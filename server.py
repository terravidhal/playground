from flask import Flask ,render_template , redirect # added redirect!
app = Flask(__name__)    


@app.route('/')
def home():
    return redirect("/play")

# OR
# @app.route('/')
# def home():
#     return redirect(url_for('level_1')) # import url_for 

@app.route('/play')
def level_1():
    return render_template('index.html', num = 3, Color = "#01fefe")

@app.route('/play/<int:x>')
def level_2(x):
    return render_template('index.html', num = x, Color = "#01fefe")

@app.route('/play/<int:x>/<color>')
def level_3(x, color):
    return render_template('index.html', num = x, Color = color)

@app.errorhandler(404) # we specify in parameter here the type of error, here it is 404
def page_not_found(error): # (error) is important because it recovers the instance of the error that was thrown
    return f"<h2>Sorry! No response. Try again</h2>"


if __name__=="__main__":   
    app.run(debug=True)    