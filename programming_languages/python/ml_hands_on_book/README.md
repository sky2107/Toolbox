# ML

> Installation

    # scikit
    conda install -c anaconda scikit-learn
    # matplotlib
    conda install -c conda-forge matplotlib
    # numpy
    conda install -c conda-forge numpy
    # pandas
    conda install -c conda-forge pandas
    # updated anaconda
    conda update -n base -c defaults conda

> Question concerning the book

* from six.moves import urllib
* import matplotlib as mpl
* import matplotlib.pyplot as plt
* from zlib import crc32

> redo function did not understood the above code

    import hashlib

    def test_set_check(identifier, test_ratio, hash=hashlib.md5):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

    ------------------------------------------------------------------------
    from zlib import crc32

    def test_set_check(identifier, test_ratio):
        return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

    def split_train_test_by_id(data, test_ratio, id_column):
        ids = data[id_column]
        in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
        return data.loc[~in_test_set], data.loc[in_test_set]