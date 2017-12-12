from sklearn.clusters import DBSCAN
import pandas as pd
data = pd.read_csv("data/wholesale.csv")
# Drop non-continuous variables
data.drop(["Channel", "Region"], axis = 1, inplace = True)
stscaler = StandardScaler().fit(data)
data = stscaler.transform(data)
dbsc = DBSCAN(eps = .5, min_samples = 15).fit(data)
labels = dbsc.labels_
core_samples = np.zeros_like(labels, dtype = bool)
core_samples[dbsc.core_sample_indices_] = True


