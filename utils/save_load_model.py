import joblib

joblib.dump(my_model_path, "my_model.joblib")
#...
my_model_loaded = joblib.load("my_model.joblib")