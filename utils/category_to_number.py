from sklearn.preprocessing import OrdinalEncoder

def category_to_number(data):
    '''It converts categories from text to numbers

    Parameters:
    data (DataFrame): your category

    Returns:
    data encoded

    Usage example:
    data_cat_encoded = category_to_number(data)
    '''

    ordinal_encoder = OrdinalEncoder()
    return ordinal_encoder.git_transform(data)