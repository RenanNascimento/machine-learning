from sklearn.impute import SimpleImputer

def replace_missing_values(data, strategy):
    '''It replaces missing values in your data set by some strategy

    Parameters:
    data (DataFrame): your data
    strategy (str): mean | median | most_frequent | constant

    Returns:
    data transformed

    Usage example:
    X = replace_missing_values(data, "median")
    '''

    imputer = SimpleImputer(strategy=strategy)
    imputer.fit(data)
    return imputer.transform(data)