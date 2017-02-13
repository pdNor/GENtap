import datetime

PATH_TO_GENDATA = '../data/genData.gp'
PATH_TO_KEYWORDS = '../data/keyWords.gp'
GENERATE_FILES = 1
OUTPUT_DIR = '../output/'
LINE_LENGTH = 80
class commentTypes():
    UPPER_LINE = 1
    LOWER_LINE = 2

class pyParse():
    def __init__(self):
        self.fileGenData = open(PATH_TO_GENDATA)
        self.fileKey = open(PATH_TO_KEYWORDS)
        self.genData = {}
        self.keyWord = {}

    def readFile(self):
        for line in self.fileGenData:
            (key,val) = line.split(',')
            val = val.replace('\n','')
            self.genData[key] = val

class pyCgen():
    def __init__(self):
        self.data = pyParse()
        self.data.readFile() 
        self.sourceFile = None
        self.headerFile = None

    def generateSourceFile(self, arg1):
        self.sourceFile = open(OUTPUT_DIR + arg1,'w')
        self.printBox(commentTypes.UPPER_LINE)
        self.printAuthor()
        self.printBox(commentTypes.UPPER_LINE)

    def printBox(self, type):
        if type == commentTypes.UPPER_LINE:
            self.sourceFile.write(self.data.genData['star']*LINE_LENGTH)
            self.sourceFile.write('\n')
    
    def printAuthor(self):
        now = datetime.datetime.now()
        line = ' Copyright: ' + self.data.genData['company'] + ' ' + str(now.year)
        
        for x in range(len(line),(LINE_LENGTH - 2)):
            line = line + ' '
        
        line = line + self.data.genData['star'] + '\n'

        self.sourceFile.write(self.data.genData['star'])
        self.sourceFile.writelines(line)

class userInt():
    def __init__(self):
        self.pyGen = pyCgen()

    def initUI(self):
        print('Kompis Automation \n')
        print('Options:\n1:Generate empty c and h file')
        try:
            sel = int(input('Select: '))
        except ValueError:
            print('Not a valid selection')
            self.initUI()
        self.selection(sel)
        
    def selection(self, sel):
        if sel == GENERATE_FILES:
            self.generateFile()
        else:
            print("Not a valid selection")
    
    def generateFile(self):
        outPutFileName = input("Enter filename: ")
        print(outPutFileName)
        self.pyGen.generateSourceFile(outPutFileName)
        print(self.pyGen.data.genData)
        


gui = userInt()
gui.initUI()