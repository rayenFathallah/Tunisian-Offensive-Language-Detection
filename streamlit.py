from scraper import extract_comments 
from translation import translate
import streamlit as st
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
import concurrent.futures

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

# Function to apply model to a list of comments
def apply_model_to_comment(comment):
    result = fine_tuned_pipe(comment)
    label = result[0]['label']
    return label_map[int(label.split('_')[1])]  # Extract label from 'LABEL_X' and map it

# Function to run parallel translation and classification
def process_comments(post_id):
    # Step 1: Extract comments
    comments = extract_comments(post_id)  # Pass the post ID to extract comments
    
    # Step 2: Translate comments in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        translated_comments = list(executor.map(translate, comments))  # Assuming `translate` function is defined elsewhere
    
    # Step 3: Show the translated comments in Streamlit
    st.write("Translated Comments:")
    for i, translated_comment in enumerate(translated_comments):
        st.write(f"{i+1}. {translated_comment}")

    # Step 4: Apply the model to each translated comment
    with concurrent.futures.ThreadPoolExecutor() as executor:
        predicted_labels = list(executor.map(apply_model_to_comment, translated_comments))
    
    # Step 5: Count occurrences of each class
    class_counts = {class_name: predicted_labels.count(class_name) for class_name in label_map.values()}
    
    # Step 6: Display the class counts in Streamlit
    st.write("Class Distribution:")
    st.write(class_counts)

# Streamlit input to set post ID
st.title("Post Comment Classification")
post_id = st.text_input("Enter Post ID:")

# Run the process when the post ID is provided
if post_id:
    process_comments(post_id)
