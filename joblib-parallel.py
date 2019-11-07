from math import sqrt
from joblib import Parallel, delayed

def parallel(out, limit):
    Parallel(n_jobs=2)(delayed(sqrt)(i ** out) 
                   for i in range(limit))
    

start = time.time()
parallel(2, 100)
end = time.time()
print(end - start)
