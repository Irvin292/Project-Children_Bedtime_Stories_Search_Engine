import psycopg2
from psycopg2 import OperationalError
from flask import Flask, request, render_template, session, redirect, url_for
import os

dirc = os.getcwd()

app = Flask(__name__, template_folder = dirc)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result.html')
def result():
    return render_template("result.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")    

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="final",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None

@app.route('/result.html', methods=['POST'])
def my_form_post():
    search_text = request.form['search']
    search_type = request.form['search_type']
    conn = create_connection()
    cur = conn.cursor()



    if search_type == "title":
        query = f"SELECT title, content, word_count FROM stories_data WHERE title ilike '%{search_text}%';"
    else:
        query = f"SELECT title, word_count FROM stories_data WHERE content ilike '%{search_text}%';"

    cur.execute(query)
    result = cur.fetchall()

    stories = []
    if result:
        for story in result:
            if search_type == "title":
                title, content, word_count = story
                stories.append({"title": title, "content": content, "word_count": word_count})
            else:
                title = story[0]
                stories.append({"title": title, "content": None, "word_count": None})

    return render_template('result.html', stories=stories)

# @app.route('/index.html', methods=['GET', 'POST'])
# def entry_page():
#     if request.method == 'POST':
#         search_text = request.form.get['search']
#         search_type = request.form.get['search_type']
#         return redirect(url_for('result.html', my_var = search_text))
#     else:
#         return render_template('/index.html')

# @app.route('/result.html', methods=['GET', 'POST'])        
# def database():
#     my_var = request.args.get('my_var', None)
#     return render_template('/result.html', my_var = my_var)

if __name__ == '__main__':
    app.run(debug=True)

