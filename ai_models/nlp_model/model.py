import spacy
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class NLPModel:
    def __init__(self, model_name='bert-base-uncased'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        outputs = self.model(**inputs)
        return outputs.logits

# Example usage:
# nlp_model = NLPModel()
# print(nlp_model.predict("This is a test sentence."))
