from sklearn.preprocessing import OneHotEncoder

def one_hot_encoder(data):
    '''Gevin a category, it creates one-hot encoder

    Parameters:
    data (DataFrame): your category

    Returns:
    data encoded

    Usage example:
    data_cat_1hot = one_hot_encoder(data)
    '''

    cat_encoder = OneHotEncoder()
    return cat_encoder.fit_transform(data)