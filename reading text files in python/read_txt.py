
def readLinesFromFile(filename="lines.txt"):
    file = open(filename)
    a = file.read()
    print(a)
    if "dash" in a:
        print(a[10]) 
    file.close()
    
#readLinesFromFile()    


def readLinesFromFileSeconOption(filename="lines.txt"):
    
    Lines = []
    with open(filename) as file:
        a = file.read()
        words = (a.split(":",1))
        print(words)
       # print(a)
        for line in file.readlines():
            Lines.append(line.split(":",1))
            print(file.readlines())
            word, sentences = zip(*Lines)
            
    return word, sentences      
        
        
readLinesFromFileSeconOption()        