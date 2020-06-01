import numpy as np
import pandas as pd


from sklearn.base import BaseEstimator, TransformerMixin


# frequent label categorical encoder
class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, tol=0.01, variables=None):

        self.tol = tol

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):

        # persist frequent labels in dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            # the encoder will learn the most frequent categories
            label_frequency = pd.Series(
                X[var].value_counts() / np.float(len(X)))
            # frequent labels:
            self.encoder_dict_[var] = list(
                label_frequency[label_frequency >= self.tol].index)

        return self

    def transform(self, X):
        X_copy = X.copy()
        for feature in self.variables:
            X_copy[feature] = np.where(X[feature].isin(self.encoder_dict_[
                feature]), X[feature], 'Rare')

        return X_copy


# string to numbers categorical encoder
class CategoricalEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        temp = pd.concat([X, y], axis=1)
        temp.columns = list(X.columns) + ['target']

        # persist transforming dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            ordered_labels = temp.groupby([var])['target'].mean(
            ).sort_values(ascending=True).index
            self.encoder_dict_[var] = {k: i for i,
                                       k in enumerate(ordered_labels, 0)}

        return self

    def transform(self, X):
        # encode labels
        X_copy = X.copy()
        for feature in self.variables:
            X_copy[feature] = X[feature].map(self.encoder_dict_[feature])

        return X_copy
