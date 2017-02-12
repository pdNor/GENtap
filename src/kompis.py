
PATH_TO_GENDATA = '../data/genData.gp'
PATH_TO_KEYWORDS = '../data/keyWords.gp'
GENERATE_FILES = 1

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

class userInt():
    def __init__(self):
        self.outPutFileName = ""
        self.pyGen = pyCgen()

    def initGUI(self):
        print('Kompis Automation \n')
        print('Options:\n1:Generate empty c and h file')
        try:
            sel = int(input('Select: '))
        except ValueError:
            print('Not a valid selection')
        
        self.selection(sel)

    def selection(self, sel):
        if sel == GENERATE_FILES:
            self.generateFile()
        else:
            print("Not a valid selection")
    
    def generateFile(self):
        self.outPutFileName = input("Enter filename: ")
        print(self.pyGen.data.genData)

gui = userInt()
gui.initGUI()