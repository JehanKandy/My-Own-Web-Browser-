from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class jkweb():
    def __init__(self):
            
        #get all widget from PyQt5
        self.window = QWidget()
        
        #set the title of web browser
        self.window.setWindowTitle("JehanKandy Web Browser")
        
        #get box layout for web browser
        self.layout = QVBoxLayout()
        
        #buttons in horizontal 
        self.horizontal = QHBoxLayout()
        
        #for Url Bar
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30) #size of url bar
        
        #for Go button
        self.go_btn = QPushButton("GO")
        self.go_btn.setMinimumHeight(30) #size of GO button
        
        #for Back button
        self.back_btn = QPushButton("<-")
        self.back_btn.setMinimumHeight(30) #size of Back button
        
        #for Forward button
        self.forward_btn = QPushButton("->")
        self.forward_btn.setMinimumHeight(30) #size of Forward button
        
        #now add buttons and url box on the browser
        self.horizontal.addWidget(self.url_bar)         #for url bar
        self.horizontal.addWidget(self.go_btn)          #for GO Button
        self.horizontal.addWidget(self.back_btn)        #for Back Button
        self.horizontal.addWidget(self.forward_btn)     #for GO Button
        
        #now create the browser
        self.browser = QWebEngineView()
        
        
        #when someone click the go button
        self.go_btn.clicked.connect(lambda: self.navigation(self.url_bar.toPlainText()))
        
        #when someone click the back button
        self.back_btn.clicked.connect(self.browser.back)
        
        #when someone click the forward button
        self.forward_btn.clicked.connect(self.browser.forward)
        
        
        #add horizontal Layout
        self.layout.addLayout(self.horizontal)
        
        #add all Widget
        self.layout.addWidget(self.browser)
        
        #set the Strating page
        self.browser.setUrl(QUrl("http://google.com"))
        
        #display the browser
        self.window.setLayout(self.layout)
        self.window.show()
    
    #now create browser functions
    
    def navigation(self, url):
        
        #check url not strat with http:
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
            
        
        




app = QApplication([])
window = jkweb()
app.exec_()