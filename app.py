from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():

    name = request.form['name']
    max_marks = int(request.form['max_marks'])

    sub1 = int(request.form['sub1'])
    sub2 = int(request.form['sub2'])
    sub3 = int(request.form['sub3'])
    sub4 = int(request.form['sub4'])
    sub5 = int(request.form['sub5'])

    marks = [sub1, sub2, sub3, sub4, sub5]

    # Validation
    for mark in marks:
        if mark < 0 or mark > max_marks:
            return render_template(
                "index.html",
                error=f"Marks must be between 0 and {max_marks}."
            )

    total = sum(marks)
    average = total / 5

    maximum_total = max_marks * 5
    percentage = (total / maximum_total) * 100
    percentage = round(percentage, 2)

    # Grade
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    # Pass / Fail
    if percentage >= 35:
        status = "Pass"
    else:
        status = "Fail"

    # Motivational Message
    if grade == "A":
        message = "Excellent!"
    elif grade == "B":
        message = "Great Job!"
    elif grade == "C":
        message = "Good Work!"
    elif grade == "D":
        message = "Keep Practicing!"
    else:
        message = "Don't Give Up!"

    return render_template(
        "index.html",
        name=name,
        total=total,
        average=round(average, 2),
        percentage=percentage,
        grade=grade,
        status=status,
        message=message
    )


if __name__ == '__main__':
    app.run(debug=True)