from flask import Flask,render_template,request
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/analyze",methods=["POST"])
def analyze():
    code=request.form["code"]
    prompt = f"""
You are an expert software engineer.

Analyze the following code.

Return the answer in this format:

Programming Language:
If no bugs are found, clearly say:
"No bugs found. The code is syntactically and logically correct based on the provided snippet."


🔍 Issues Found

🛠 Suggested Fixes

📖 Explanation

⭐ Best Practices
Code:
{code}
"""

            response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    result = response.choices[0].message.content
    return render_template(
        "index.html", 
        result=result)
   
if __name__ == "__main__":
    app.run(debug=True)
