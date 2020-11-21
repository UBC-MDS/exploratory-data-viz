#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:36:56 2020

@author: elijah
"""
def test():
    import altair
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'KNeighborsClassifier(n_neighbors=k)' in __solution__, "Make sure you are using the KNeighborsClassifier() with the n_neighbors argument."
    assert 'cross_validate(model, X_train, y_train, cv=10, return_train_score=True)' in __solution__, "Make sure you are passing the model to the cross validation function"
    assert 'results_dict["n_neighbors"].append(k)' in __solution__, "Make sure you are appending the number of neighbors correctly."
    assert "alt.Y" in __solution__, "Make sure you are plotting the score on the y-axis."
    assert isinstance(chart1,altair.vegalite.v4.api.Chart), "Make sure you are generating an altair chart."
    __msg__.good("Nice work, well done!")
