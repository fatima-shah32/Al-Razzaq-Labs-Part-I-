import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

print("=== Lab 37: Introduction to Sequence-to-Sequence Models ===")

SOS_token = 0
EOS_token = 1

# Small sequence dataset
# Input sequence will be reversed as output sequence
pairs = [
    ([2, 3, 4], [4, 3, 2]),
    ([5, 6, 7], [7, 6, 5]),
    ([8, 9, 10], [10, 9, 8]),
    ([11, 12, 13], [13, 12, 11]),
    ([14, 15, 16], [16, 15, 14])
]

vocab_size = 20
hidden_size = 32


class EncoderRNN(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(EncoderRNN, self).__init__()

        self.hidden_size = hidden_size
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.rnn = nn.GRU(hidden_size, hidden_size)

    def forward(self, input_token, hidden):
        embedded = self.embedding(input_token).view(1, 1, -1)
        output, hidden = self.rnn(embedded, hidden)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size)


class DecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size):
        super(DecoderRNN, self).__init__()

        self.hidden_size = hidden_size
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.rnn = nn.GRU(hidden_size, hidden_size)
        self.out = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input_token, hidden):
        output = self.embedding(input_token).view(1, 1, -1)
        output = nn.functional.relu(output)
        output, hidden = self.rnn(output, hidden)
        output = self.softmax(self.out(output[0]))
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, 1, self.hidden_size)


def tensor_from_sequence(sequence):
    sequence = sequence + [EOS_token]
    return torch.tensor(sequence, dtype=torch.long).view(-1, 1)


encoder = EncoderRNN(vocab_size, hidden_size)
decoder = DecoderRNN(hidden_size, vocab_size)

encoder_optimizer = optim.Adam(encoder.parameters(), lr=0.01)
decoder_optimizer = optim.Adam(decoder.parameters(), lr=0.01)

criterion = nn.NLLLoss()
losses = []


def train(input_tensor, target_tensor):
    encoder_hidden = encoder.initHidden()

    encoder_optimizer.zero_grad()
    decoder_optimizer.zero_grad()

    loss = 0

    input_length = input_tensor.size(0)
    target_length = target_tensor.size(0)

    for ei in range(input_length):
        encoder_output, encoder_hidden = encoder(
            input_tensor[ei],
            encoder_hidden
        )

    decoder_input = torch.tensor([[SOS_token]])
    decoder_hidden = encoder_hidden

    for di in range(target_length):
        decoder_output, decoder_hidden = decoder(
            decoder_input,
            decoder_hidden
        )

        loss += criterion(decoder_output, target_tensor[di])

        topv, topi = decoder_output.topk(1)
        decoder_input = topi.detach()

        if decoder_input.item() == EOS_token:
            break

    loss.backward()

    encoder_optimizer.step()
    decoder_optimizer.step()

    return loss.item() / target_length


print("\nTraining Seq2Seq model...")

for epoch in range(1, 301):
    total_loss = 0

    for input_seq, target_seq in pairs:
        input_tensor = tensor_from_sequence(input_seq)
        target_tensor = tensor_from_sequence(target_seq)

        loss = train(input_tensor, target_tensor)
        total_loss += loss

    avg_loss = total_loss / len(pairs)
    losses.append(avg_loss)

    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {avg_loss:.4f}")


def evaluate(sequence, max_length=5):
    with torch.no_grad():
        input_tensor = tensor_from_sequence(sequence)
        input_length = input_tensor.size(0)

        encoder_hidden = encoder.initHidden()

        for ei in range(input_length):
            encoder_output, encoder_hidden = encoder(
                input_tensor[ei],
                encoder_hidden
            )

        decoder_input = torch.tensor([[SOS_token]])
        decoder_hidden = encoder_hidden

        decoded_tokens = []

        for di in range(max_length):
            decoder_output, decoder_hidden = decoder(
                decoder_input,
                decoder_hidden
            )

            topv, topi = decoder_output.topk(1)

            if topi.item() == EOS_token:
                break

            decoded_tokens.append(topi.item())
            decoder_input = topi.detach()

        return decoded_tokens


# Evaluate model
test_sequence = [2, 3, 4]
expected_output = [4, 3, 2]
prediction = evaluate(test_sequence)

print("\nModel Evaluation")
print("Input Sequence:", test_sequence)
print("Predicted Output Sequence:", prediction)
print("Expected Output Sequence:", expected_output)

# Save loss plot
plt.figure(figsize=(8, 5))
plt.plot(losses)
plt.title("Seq2Seq Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.tight_layout()
plt.savefig("seq2seq_loss_plot.png")
plt.close()

# Save model files
torch.save(encoder.state_dict(), "encoder_model.pth")
torch.save(decoder.state_dict(), "decoder_model.pth")

# Save report
with open("seq2seq_report.txt", "w") as file:
    file.write("Lab 37: Introduction to Sequence-to-Sequence Models\n\n")
    file.write("Model: Encoder GRU + Decoder GRU\n")
    file.write("Dataset: Small sequence reversal dataset\n\n")
    file.write(f"Input Sequence: {test_sequence}\n")
    file.write(f"Predicted Output Sequence: {prediction}\n")
    file.write(f"Expected Output Sequence: {expected_output}\n\n")
    file.write("Seq2Seq models convert one sequence into another sequence.\n")
    file.write("Encoder processes the input sequence and decoder generates the output sequence.\n")

print("\nFiles saved:")
print("seq2seq_loss_plot.png")
print("encoder_model.pth")
print("decoder_model.pth")
print("seq2seq_report.txt")

print("\nLab completed successfully.")
