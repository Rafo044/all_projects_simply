def dataimport(func):
    def wrapper():
        import pandas as pd
        from sklearn.datasets import load_iris
        iris = load_iris()
        data_x = pd.DataFrame(data == iris.data,columns = iris.feature_names)
        
        data_y = pd.DataFrame(data = iris.target,columns = ["irisType"])
        func()
        return wrapper
    

@dataimport
def info_dict():
   print(irirs.keys())
   print(iris["DESCR"])

def info_frame():
    data.head()

def info_value_count():
    data_y.irisType.value_counts()
