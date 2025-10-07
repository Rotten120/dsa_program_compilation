from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('upper_inp', '')
        result = input_string.upper()
    return render_template('toupper.html', result=result)

@app.route('/circle_area', methods=['GET', 'POST'])
def circle_area():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = 3.14 * radius * radius
    return render_template('circle.html', result=area)

@app.route('/triangle_area', methods=['GET', 'POST'])
def triangle_area():
    area = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area = 0.5 * base * height
    return render_template('triangle.html', result=area)

if __name__ == "__main__":
    app.run(debug=True)
