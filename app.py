from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_article', methods=['POST'])
def generate_article():
    prompt = request.form['prompt']
    # Use OpenAI GPT-3 for article generation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500  # Adjust as needed
    )
    generated_article = response['choices'][0]['text']
    return jsonify({'prompt': prompt, 'article': generated_article})

if __name__ == '__main__':
    app.run(debug=True)
