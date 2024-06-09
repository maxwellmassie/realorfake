from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def quiz():
    result = None
    correct_answer = 'B'
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer != correct_answer:
            result = 'OHH NOO FAKE 😔😔😔'
    return render_template('quiz.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
