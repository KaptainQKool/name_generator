from .config import names
from pathlib import Path
from typing import Any
import numpy as np

def generate(
        n: int | None = None,
        config: dict[str, Any] = names,
        save_output: bool = False,
        print_output: bool = True
    ) -> str | list[str]:
    
    this_dir: str = str(Path(__file__).parent.resolve())
    
    if n:
        names: list[str] = []
        for _ in range(n):
            names.append(single_name(config))
        
        if save_output:
            with open(this_dir+'/output/names.txt', 'w') as out:
                out.write('\n'.join(names))
        if print_output:
            print('\n'.join(names))
        
        return names
    else:
        name: str = single_name(config)
        
        if save_output:
            with open(this_dir+'/output/names.txt', 'w') as out:
                out.write(name)
        if print_output:
            print(name)
                
        return name


def single_name(config: dict[str, Any] = names) -> str:
    words_mean = config['words']['mean']
    words_stdev = config['words']['stdev']
    words_min = config['words']['min']
    
    n_words = max(words_min, int(np.random.normal(words_mean, words_stdev)))
    
    name_chars: list[str] = []
    for w in range(n_words):
        length_mean = config['word_length']['mean']
        length_stdev = config['word_length']['stdev']
        length_min = config['word_length']['min']
        
        length = max(length_min, int(np.random.normal(length_mean, length_stdev)))
        
        chars = [l['char'] for l in config['letters'][:]]
        weights = [l['weight'] for l in config['letters'][:]]
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