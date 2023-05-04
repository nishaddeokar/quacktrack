import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputForm
import sqlite3

streak = 0


def insert(id, step, step_target, weight, weight_target, height, level):
    con = sqlite3.connect("out.db")
    con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,STEP,STEP_TARGET,WEIGHT,WEIGHT_TARGET,HEIGHT,LEVEL) \
          VALUES (?,?,?,?,?,?,?)", (id, step, step_target, weight, weight_target, height, level))
    con.commit()
    con.close()


def get_last_level():
    con = sqlite3.connect("out.db")
    sql_query = """SELECT LEVEL FROM HEALTH_DATA ORDER BY ID DESC LIMIT 1;"""
    cursor = con.cursor()
    cursor.execute(sql_query)
    return int(cursor.fetchall()[0][0])
    con.close()


def set_level(target, step, last_level):
    global streak
    if step - target > 0:
        streak += 1
        return last_level + 1
    elif step - target < 0:
        streak = 0
        return last_level - 1
    else:
        streak += 1
        return last_level


def get_image(level):
    if level < 10:
        return 'sprite1.png'
    elif level >= 10 and level < 20:
        return 'sprite2.png'
    elif level >= 20 and level < 30:
        return 'sprite3.png'
    elif level >= 30 and level < 40:
        return 'sprite4.png'
    else:
        return 'sprite5.png'


def bmi(height, weight):
    bmi = round(weight / (height/100)**2, 1)
    if bmi <= 18.4:
        return bmi, "Underweight"
    elif bmi >= 25:
        return bmi, "Overweight"
    else:
        return bmi, "a Healthy weight"


@app.route('/', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        last_level = get_last_level()
        level = set_level(form.step_target.data, form.step.data, last_level)
        date = datetime.today().strftime('%Y-%m-%d')
        insert(date, form.step.data, form.step_target.data, float(form.weight.data),
               float(form.weight_target.data), float(form.height.data), level)
        flash('Your BMI is {}. You are {}!'.format(
            *bmi(form.height.data, form.weight.data)))
        return redirect(url_for('pet'))
    return render_template('input.html',  title='Input', form=form)


@app.route('/pet')
def pet():
    lvl = get_last_level()
    img = get_image(lvl)
    if streak != 0:
        fire = "(" + str(streak) + " days streak) \U0001F525"
    else:
        fire = ""
    user = {'username': 'Nishad', 'image': img,
            'level': lvl, 'streak': fire}
    return render_template('pet.html', title='Pet', user=user)


def make_graph():
    con = sqlite3.connect("out.db")

    test = """SELECT * FROM HEALTH_DATA;"""
    cursor = con.cursor()
    cursor.execute(test)
    print(cursor.fetchall())

    sql_query = """SELECT ID, STEP, WEIGHT FROM HEALTH_DATA ORDER BY ID;"""
    cursor = con.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    dates = []
    steps = []
    weights = []
    for row in rows:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d').date())
        steps.append(row[1])
        weights.append(row[2])

    date_range = max(dates) - min(dates)
    if date_range.days >= 365:
        timescale = 'year'
    elif date_range.days >= 31:
        timescale = 'month'
    else:
        timescale = 'day'

    # Determine the x-axis tick marks and format based on the timescale
    if timescale == 'year':
        locator = mdates.YearLocator()
        formatter = mdates.DateFormatter('%Y')
    elif timescale == 'month':
        locator = mdates.MonthLocator()
        formatter = mdates.DateFormatter('%Y-%m')
    else:
        locator = mdates.DayLocator()
        formatter = mdates.DateFormatter('%Y-%m-%d')

    # Create the plot
    plt.switch_backend('Agg')
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    line1, = ax1.plot(dates, steps)
    line2, = ax2.plot(dates, weights, color='r')

    ax1.set_xlabel('Date')
    ax1.xaxis.set_major_locator(locator)
    ax1.xaxis.set_major_formatter(formatter)
    ax1.xaxis.set_tick_params(rotation=65)

    # Set the y-axis labels
    ax1.set_ylabel('Steps')
    ax2.set_ylabel('Weight')

    # Add a legend
    ax1.legend((line1, line2), ('Steps', 'Weight'))

    plt.savefig('app/static/foo.png')

    con.close()


@app.route('/display')
def display():
    make_graph()
    user = {'username': 'Nishad', 'graph': 'foo.png'}
    return render_template('display.html', title='Display', user=user)
