from flask import Flask, render_template, request
import transformers

app = Flask(__name__)

# Load AI code generator model
generator = transformers.pipeline("text-generation", model="Salesforce/codegen-350M-mono")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    user_prompt = request.form["prompt"]

    prompt = f"""
Write a program for the following problem:

{user_prompt}

Code:
"""

    result = generator(prompt, max_length=200, num_return_sequences=1)

    code = result[0]["generated_text"]

    return render_template("result.html", code=code)

if __name__ == "__main__":
    app.run(debug=True)