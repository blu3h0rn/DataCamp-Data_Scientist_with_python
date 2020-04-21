'''A classification tree divides the feature space into rectangular regions. In contrast,
a linear model such as logistic regression produces only a single linear decision boundary
dividing the feature space into two decision regions.

We have written a custom function called plot_labeled_decision_regions() that you can use to
plot the decision regions of a list containing two trained classifiers. You can
type help(plot_labeled_decision_regions) in the IPython shell to learn more about this function.

X_train, X_test, y_train, y_test, the model dt that
you've trained in an earlier exercise , as well as the function plot_labeled_decision_regions()'''

 #Import LogisticRegression from sklearn.linear_model
from sklearn.linear_model import  LogisticRegression

# Instatiate logreg
logreg = LogisticRegression(random_state=1, solver='lbfgs')

# Fit logreg to the training set
logreg.fit(X_train, y_train)

# Define a list called clfs containing the two classifiers logreg and dt
clfs = [logreg, dt]

# Review the decision regions of the two classifiers
plot_labeled_decision_regions(X_test, y_test, clfs)