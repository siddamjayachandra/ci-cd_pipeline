from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mind Reader</title>
    <style>
        body {
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .hidden {
            display: none;
        }
        .loader {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #3498db;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            display: none;
            margin: 10px auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <h1>Mind Reader</h1>
    <p>Enter a number, and I'll reveal something about your nature!</p>
    <input type="number" id="userNumber" placeholder="Enter a number" min="0" max="99">
    <button onclick="startMindReading()">Read My Mind</button>
    <div id="loader" class="loader"></div>
    <p id="message" class="hidden"></p>
    
    <script>
        const insights = {};
        for (let i = 0; i <= 99; i++) {
            insights[i] = `Your personality is unique and number ${i} represents a special trait in you.`;
        }

        insights[0] = "You have a calm and balanced nature, seeking peace over chaos.";
        insights[1] = "You are a natural leader, always ready to take initiative.";
        insights[2] = "You have a dual personality—sometimes introverted, sometimes extroverted.";
        insights[3] = "You are creative and full of imagination, always thinking outside the box.";
        insights[4] = "You value stability and discipline, preferring structure in life.";
        insights[5] = "You are adventurous and love experiencing new things.";
        insights[6] = "You are a caregiver, always looking after others' well-being.";
        insights[7] = "You are a deep thinker, always questioning the mysteries of life.";
        insights[8] = "You have a strong sense of ambition and strive for success.";
        insights[9] = "You are compassionate and deeply understand emotions.";
        insights[10] = "You are optimistic and always see the bright side of life.";
        insights[99] = "You are an enigma—completely unpredictable!";

        function startMindReading() {
            const number = parseInt(document.getElementById("userNumber").value, 10);
            const message = document.getElementById("message");
            const loader = document.getElementById("loader");

            if (isNaN(number) || number < 0 || number > 99) {
                alert("Please enter a number between 0 and 99!");
                return;
            }

            message.classList.add("hidden");
            loader.style.display = "block";

            setTimeout(() => {
                loader.style.display = "none";
                message.classList.remove("hidden");
                message.innerText = insights[number];
            }, 3000);
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

