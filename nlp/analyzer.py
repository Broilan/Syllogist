from .tokenizer import tokenize_text, split_sentences
from .validity import is_valid_syllogism

def analyze_syllogism(statement):
    tokens = tokenize_text(statement)
    
    # Extract premises and conclusion
    sentences = split_sentences(statement)
    if len(sentences) < 3:
        return {'error': 'Invalid syllogism format. Expected at least two premises and a conclusion.'}
    
    premises = sentences[:-1]
    conclusion = sentences[-1]
    
    # Check validity
    is_valid = is_valid_syllogism(premises, conclusion)
    
    return {
        'tokens': tokens,
        'premises': premises,
        'conclusion': conclusion,
        'is_valid': is_valid
    }