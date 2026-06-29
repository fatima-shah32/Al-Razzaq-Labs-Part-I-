# Lab 28: Implementing Early Stopping

## Objective

Understand and implement Early Stopping in a Keras model to reduce overfitting and save training time.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

Synthetic binary classification dataset.

## Early Stopping Configuration

```text
Monitor: val_loss
Patience: 5
Restore Best Weights: True
Maximum Epochs: 100
Tasks Performed
Created synthetic training and validation data
Built a dense neural network
Added EarlyStopping callback
Trained model with maximum 100 epochs
Recorded actual epochs completed
Evaluated validation performance
Saved training plots, history, model, and report
Files
early_stopping_keras.py
early_stopping_model.keras
early_stopping_history.csv
early_stopping_loss.png
early_stopping_accuracy.png
early_stopping_report.txt
README.md
Conclusion

Early stopping monitors validation loss and stops training when improvement ends. It helps save computational resources and can reduce overfitting.
