# Lab 37: Introduction to Sequence-to-Sequence Models

## Objective

Understand and implement a simple Sequence-to-Sequence model using encoder and decoder networks.

## Tools Used

- Python
- PyTorch
- NumPy
- Matplotlib
- Pandas

## Concepts Covered

- Encoder
- Decoder
- GRU
- SOS token
- EOS token
- Sequence prediction

## Dataset

Small sequence reversal dataset.

Example:

```text
Input:  [2, 3, 4]
Output: [4, 3, 2]
Tasks Performed
Created a small sequence dataset
Built EncoderRNN model
Built DecoderRNN model
Trained Seq2Seq model
Evaluated model output quality
Saved training loss plot
Saved encoder and decoder models
Generated report
Files
seq2seq_model.py
seq2seq_loss_plot.png
encoder_model.pth
decoder_model.pth
seq2seq_report.txt
README.md
Conclusion

This lab introduced Seq2Seq models using a simple encoder-decoder GRU architecture. The model learned to transform an input sequence into an output sequence.
