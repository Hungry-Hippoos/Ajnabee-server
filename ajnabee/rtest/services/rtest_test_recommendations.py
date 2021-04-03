import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

def recommend(X,user,threshold=5):
    model = KMeans(n_clusters=2, random_state=0)
    print(X)
    model.fit(X[:,1:])
    frame = pd.DataFrame(X)
    frame['cluster'] = model.predict(X[:,1:])
    k = model.predict(user.reshape(1,-1)[:,1:])
    print("K",k)
    frame.columns = ['User_id','F1', 'F2','F3', 'F4', 'F5', 'F6','F7', 'F8','F9', 'F10','cluster']
    print(frame)
    data = frame[frame["cluster"]==k[0]].iloc[:,1:11]
    print(" ",data)
    distances = model.transform(data)
    required_distances = distances[:,k].reshape(distances.shape[0])
    idx = (-required_distances).argsort()[:threshold]
    print(required_distances)
    # return user_name with the help of idx
    print(len(data.iloc[idx,:].index))
    list_recommended_users = []
    for i in range(len(data.iloc[idx,:].index)):
        list_recommended_users.append(data.iloc[idx,:].index[i])
    print(list_recommended_users)
    return list_recommended_users

# recommend(X,y,model_kmeans,0,2)