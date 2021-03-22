#  Debug machine learning classifiers and explain their predictions

# PyPi: https://pypi.org/project/eli5/
# Docs: https://eli5.readthedocs.io/en/latest/

# pip install eli5

"""
Basic Usage
There are two main ways to look at a classification or a regression model:

1. inspect model parameters and try to figure out how the model works globally;
2. inspect an individual prediction of a model, try to figure out why the model makes the decision it makes.

For (1) ELI5 provides eli5.show_weights() function; for (2) it provides eli5.show_prediction() function.
"""

import eli5

eli5.show_weights(clf)

