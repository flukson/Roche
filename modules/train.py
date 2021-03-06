import numpy as np
import pandas as pd
import pickle as pkl # tool for object (de)serialization
import sklearn

from common import processed_suffix, getAccuracy

def execute(data_dir, data_file, clf, categorize=False):

    """Performs model training
    Args:
        data_dir (str): relative path to data subdirectory
        data_file (str): name of csv data file
        clf: classifier
        categorize: set to True if Age and Fare should be categorized
    """

    # Split the data for training:
    data = pd.read_csv(data_dir + data_file + processed_suffix + "_" + str(categorize), sep = ';')

    target = data["Survived"]
    del(data["Survived"])

    tr_col = []
    for c in data.columns:
        if c == "Survived":
            pass
        else:
            tr_col.append(c)

    # Fit model and predict on training data:
    clf.fit(data[tr_col], target)
    predictions = clf.predict(data[tr_col])

    # Save model to file:
    model_pickle = open(data_dir + clf.__class__.__name__ + ".pkl", 'wb')
    pkl.dump(clf, model_pickle)
    model_pickle.close()

    # Calculate and print accuracy:
    accuracy = getAccuracy(target, predictions)
    return accuracy
