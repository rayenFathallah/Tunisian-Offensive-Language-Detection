import os
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertModel, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from transformers import pipeline
import random
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the tokenizer
model_path = r"models/fine_tuned_tunibert"  # Use raw string to avoid issues with backslashes on Windows

# Load the tokenizer from the local directory
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)


fine_tuned_pipe = pipeline(
    "text-classification",
    model="models/fine_tuned_tunibert",  # Adjust the path if necessary
    tokenizer=tokenizer,
    device=-1  # Use CPU
)
label_map = {0: 'normal', 1: 'hate', 2: 'abusive'}


random_sample = "ييع عصبة قيس سعيد"
real_label = 2  

results = fine_tuned_pipe(random_sample)

predicted_label = results[0]['label']
predicted_label_index = label_map[int(predicted_label.split('_')[1])]  # Extract label from 'LABEL_X' and map it

print(f"Test Sentence: {random_sample}")
print(f"Real Label: {label_map[real_label]}")
print(f"Predicted Label: {predicted_label_index}, with confidence score: {results[0]['score']}")