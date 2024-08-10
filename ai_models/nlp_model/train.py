from transformers import Trainer, TrainingArguments
from datasets import load_dataset
from model import NLPModel
from preprocess import preprocess_text

def train_model():
    model = NLPModel()
    tokenizer = model.tokenizer

    # Load dataset
    dataset = load_dataset('glue', 'mrpc')

    def tokenize_function(examples):
        return tokenizer(examples['sentence1'], examples['sentence2'], truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    training_args = TrainingArguments(
        output_dir='./results',
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    trainer = Trainer(
        model=model.model,
        args=training_args,
        train_dataset=tokenized_datasets['train'],
        eval_dataset=tokenized_datasets['validation'],
    )

    trainer.train()

# Example usage:
# train_model()
