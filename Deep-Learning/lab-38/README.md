# Lab 38: Implementing a Simple Attention Mechanism

## Objective

Understand and implement a basic Attention Mechanism in a Seq2Seq-style architecture.

## Concepts Covered

- Query
- Key
- Value
- Attention Weights
- Context Vector
- Sequence Modeling

## Tools Used

- Python
- TensorFlow
- NumPy
- Matplotlib
- Seaborn

## Workflow

1. Prepare Text Data
2. Tokenize Sentences
3. Build LSTM Encoder
4. Add Custom Attention Layer
5. Train Model
6. Visualize Attention Weights
7. Save Model

## Files

```text
simple_attention.py
README.md
attention_model.keras
accuracy_plot.png
attention_heatmap.png
project_report.txt
```

## Results

The model successfully learned attention scores and generated attention heatmaps showing which input tokens received more focus.

## Conclusion

Attention mechanisms improve interpretability and help neural networks focus on important input features, making them a fundamental component of modern NLP architectures such as Transformers.
