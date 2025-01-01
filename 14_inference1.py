import mlflow
from mlflow.models import infer_signature
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

if __name__=="__main__":
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=42)
    X = pd.DataFrame(X, columns=["feature_{}".format(i) for i in range(10)])
    y = pd.DataFrame(y, columns=["target"])

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=43)

    # load model
    rfc = mlflow.sklearn.load_model(model_uri="/home/ahmedcr7/Programming/Python/4- MLops-tools/MLfLow/testing_artifacts/edab45d92c8544068ca058feb3c57284/artifacts/random_forest_classifier")
    # rfc = mlflow.pyfunc.load_model(model_uri="/home/ahmedcr7/Programming/Python/4- MLops-tools/MLfLow/testing_artifacts/edab45d92c8544068ca058feb3c57284/artifacts/random_forest_classifier")
    
    y_pred = rfc.predict(X_test)
    y_pred = pd.DataFrame(y_pred, columns=["prediction"])

    print(y_pred.head())