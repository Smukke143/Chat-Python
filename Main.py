from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'chat'
)




app = Flask(__name__)


@app.route('/',methods=['GET'])
def main():
    
    mycursor = connection.cursor(buffered=True)

    mycursor.execute('Select * from users')

    data = mycursor.fetchall()

    print(data)

    datalist = {'data':data}

    return render_template('auth.html',data = datalist)



@app.route('/login',methods=['GET','POST'])
def login():

    login = request.form['login']
    Password = request.form['password']

    mycursor = connection.cursor(buffered=True)

    mycursor.execute('Select * from users where login = %s and password = %s',(login,Password))

    data = mycursor.fetchone()

    datalist = {'list': data}

    if data is None:
        return 'Такого пользователя не найденно или не верный пароль '
    else:
        return 'Вы вошли в свой аккаунт'


@app.route('/Reg',methods=['GET','POST'])
def Reg():

    login = request.form['login']
    Password = request.form['password']

    mycursor = connection.cursor(buffered=True)

    mycursor.execute('insert into users (login,password) values (%s , %s)',(login ,Password))
    connection.commit()

    return 'Пользователь зарегестрирован'

    


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0',port = int('3000'))