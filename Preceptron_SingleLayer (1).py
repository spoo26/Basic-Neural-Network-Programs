
# coding: utf-8

# In[1]:

#make prediction with weights
def predict(row,weights,b):
	activation=0.0
	for i in range(len(row)-1):
		activation+=weights[i]*row[i]
	activation+=b
	return 1.0 if activation>=1.0 else -1.0

#test predictions
dataset=[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1]]
alpha=1
weights=[0,0]
b=0
print("w1=%d, w2=%d, b=%d" %(weights[0],weights[1],b))
for row in dataset:
	prediction=predict(row,weights,b)
	print("Expected=%d,Predicted=%d" %(row[-1],prediction))
	while(row[-1]!=prediction):
		weights[0]+=alpha*row[-1]*row[0]
		weights[1]+=alpha*row[-1]*row[1]
		b+=alpha*row[-1]
		prediction=predict(row,weights,b)
	print("w1=%d, w2=%d, b=%d" %(weights[0],weights[1],b))
	print("After weight updation Expected=%d,Predicted=%d" %(row[-1],prediction))

