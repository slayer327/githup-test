class dog():
    def __init__(self,name,color):
        self.name=name
        self.color=color
listdog=[]
d1=dog('panda','den')
listdog.append(d1)
print(listdog[0].name," ",listdog[0].color)
listdog[0].color='trang'
print(d1.name," ",d1.color)