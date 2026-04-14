import fast_text_proc

text = "Hello World! This is a test. Contact us at info@example.com."

# Tokenize
tokens = fast_text_proc.fast_tokenize(text)
print(tokens) # ['hello', 'world', 'this', 'is', 'a', 'test', 'contact', 'us', 'at', 'info@example.com']

# Clean
cleaned = fast_text_proc.clean_text(text)
print(cleaned) # "hello world this is a test contact us at info@example.com"

# Extract Emails
emails = fast_text_proc.extract_emails(text)
print(emails) # ['info@example.com']

# Batch Processing (Parallel)
texts = [text] * 1000
results = fast_text_proc.batch_tokenize(texts)