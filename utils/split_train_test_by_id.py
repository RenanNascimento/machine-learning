from zlib import crc32

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    '''It splits your data into train and test set by creating a hash to each `id`

    Parameters:
    data (DataFrame): your data
    test_ratio (int): test set size in percentage
    id_column (str): id column name

    Returns:
    train_set, test_set

    Usage example:
    train_set, test_set = split_train_test_by_id(data, 0.2, "index")
    len(train_set)
    len(test_set)
    '''

    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]