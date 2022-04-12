from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

todos = []

@app.route('/')
def index():
	#had to create a 'template' folder in the same directory as this script for it to find index.html as the template.
	return render_template('index.html', todos=todos)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['Task Name']
    priority = request.form['Priority']
    email = request.form['Email Address']

#if the email field doesn't have an @ symbol, go back to main page.
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
#if task has nothing, then go back to the main page.
    elif not task:
        return redirect('/')
#if the priority hasn't been changed, go back to main page.
    elif priority == 'Priority Level':
        return redirect('/')
#if all forms have been properly filled, append the entered info into the fields and variables.
    else:
        todos.append((task, priority, email))
    print(todos)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    del todos[:]
    return redirect('/')

if __name__ == '__main__':
	app.run(debug = True)