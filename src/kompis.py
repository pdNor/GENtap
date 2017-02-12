
PATH_TO_GENDATA = '../data/genData.gp'
PATH_TO_KEYWORDS = '../data/keyWords.gp'

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



obj = pyCgen()
obj.data.readFile()
print(obj.data.genData)