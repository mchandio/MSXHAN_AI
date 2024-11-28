from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pickle

app = Flask(__name__)

# Load the DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

history = []

@app.route('/')
def home():
    return render_template('index.html')  # Assuming index.html exists

@app.route('/chat', methods=['POST'])
def chat():
    try:
        text = request.form['text']
        history.append(text)
        context = " ".join(history[-50:])  # Adjust history length as needed

        # Tokenize the input and generate response
        input_ids = tokenizer.encode(context, return_tensors="pt")
        input_ids = input_ids[:, -model.config.n_positions:]  # Ensure input doesn't exceed model's max length

        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # Create an attention mask

        response = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=50,  # Reducing the max_new_tokens for faster response, adjust as needed
            num_beams=4,
            early_stopping=True,
            pad_token_id=tokenizer.eos_token_id  # Set the pad_token_id
        )

        generated_text = tokenizer.decode(response[0], skip_special_tokens=True)
        return jsonify({'response': generated_text})

    except Exception as e:
        print(f"Error: {str(e)}")  # Log the error for debugging
        return jsonify({'error': "An error occurred. Please try again."})

if __name__ == '__main__':
    app.run(debug=True)
