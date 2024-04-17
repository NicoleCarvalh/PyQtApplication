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

  def gotologin(self):
    login = LoginScreen()
    widget.addWidget(login)
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
