import transformers

tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-cased")
model = transformers.pipeline("summarization")