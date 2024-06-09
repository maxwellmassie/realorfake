# from flask import Flask, render_template_string, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def quiz():
#     question = "Apakah bumi bulat?"
#     choices = ["Ya", "Tidak"]
#     correct_answer = "Ya"
#     message = ""

#     if request.method == "POST":
#         selected_answer = request.form.get("answer")
#         if selected_answer:
#             if selected_answer == correct_answer:
#                 message = "Benar!"
#             else:
#                 message = "FAKE"

#     return render_template_string('''
#         <!doctype html>
#         <html lang="en">
#           <head>
#             <meta charset="utf-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#             <title>Kuis Sederhana</title>
#           </head>
#           <body>
#             <div style="text-align: center; margin-top: 50px;">
#               <h1>{{ question }}</h1>
#               <form method="post">
#                 <div>
#                   <input type="radio" id="choice1" name="answer" value="{{ choices[0] }}">
#                   <label for="choice1">{{ choices[0] }}</label>
#                 </div>
#                 <div>
#                   <input type="radio" id="choice2" name="answer" value="{{ choices[1] }}">
#                   <label for="choice2">{{ choices[1] }}</label>
#                 </div>
#                 <button type="submit">Submit</button>
#               </form>
#               {% if message %}
#                 <p>{{ message }}</p>
#               {% endif %}
#             </div>
#           </body>
#         </html>
#     ''', question=question, choices=choices, message=message)

# if __name__ == "__main__":
#     app.run(debug=True)
