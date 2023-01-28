import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from string import punctuation
import numpy as np
from collections import Counter


class SentimentLSTM(nn.Module):
    """
    The RNN model that will be used to perform Sentiment analysis.
    """

    def __init__(self, vocab_size, output_size, embedding_dim, hidden_dim,
                 n_layers, bidirectional=False):
        """
        Initialize the model by setting up the layers.
        """
        super(SentimentLSTM, self).__init__()

        self.output_size = output_size
        self.n_layers = n_layers
        self.hidden_dim = hidden_dim

        # embedding and LSTM layers
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers, batch_first=True)

        # linear and sigmoid layer
        if bidirectional:
            self.fc = nn.Linear(hidden_dim * 2, output_size)
        else:
            self.fc = nn.Linear(hidden_dim, output_size)

        self.sig = nn.Sigmoid()

    def forward(self, x):
        """
        Perform a forward pass of our model on some input and hidden state.
        """
        batch_size = x.size(0)
        # x.shape [batch, seq_len]

        # embeddings and lstm_out
        embeds = self.embedding(x)
        # embeds.shape [batch, seq_len, embedding_dim]

        lstm_out, hidden = self.lstm(embeds)
        # lstm_out.shape [batch, seq_len, hidden_dim]
        # hidden[0] [n_layer * n_direction, batch, hidden_dim]
        # hidden[1] (cell) [n_layer * n_direction, batch, hidden_dim]

        # fully connected layer
        out = self.fc(lstm_out[:, -1, :])
        # out.shape: [batch, output_size]

        # sigmoid function
        sig_out = self.sig(out)

        # return last sigmoid output and hidden state
        return sig_out, hidden


def pad_features(reviews_ints, seq_length):
    """
        Return features of review_ints, where each review is padded with 0's
        or truncated to the input seq_length.
    """
    # getting the correct rows x cols shape
    features = np.zeros((len(reviews_ints), seq_length), dtype=int)

    # for each review, I grab that review
    for i, row in enumerate(reviews_ints):
        features[i, -len(row):] = np.array(row)[:seq_length]

    return features


def tokenize_review(test_review):
    test_review = test_review.lower()  # lowercase
    # get rid of punctuatuon
    test_text = ''.join([c for c in test_review if c not in punctuation])

    # splitting by spaces
    test_words = test_text.split()

    # tokens
    test_ints = []
    test_ints.append([vocab_to_int[word] for word in test_words])

    return test_ints


def test(model, test_loader, criterion):
    test_losses = []  # track loss
    num_correct = 0

    model.eval()
    # iterate over test data
    for inputs, labels in test_loader:
        if (train_on_gpu):
            inputs, labels = inputs.cuda(), labels.cuda()

        # get predicted outputs
        output, h = model(inputs)

        # calculate loss
        test_loss = criterion(output.squeeze(), labels.float())
        test_losses.append(test_loss.item())

        # convert output probabilities to predicted class (0 or 1)
        pred = torch.round(output.squeeze())  # rounds to the nearest integer

        # compare predictions to true label
        correct_tensor = pred.eq(labels.float().view_as(pred))
        correct = np.squeeze(correct_tensor.numpy()) if not train_on_gpu else np.squeeze(correct_tensor.cpu().numpy())
        num_correct += np.sum(correct)

    # -- stats! -- ##
    # avg test loss
    print("Test loss: {:.3f}".format(np.mean(test_losses)))

    # accuracy over all test data
    test_acc = num_correct / len(test_loader.dataset)
    print("Test accuracy: {:.3f}".format(test_acc))


def predict(net, test_review, sequence_length=200):
    ''' Prints out whether a give review is predicted to be
        positive or negative in sentiment, using a trained model.

        params:
        net - A trained net
        test_review - a review made of normal text and punctuation
        sequence_length - the padded length of a review
        '''

    net.eval()

    # tokenize review
    test_ints = tokenize_review(test_review)

    # pad tokenize sequence
    seq_length = sequence_length
    features = pad_features(test_ints, seq_length)

    # convert to tensor to pass to model
    feature_tensor = torch.from_numpy(features)

    batch_size = feature_tensor.size(0)

    if (train_on_gpu):
        feature_tensor = feature_tensor.cuda()

    # get the output from the model
    output, h = net(feature_tensor)

    # convert output probabilities to predicted class (0 or 1)
    pred = torch.round(output.squeeze())
    # printing output value, before rounding
    print('Prediction value, pre-rounding: {:.6f}'.format(output.item()))

    # print custom response based on whether test_review is pos/neg
    if pred.item() == 1:
        print('Positive review detected!')
    else:
        print('Negative review detected!')


with open('data/reviews.txt', 'r') as f:
    reviews = f.read()
with open('data/labels.txt', 'r') as f:
    labels = f.read()

# Check the data is loaded well.
print(reviews[:2000])
print()
print(labels[:20])

# Normalization
reviews = reviews.lower() # lowercase, standardize
all_text = ''.join([c for c in reviews if c not in punctuation])

# split by new lines and spaces
reviews_split = all_text.split('\n')
all_text = ' '.join(reviews_split)

# create a list of words
words = all_text.split()

# Check the Normalization is well
print(words[:30])

# Encoding the words
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int = {word: ii for ii, word in enumerate(vocab, 1)}

# use the dict to tokenize each review in reviews_split
# store the tokenized reviews in reviews_ints
reviews_ints = []
for review in reviews_split:
    reviews_ints.append([vocab_to_int[word] for word in review.split()])

# stats about vocabulary
print('Unique words: ', len(vocab_to_int))  # should ~ 74000+
print()

# print tokens in first review
print('review: \n', reviews_split[:1])
print('Tokenized review: \n', reviews_ints[:1])

# 1=positive, 0=negative label conversion
labels_split = labels.split('\n')
encoded_labels = np.array([1 if labels == 'positive' else 0 for labels in labels_split])

# outlier review stats
review_lens = Counter([len(x) for x in reviews_ints])
print("Zero-length reviews: {}".format(review_lens[0]))
print("Maximum review length: {}".format(max(review_lens)))

print('Number of reviews before removing outliers: ', len(reviews_ints))

# remove any reviews/labels with zero length from the reviews_ints list.

# get any indices of any reviews with length 0
non_zero_idx = [ii for ii, review in enumerate(reviews_ints) if len(review) != 0]

# remove 0-length review with their labels
reviews_ints = [reviews_ints[ii] for ii in non_zero_idx]
encoded_labels = np.array([encoded_labels[ii] for ii in non_zero_idx])

print('Number of reviews after removing outliers: ', len(reviews_ints))


# Test your implementation!
seq_length = 200

features = pad_features(reviews_ints, seq_length=seq_length)

# test statements - do not change - ##
assert len(features) == len(reviews_ints), "Your features should have as many rows as reviews."
assert len(features[0]) == seq_length, "Each feature row should contain seq_length values."

# print first 10 values of the first 30 batches
print(features[:30,:10])

split_frac = 0.8

# split data into training, validation, and test data (features and labels, x and y)
split_idx = int(len(features)*0.8)
train_x, remaining_x = features[:split_idx], features[split_idx:]
train_y, remaining_y = encoded_labels[:split_idx], encoded_labels[split_idx:]

test_idx = int(len(remaining_x)*0.5)
val_x, test_x = remaining_x[:test_idx], remaining_x[test_idx:]
val_y, test_y = remaining_y[:test_idx], remaining_y[test_idx:]

# print out the shapes of your resultant feature data
print("\t\t\tFeatures Shapes:")
print("Train set: \t\t{}".format(train_x.shape),
      "\nValidation set: \t{}".format(val_x.shape),
      "\nTest set: \t\t{}".format(test_x.shape))

# create Tensor datasets
train_data = TensorDataset(torch.from_numpy(train_x), torch.from_numpy(train_y))
valid_data = TensorDataset(torch.from_numpy(val_x), torch.from_numpy(val_y))
test_data = TensorDataset(torch.from_numpy(test_x), torch.from_numpy(test_y))

# dataloaders
batch_size = 50

# make sure to SHUFFLE for your training data
train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
valid_loader = DataLoader(valid_data, shuffle=False, batch_size=batch_size)
test_loader = DataLoader(test_data, shuffle=False, batch_size=batch_size)

# obtain one batch of training data
dataiter = iter(train_loader)
sample_x, sample_y = dataiter.next()

print('Sample input size: ', sample_x.size()) # batch_size, seq_length
print('Sample input: \n', sample_x)
print()
print('Sample label size: ', sample_y.size()) # batch_size
print('Sample label: \n', sample_y)

# negative test review
test_review_neg = 'The worst movie I have seen; acting was terrible and I want my money back. This movie had bad acting and the dialogue was slow.'

# positive test review
test_review_pos = 'This movie had the best acting and the dialogue was so good. I loved it.'


# First checking if GPU is available
train_on_gpu = torch.cuda.is_available()

if train_on_gpu:
    print('Training on GPU.')
else:
    print('No GPU available, training on CPU.')

# test code and generate tokenized review
test_ints = tokenize_review(test_review_neg)

# test sequence padding
seq_length = 200
features = pad_features(test_ints, seq_length)

# test conversion to tensor and pass it to model
feature_tensor = torch.from_numpy(features)
print(feature_tensor.size())

# loss and optimization functions
lr = 0.001

criterion = nn.BCELoss()
# optimizer = torch.optim.Adam(net.parameters(), lr=lr)

# Instantiate the model w/ hyperparams

# +1 for zero padding + our word tokens
vocab_size = len(vocab_to_int) + 1
output_size = 1
embedding_dim = 400
hidden_dim = 256
n_layers = 2
bidirectional = True

net2 = SentimentLSTM(vocab_size, output_size, embedding_dim, hidden_dim, n_layers)
net2_state_dict = torch.load('./data/trained.pt')
net2.load_state_dict(net2_state_dict)

optimizer2 = torch.optim.Adam(net2.parameters(), lr=lr)

# call function
# try negative and positive reviews!
seq_length = 200
print('Case 1: ' + test_review_neg)
predict(net2, test_review_neg, seq_length)

print('\nCase 2: ' + test_review_pos)
predict(net2, test_review_pos, seq_length)

test(net2, test_loader, criterion)