import sys
import requests

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont, QPainter, QBrush, QPen
from PyQt5 import QtCore

from math import floor
# To change what accounts the program grabs, change these values

platform = "pc"
region = "us"

player1 = "BonzosBGN-1925"
player2 = "SarcophaGus-11668"
player3 = "JDat-1846"
player4 = "ReputeUrchin-1953"
player5 = "WackyD-11704"
player6 = "Your3Welcome-1387"

role1 = 'tank'
role2 = 'tank'
role3 = 'support'
role4 = 'support'
role5 = 'damage'
role6 = 'damage'

#
#   Overwatch API Application code
#   The overwatch API used for this project is 
#   http://owapi.io/profile/platform/region/playername-####
#

def getPlayerSR(pf, rg, player, role):
    r = requests.get("http://owapi.io/profile/" + pf + '/' + rg + '/' + player)
    a = r.json()
    if 'message' in a:
        return "Profile not found"
    sr = (a['competitive'][role]['rank'])
    if sr is not None:
        print(player + "  SR: " + str(sr))
        return sr
    else:
        return 0000

rank1 = getPlayerSR(platform, region, player1, role1)
rank2 = getPlayerSR(platform, region, player2, role2)
rank3 = getPlayerSR(platform, region, player3, role3)
rank4 = getPlayerSR(platform, region, player4, role4)
rank5 = getPlayerSR(platform, region, player5, role5)
rank6 = getPlayerSR(platform, region, player6, role6)

def findAvgSR(sr1, sr2, sr3, sr4, sr5, sr6):
    total = sr1 + sr2 + sr3 + sr4 + sr5 + sr6
    avg = total / 6
    return floor(avg)
#
#   Qt5 Application code
#

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Average SR Finder')
window.setFixedSize(750, 500)

# Constructing UI elements

playerLabel1 = QLabel("", parent=window)
playerLabel2 = QLabel("", parent=window)
playerLabel3 = QLabel("", parent=window)
playerLabel4 = QLabel("", parent=window)
playerLabel5 = QLabel("", parent=window)
playerLabel6 = QLabel("", parent=window)

rankLabel1 = QLabel("", parent=window)
rankLabel2 = QLabel("", parent=window)
rankLabel3 = QLabel("", parent=window)
rankLabel4 = QLabel("", parent=window)
rankLabel5 = QLabel("", parent=window)
rankLabel6 = QLabel("", parent=window)

playerLabel1.setGeometry(10, 5, 200, 20)
playerLabel2.setGeometry(10, 85, 200, 20)
playerLabel3.setGeometry(10, 165, 200, 20)
playerLabel4.setGeometry(10, 245, 200, 20)
playerLabel5.setGeometry(10, 325, 200, 20)
playerLabel6.setGeometry(10, 405, 200, 20)

rankLabel1.setGeometry(10, 25, 200, 20)
rankLabel2.setGeometry(10, 105, 200, 20)
rankLabel3.setGeometry(10, 185, 200, 20)
rankLabel4.setGeometry(10, 265, 200, 20)
rankLabel5.setGeometry(10, 345, 200, 20)
rankLabel6.setGeometry(10, 425, 200, 20)

playerLabel1.setText(player1)
playerLabel2.setText(player2)
playerLabel3.setText(player3)
playerLabel4.setText(player4)
playerLabel5.setText(player5)
playerLabel6.setText(player6)

rankLabel1.setText("SR: " + str(rank1))
rankLabel2.setText("SR: " + str(rank2))
rankLabel3.setText("SR: " + str(rank3))
rankLabel4.setText("SR: " + str(rank4))
rankLabel5.setText("SR: " + str(rank5))
rankLabel6.setText("SR: " + str(rank6))

avgSRLabel = QLabel("", parent=window)
avgSRLabel.setGeometry(300, 5, 450, 200)
avgSRLabel.setFont(QFont("Arial", 40))
avgSRLabel.setText("Avg SR: " + str(findAvgSR(rank1, rank2, rank3, rank4, rank5, rank6)))

window.show()

# Exit Application
sys.exit(app.exec())