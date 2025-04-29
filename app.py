
import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from functools import partial
from nltk.chat.util import Chat, reflections
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 608)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 341, 31))
        self.textEdit.setObjectName("textEdit")
        self.input_le = QtWidgets.QLineEdit(self.centralwidget,returnPressed=self.on_return_pressed)
        
        self.input_le.setGeometry(QtCore.QRect(460,571, 271, 20))
        self.input_le.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 341, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(440, -10, 20, 651))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 811, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Find = QtWidgets.QPushButton(self.centralwidget)
        self.Find.setGeometry(QtCore.QRect(370, 40, 75, 31))
        self.Find_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Find_2.setGeometry(QtCore.QRect(700, 40, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Find.setFont(font)
        self.Find.setObjectName("Find")
        self.Find_2.setFont(font)
        self.Find_2.setObjectName("Find_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(490, 10, 201, 81))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 182, 177))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Year = QtWidgets.QComboBox(self.groupBox)
        self.Year.setEditable(False)
        self.Year.setObjectName("Year")
        self.Year.addItem("")
        self.Year.addItem("")
        self.gridLayout.addWidget(self.Year, 2, 0, 1, 1)
        self.story = QtWidgets.QComboBox(self.groupBox)
        self.story.setEditable(False)
        self.story.setObjectName("story")
        self.story.addItem("")
        self.gridLayout.addWidget(self.story, 3, 0, 1, 1)
        self.Rating = QtWidgets.QComboBox(self.groupBox)
        self.Rating.setEditable(False)
        self.Rating.setObjectName("Rating")
        self.Rating.addItem("")
        self.Rating.addItem("")
        self.gridLayout.addWidget(self.Rating, 1, 0, 1, 1)
        self.Soup = QtWidgets.QComboBox(self.groupBox)
        self.Soup.setEditable(False)
        self.Soup.setObjectName("Soup")
        self.Soup.addItem("")
        
        self.gridLayout.addWidget(self.Soup, 4, 0, 1, 1)
        self.Genre = QtWidgets.QComboBox(self.groupBox)
        self.Genre.setObjectName("Genre")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
        self.Genre.addItem("")
       
        
        self.gridLayout.addWidget(self.Genre, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 110, 421, 491))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 419, 489))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setObjectName("tableView")
        # self.header=self.tableView.horizontalHeader()
        # self.header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(460, 110, 271, 461))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 269, 489))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_7.addWidget(self.textEdit_3, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MovieRecommendar"))
        self.label.setText(_translate("MainWindow", "Enter a Movie name to find same type of movies"))
        self.Find.setText(_translate("MainWindow", "Find"))
        self.Find_2.setText(_translate("MainWindow", "Apply"))
        self.groupBox.setTitle(_translate("MainWindow", "Filters"))
        self.Year.setToolTip(_translate("MainWindow", "Based on movie\'s year"))
        self.Year.setCurrentText(_translate("MainWindow", "Old to New"))
        self.Year.setItemText(0, _translate("MainWindow", "Old to New"))
        self.Year.setItemText(1, _translate("MainWindow", "New to Old"))
        self.story.setToolTip(_translate("MainWindow", "Based on movie\'s story"))
        self.story.setCurrentText(_translate("MainWindow", "Same Story"))
        self.story.setItemText(0, _translate("MainWindow", "Same Story"))
        self.Rating.setToolTip(_translate("MainWindow", "Based on Movie rating"))
        self.Rating.setCurrentText(_translate("MainWindow", ""))
        self.Rating.setItemText(1, _translate("MainWindow", "Low to High"))
        self.Rating.setItemText(0, _translate("MainWindow", "High To Low"))
        self.Soup.setToolTip(_translate("MainWindow", "Based on Same actor,director,producer,genre"))
        self.Soup.setCurrentText(_translate("MainWindow", "Soup"))
        self.Soup.setItemText(0, _translate("MainWindow", "Soup"))
       
        self.Genre.setItemText(0, _translate("MainWindow", "fantasy"))
        self.Genre.setItemText(1, _translate("MainWindow", "drama"))
        self.Genre.setItemText(2, _translate("MainWindow", "horror"))
        self.Genre.setItemText(3, _translate("MainWindow", "mystery"))
        self.Genre.setItemText(4, _translate("MainWindow", "family"))
        self.Genre.setItemText(5, _translate("MainWindow", "comedy"))
        self.Genre.setItemText(6, _translate("MainWindow", "action"))
        self.Genre.setItemText(7, _translate("MainWindow", "history"))
        self.Genre.setItemText(8, _translate("MainWindow", "thriller"))
        self.Genre.setItemText(9, _translate("MainWindow", "sci-fi"))
        self.Genre.setItemText(10, _translate("MainWindow", "romance"))
        self.Genre.setItemText(11, _translate("MainWindow", "adventure"))
        self.Genre.setItemText(12, _translate("MainWindow", "biography"))
        self.Genre.setItemText(13, _translate("MainWindow", "war"))
        self.Genre.setItemText(14, _translate("MainWindow", "crime"))
        self.Genre.setItemText(15, _translate("MainWindow", "film-noir"))
        self.Genre.setItemText(16, _translate("MainWindow", "western"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Recommendation for your search"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Chat with me"))

class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe

    dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)

    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return QtCore.QVariant()

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() \
            and 0 <= index.column() < self.columnCount()):
            return QtCore.QVariant()
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.iloc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return QtCore.QVariant()

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
       
        BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(BASE_DIR, "Bestdataset.csv")
        self.dataset = pd.read_csv(csv_path, low_memory=False, index_col=0)

        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix=self.tfidf.fit_transform(self.dataset['soup'].values.astype('U'))
        self.tfidf_matrix1=self.tfidf.fit_transform(self.dataset['description'].values.astype('U'))
        self.cosine_sim= linear_kernel(self.tfidf_matrix,self.tfidf_matrix)
        self.cosine_sim1= linear_kernel(self.tfidf_matrix1,self.tfidf_matrix1)
        self.indices = pd.Series(self.dataset.index,index=self.dataset['title'])  
        #self.pushButton.clicked.connect(self.browse_slot(argument))....it gives first argument error
        self.Find.clicked.connect(partial(self.get_recommendation,self.cosine_sim)) 
       
        self.story.activated.connect(partial(self.SoupStory,self.cosine_sim1))
        self.Year.activated.connect(partial(self.ratingYear,self.dataset))
        self.Soup.activated.connect(partial(self.SoupStory,self.cosine_sim))
       
        self.Genre.activated.connect(partial(self.genration,self.dataset))
        pairs = [
            [r"my name is (.*)", ["Hello %1 , how are you today?",]],
            [
                r"(what is your name?|who are you?)",
                ["my name is Blockbuster and made by jugesh.\n And yours?"],
            ],
            [
                r"(what is your (location|city)?|from where you are talking)",
                [
                    "i am here, in front of you \n  same location as yours"
                ],
            ],
            [
                r"(you) are (.*)",
                ["i am very very intelligent computer  \n %1 not %2 may be you are %2"],
            ],
            [
                r"is human (.*)",
                [" i think human is not very intelligent but may be %1"],
            ],
            
             [
                r"(how to use (it|this) ?)",
                ["enter correct spelling of movie in top left text bar and click find if that movie is availabel in database you will done or it show your whole database"],
            ],
              [
                r"(how to use filter?)",
                ["click on any filter and click on apply"],
            ],
               [
                r"(what is soup ?)",
                ["soup is mixture of director, actor, producer, genre and title. It show more precise recommendation."],
            ],
                [
                r"((Thank you| thanks))",
                ["your welcome"],
            ],
                 [
                r"(how its work?)",
                ["I use machine learning algorithm on your search to match features of your search"],
            ],
                   [r"((which movie is best *|show best movie))", ["your can use filter directly click on score and get best movie "]],
                  [r"(.*)", ["what!\n Sorry,i can't understand, FQA: how to use filter | how its work | how to use it"]]
        ]

        self._chat = Chat(pairs, reflections)
        self.Rating.activated.connect(partial(self.ratingText,self.dataset))
        self.textEdit_3.append("Please enter the movie name and click Find button ,it takes some time or may be show not responding ,so wait for result")
        #self.textEdit_2.setPlainText(str(self.data)).......it gives connection error
    @property
    def chat(self):
        return self._chat
    @QtCore.pyqtSlot()
    def on_return_pressed(self):
        text = self.input_le.text()
        if text:
        
            res = self.chat.respond(text)
            self.textEdit_3.append("\n[me]: {}".format(text))
            self.textEdit_3.append("[bot]: {}".format(res))
            self.input_le.clear()
        
    def genration(self,dataset):
         self.check = str(self.Genre.currentText())
         data=pd.DataFrame()
         for i in range(len(dataset)):
           
          
             yes=self.check in dataset.iloc[i]['genre']
             if yes==True:
                 
                 data = pd.concat([data, dataset.iloc[[i]]], ignore_index=True)

         self.Find_2.clicked.connect(partial(self.showgenre,data))
        
         
    def showgenre(self,dataset):
        model = DataFrameModel(pd.DataFrame(dataset))
        self.tableView.setModel(model)
        
    def ratingText(self,dataset): 
        self.check = str(self.Rating.currentText())
    
        if self.check=="High To Low":
            self.Find_2.clicked.connect(partial(self.Ratings,False,dataset))
        else:
            self.Find_2.clicked.connect(partial(self.Ratings,True,dataset))
    def ratingYear(self,dataset):
        self.check = str(self.Year.currentText())
    
        if self.check=="New to Old":
            self.Find_2.clicked.connect(partial(self.Years,False,dataset))
        else:
            self.Find_2.clicked.connect(partial(self.Years,True,dataset))
    def SoupStory(self,cosine_sim1):
        self.Find_2.clicked.connect(partial(self.get_recommendation,cosine_sim1))
        
        
    def Ratings(self,yes,dataset):
        self.data=dataset.sort_values('score',ascending=yes).reset_index(drop=True)
        model = DataFrameModel(pd.DataFrame(self.data))
        self.tableView.setModel(model)
    def Years(self,yes,dataset):
        self.data=dataset.sort_values('year',ascending=yes).reset_index(drop=True)
        model = DataFrameModel(pd.DataFrame(self.data))
        self.tableView.setModel(model)
    def get_recommendation(self,cosine_sim):
       
        try:
            title=str.lower( self.textEdit.toPlainText())
        
            idx=self.indices[title]
            sim_scores=list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores,key=lambda x:x[1],reverse=True)
            self.textEdit_3.append("\ntop 10 movie relate to your movie")
            sim_scores =sim_scores[1:11]
            movie_indices=[i[0] for i in sim_scores] 
            self.data= self.dataset.iloc[movie_indices].reset_index(drop=True)
            
            #setPlainText argument 1 has unexpected type series..... if you not convert it into string 
            
            model = DataFrameModel(pd.DataFrame(self.data))
            self.tableView.setModel(model)
            self.Rating.activated.connect(partial(self.ratingText,self.data))
            self.Year.activated.connect(partial(self.ratingYear,self.data))
           # self.Genre.activated.connect(partial(self.genration,self.data))
            
            
        except KeyError as e:
            self.textEdit_3.append("\nmay be wrong spelling or movie does not exist in database "+str(e)+" here you can see Movies")
            model = DataFrameModel(self.dataset)
            self.tableView.setModel(model)
if __name__ == "__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
