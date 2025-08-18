class WriteFile:
    def __init__(self,path:str):
        self.path = path
        self.file = open(self.path.replace(".py",".txt"),"w")

    def __call__(self,data: list[str]):
        print(data,file=self.file)
        self.file.close()