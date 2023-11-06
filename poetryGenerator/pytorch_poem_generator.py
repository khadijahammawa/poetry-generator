from transformers import pipeline

pipeline = pipeline("text-generation", model="striki-ai/william-shakespeare-poetry")

def generate_poetry(prompt):
    generated_text = pipeline(
        prompt, 
        max_length=100, 
        do_sample=True, 
        temperature=0.85,      # Adjust temperature for creativity
    )[0]['generated_text']

    print(generated_text)

    return generated_text

#model = TFGPT2LMHeadModel.from_pretrained("striki-ai/william-shakespeare-poetry", from_pt=True)