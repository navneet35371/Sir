import nltk   
from urllib import urlopen
from semanticpy.vector_space import VectorSpace

arr=[]
i=0
fin=open("input.txt","r")

fink = fin.readline()
while fink:
        
        #print fink
        if(not fink):
                break
    	html = urlopen(fink).read();
    	raw = nltk.clean_html(html);
        arr.append(raw)
        i=i+1
        fink = fin.readline()


vector_space = VectorSpace(arr)
#print arr[i-1]
#print "pa------------------------------------------van "
#i=i-1
print vector_space.search(["Topcoder"])
print vector_space.related(0)
