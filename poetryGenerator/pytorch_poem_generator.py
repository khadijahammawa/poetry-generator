from transformers import pipeline
import re

# Choose the model you want to use
model = "gpt2"  # or another model like "gpt2-medium", "gpt2-large", etc.

# Set up the text generation pipeline with the chosen model
generator = pipeline("text-generation", model=model, device="cpu")  # set device to CPU



def generate_rhymed_poem(prompt, num_lines=4):
    attempts = 10  # Number of generation attempts to find a rhyme
    poem_lines = []
    last_word = None

    for _ in range(num_lines):
        for _ in range(attempts):
            # Generating strings based on the previous rhyme
            generated = generator(prompt, max_length=40, num_return_sequences=1)[0]['generated_text']
            line = generated[len(prompt):].split('\n')[0]  # We take only the first generated line
            line = re.sub(r'[^\w\s]', '', line)  # delete punctuation for easier 
            words = line.strip().split()
            if words:
                new_last_word = words[-1]
                if not last_word or rhymes(last_word, new_last_word):  # check rhyme
                    poem_lines.append(line)
                    prompt += '\n' + line
                    last_word = new_last_word
                    break
    res = '\n'.join(poem_lines)
    print(res)
    return res

def rhymes(word1, word2):
    return word1[-2:] == word2[-2:]  # simple check for rhyme

