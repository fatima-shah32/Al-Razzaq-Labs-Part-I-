# Lab 24: Custom Loss Functions in Keras

## Objective

Understand how to define, integrate, train, and evaluate a model using a custom loss function in Keras.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

Synthetic regression dataset.

## Custom Loss Function

```python
def custom_mse(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))
Tasks Performed
Defined a custom MSE loss function
Created synthetic training and validation data
Built a simple neural network
Compiled model using custom loss
Trained and evaluated the model
Compared custom MSE with built-in MSE
Saved results, plot, models, and report
Files
custom_loss_keras.py
custom_loss_results.csv
training_history.csv
custom_loss_comparison.png
model_custom_loss.keras
model_builtin_mse.keras
custom_loss_report.txt
README.md
Conclusion

This lab demonstrated how custom loss functions can be used in Keras. Custom losses give flexibility when standard loss functions do not fully match the problem requirements.
