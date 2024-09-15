
# K-Nearest Neighbors (KNN) Project

## Team Member
- Aaron Campbell
- Email: campbella20@students.ecu.edu

## Quick Start
This project implements the K-Nearest Neighbors (KNN) algorithm on the Iris dataset. 
To run the code, follow these steps:

1. **Clone the repository**: Use `git clone <repository-url>` to clone the project.
2. **Install dependencies**: Ensure you have the following Python packages installed:
   - pandas
   - numpy
   - matplotlib
   - scikit-learn
   - random
   - math
   - operator
3. **Run the Jupyter notebook**: Open the Jupyter notebook in your preferred environment and execute the cells to see the KNN algorithm in action.

## Results
The following average accuracies were achieved for different values of k:

```
k=1, Average Accuracy: 94.80%
k=2, Average Accuracy: 95.20%
k=3, Average Accuracy: 94.00%
k=4, Average Accuracy: 96.80%
k=5, Average Accuracy: 95.20%
k=6, Average Accuracy: 97.60%
k=7, Average Accuracy: 97.20%
k=8, Average Accuracy: 98.80%
k=9, Average Accuracy: 98.00%
k=10, Average Accuracy: 96.40%
k=11, Average Accuracy: 98.00%
k=12, Average Accuracy: 97.20%
k=13, Average Accuracy: 97.20%
k=14, Average Accuracy: 95.20%
k=15, Average Accuracy: 97.20%
k=16, Average Accuracy: 94.00%
k=17, Average Accuracy: 96.00%
k=18, Average Accuracy: 96.00%
k=19, Average Accuracy: 96.00%
k=20, Average Accuracy: 94.00%
```

## Best K Value
The best k value based on the average accuracy is k=8, with an accuracy of 98.80%.

Since all K's have similar accuracy it could indicate that the dataset has a clear structure and that the distance metrics used are effective at classifying the instances. 
Also, the slight variations in accuracy might also suggest that the choice of k has a minor impact on the overall performance for this specific dataset.

## Line Chart
The line chart is in the Github Repo