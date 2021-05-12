import numpy as np

def split_train_test(data, test_ratio):
    '''It splits your data into train and test set using a random sampling method

    Parameters:
    data (DataFrame): your data
    test_ratio (int): test set size in percentage

    Returns:
    train_set, test_set

    Usage example:
    train_set, test_set = split_train_test(data, 0.2)
    len(train_set)
    len(test_set)
    '''

    np.random.seed(42) # it allows to always generate the same shuffled indices
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]