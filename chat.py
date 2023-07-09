import random
import json
import torch
from model import NeuralNet
from nlp1 import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)
FILE = 'data.pth'
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = 'EyeCare Bot'
print("Welcome to your EyeCare Bot. How can we help you?")
while True:
    sentence = input('You: ')
    if sentence == 'quit' or sentence == 'goodbye' or sentence == 'okay thank you' or sentence == 'thank you bye':
        print('Have a nice day, goodbye')
        break
    if sentence == 'yes, where can i get good eye care?' or sentence == 'yes, i want appointment of eye care specialist':
        print('EyeCare Bot: What area do you live in?')
        sentence = input('You: ')

    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)
    __, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.85:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")

    else:
        print(f"{bot_name}: Can you rephrase your problem.")