import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sqlite3



class WelcomeScreen(QDialog):
  def __init__(self):
    super(WelcomeScreen, self).__init__()
    loadUi("welcomeScreen.ui", self)
    self.login_button.clicked.connect(self.gotologin)
    self.register_button.clicked.connect(self.gotocreate)

  def gotologin(self):
    login = LoginScreen()
    widget.addWidget(login)
    widget.setCurrentIndex(widget.currentIndex()+1)

  def gotocreate(self):
    create = CreateAccScreen()
    widget.addWidget(create)
    widget.setCurrentIndex(widget.currentIndex()+1)


class LoginScreen(QDialog):
  def __init__(self):
    super(LoginScreen, self).__init__()
    loadUi("login.ui", self)
    self.enter_button.clicked.connect(self.loginfunction)

  def loginfunction(self):
    user = self.email_field.text()
    password = self.password_field.text()

    if len(user) == 0 or len(password)==0:
      self.error_message.setText("Please input all fields.")
      return
    
    # Conexão BD
    conn = sqlite3.connect("shop_data.db")
    cur = conn.cursor()
    query = 'SELECT password from login_info WHERE username =\''+user+"\'"
    cur.execute(query)
    result_pass = cur.fetchone()


    if result_pass is None:
      self.error_message.setText("User not found.")
    else:
      result_pass = result_pass[0] 
      
    
    if result_pass == password:
      print("Successfully logged in!")
      self.error_message.setText("")
    else:
      self.error_message.setText("Invalid username or password")

class CreateAccScreen(QDialog):
  def __init__(self):
    super(CreateAccScreen, self).__init__()
    loadUi("registerScreen.ui", self)
    self.create_button.clicked.connect(self.createaccount)

  def createaccount(self):
    user = self.email_field.text()
    password = self.password_field.text()
    repeatPassword = self.repeat_password_field.text()

    if len(user) == 0 or len(password) == 0 or len(repeatPassword) == 0:
      self.error_message.setText("Please, fill all inputs.")

    elif password!=repeatPassword:
      self.error_message.setText("The passwords don't match")

    else:
      conn = sqlite3.connect("shop_data.db")
      cur = conn.cursor()

      user_info = [user, password]
      cur.execute('INSERT INTO login_info (username, password) VALUES (?, ?)', user_info)

      conn.commit()
      conn.close()

      print("User registered :) ")
      # fillprofile = FillProfileScreen()
      # widget.addWidget(fillprofile)
      # widget.setCurrentIndex(widget.currentIndex()+1)
    

app = QApplication(sys.argv)
welcome=WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(1100)
widget.show()
try:
  sys.exit(app.exec()) 
except:
  print("Exiting")
