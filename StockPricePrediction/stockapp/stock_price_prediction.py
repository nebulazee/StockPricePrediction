import pandas as pd
import quandl,math
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression 

def predict(data):
	df=quandl.get(data)
	#df=quandl.get("EOD/MSFT", authtoken="hUwCJi-QMa5gwQXG71xr")
	#df=quandl.get("SSE/TL0", authtoken="hUwCJi-QMa5gwQXG71xr")
	#print(df)
	df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
	df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
	df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
	df['100ma']=df['Adj. Close'].rolling(window=100,min_periods=0).mean()
	df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume','100ma']]
	 
	forecast_col = 'Adj. Close'

	df.fillna(value=-99999, inplace=True)
	forecast_out = int(math.ceil(0.0001 * len(df)))
	#print(forecast_out)
	df['label']=df[forecast_col].shift(-forecast_out)
	#e=df[:-forecast_out]
	#df.dropna(inplace=True)
	#print(df)
	x=np.array(df.drop(['label'],1))
	x=preprocessing.scale(x)

	x_lately=x[-forecast_out:]
	x=x[:-forecast_out]

	df.dropna(inplace=True)
	y=np.array(df['label'])
	y=np.array(df['label'])

	x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)

	clf=LinearRegression(n_jobs=-1)
	clf.fit(x_train,y_train)
	accuracy=clf.score(x_test,y_test)


	forecast_set = clf.predict(x_lately)
	print(accuracy)
	print(forecast_set)
	return forecast_set
