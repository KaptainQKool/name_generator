from config import names
import numpy as np

def generate_name() -> str:
    words_mean = names['words']['mean']
    words_stdev = names['words']['stdev']
    words_min = names['words']['min']
    
    n_words = max(words_min, int(np.random.normal(words_mean, words_stdev)))
    
    name_chars: list[str] = []
    for w in range(n_words):
        length_mean = names['word_length']['mean']
        length_stdev = names['word_length']['stdev']
        length_min = names['word_length']['min']
        
        length = max(length_min, int(np.random.normal(length_mean, length_stdev)))
        
        chars = [l['char'] for l in names['letters'][:]]
        weights = [l['weight'] for l in names['letters'][:]]
        weights_n = [float(i)/sum(weights) for i in weights]
        
        letters: list[str] = np.random.choice(chars, length, p=weights_n)
        letters[0] = letters[0].upper()
        
        if w > 0:
            seps = [l['char'] for l in names['seps'][:]]
            sep_weights = [l['weight'] for l in names['seps'][:]]
            sep_weights_n = [float(i)/sum(sep_weights) for i in sep_weights]
            
            sep: str = np.random.choice(seps, p=sep_weights_n)
            name_chars.append(sep)
        name_chars.extend(letters)
        
    name: str = ''.join(name_chars)
    return name