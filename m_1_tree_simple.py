from sklearn import tree
p={("smooth","apple"):1, ("orange","bumpy"):0}
x=[[140,1],[130,1],[150,0],[170,0]]
y=[1,1,0,0]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
l=clf.predict([[132,1]])
o=l[0]
print o
#print p[0][1]
print [k for k,v in p.items() if o==v]
