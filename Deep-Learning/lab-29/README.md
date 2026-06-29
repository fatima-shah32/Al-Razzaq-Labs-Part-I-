# Lab 29: Model Checkpointing

## Objective

Understand and implement model checkpointing in Keras to save the best model weights during training.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

MNIST handwritten digit dataset.

## Checkpoint Configuration

```text
Monitor: val_accuracy
Save Best Only: True
Save Weights Only: True
Mode: max
File: checkpoints/best_model.weights.h5
Tasks Performed
Loaded and normalized MNIST dataset
Built a dense neural network
Added ModelCheckpoint callback
Trained model with checkpointing enabled
Saved best validation accuracy weights
Reloaded saved weights
Evaluated saved checkpoint model
Saved plots, history, final model, and report
Files
model_checkpointing.py
checkpoints/best_model.weights.h5
best_checkpoint_model.keras
checkpoint_training_history.csv
checkpoint_accuracy_plot.png
checkpoint_loss_plot.png
checkpoint_report.txt
README.md
Conclusion

Model checkpointing is useful for preserving the best model state during training. It protects progress and allows the best model weights to be reloaded for evaluation or deployment.
