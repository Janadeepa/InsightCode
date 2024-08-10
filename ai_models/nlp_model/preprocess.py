import re

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Example usage:
# processed_text = preprocess_text("This is a sample text, with punctuation!")
# print(processed_text)
