def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert '"knn__n_neighbors"' in __solution__, "Make sure you are setting the knn grid parameter properly."
    assert "GridSearchCV" in __solution__,  "Make sure you are calling the GridSearchCV() function on your param_grid and bb_pipe."
    assert '"knn__weights"' in __solution__, "Make sure you are weighting knn using the 'uniform' and 'distance' metrics."
    assert "cv=10" in __solution__, "Make sure you are using 10-fold cross validation."
    assert "grid_search.fit" in __solution__, "Make sure you are fitting the grid model on the training data."
    assert "grid_search.score" in __solution__, "Make sure you are scoring the model on the test set."
    assert round(bb_test_score,3) == 0.919, "Your model score is incorrect. Are you scoring the model on the test set?"
    assert 'best_params_' in __solution__, "Make sure you are extracting the best parameters from the grid search."
    assert best_hyperparams['knn__n_neighbors'] == 40, "The value for number of neighbors is incorrect. Are you setting up the grid properly?"
    assert best_hyperparams['knn__weights'] == 'uniform', "The value for knn__weights is incorrect. Are you setting up the grid properly?"
    __msg__.good("Nice work, well done!")
