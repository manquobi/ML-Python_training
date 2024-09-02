import os
os.system('cls' if os.name == 'nt' else 'clear')

import numpy
from sklearn import metrics
import matplotlib.pyplot as plt


actual = numpy.random.binomial(1, 0.9, size = 1000)
predicted = numpy.random.binomial(1, 0.9, size = 1000) 
confusion_matrix = metrics.confusion_matrix(actual, predicted) 
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

cm_display.plot()
plt.show() 
Accuracy = metrics.accuracy_score(actual, predicted) 





