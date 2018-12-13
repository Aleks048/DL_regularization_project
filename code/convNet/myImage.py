#to store image and label
class MyImage:
    path = ""
    classNum=0
    def __init__(self,path = "",classNum = 0):
        self.classNum  = classNum
        self.path = path