import spacy

nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

def split_sentences(text):
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]
