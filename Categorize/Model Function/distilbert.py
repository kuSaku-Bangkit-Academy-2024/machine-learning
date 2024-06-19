import os
import sys
import pickle
import tensorflow as tf
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
import logging

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Suppress Hugging Face Transformers logs
logging.getLogger("transformers").setLevel(logging.ERROR)

# Load the tokenizer and model
model_path = './distilbert/saved_model'
tokenizer_path = 'distilbert/saved_model'

tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_path)
model = TFDistilBertForSequenceClassification.from_pretrained(model_path)

# Load category mappings
with open('category_to_id.pkl', 'rb') as f:
    category_to_id = pickle.load(f)

with open('id_to_category.pkl', 'rb') as f:
    id_to_category = pickle.load(f)

def predict_category(note):
    """
    Predicts the category for a single note.

    Args:
        note (str): The note text to classify.

    Returns:
        str: The predicted category for the note.
    """
    inputs = tokenizer(note, return_tensors='tf', truncation=True, padding=True)
    logits = model(inputs).logits
    predicted_class_id = tf.argmax(logits, axis=1).numpy()[0]
    return id_to_category[predicted_class_id]

def predict_batch(notes):
    """
    Predicts the categories for a list of notes.

    Args:
        notes (list of str): The list of note texts to classify.

    Returns:
        list of str: The list of predicted categories for the notes.
    """
    inputs = tokenizer(notes, return_tensors='tf', truncation=True, padding=True)
    logits = model(inputs).logits
    predicted_class_ids = tf.argmax(logits, axis=1).numpy()
    return [id_to_category[class_id] for class_id in predicted_class_ids]

if __name__ == "__main__":
    notes = ["Dinner at a restaurant", "Monthly salary", "Car", "HighSchool", "McDonalds"]
    categories = predict_batch(notes)
    for note, category in zip(notes, categories):
        print(f"Note: {note} - Predicted Category: {category}")
