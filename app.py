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
    <p>Enter a number, and I'll read your mind!</p>
    <input type="number" id="userNumber" placeholder="Enter a number">
    <button onclick="startMindReading()">Read My Mind</button>
    <div id="loader" class="loader"></div>
    <p id="message" class="hidden"></p>
    
    <script>
        function startMindReading() {
            const number = document.getElementById("userNumber").value;
            const message = document.getElementById("message");
            const loader = document.getElementById("loader");
            
            if (!number) {
                alert("Please enter a number!");
                return;
            }
            
            let steps = [
                "Reading your mind...",
                "Analyzing your thoughts...",
                "Deciphering the secrets of the universe...",
                "Almost there...",
                "Got it!"
            ];
            
            message.classList.add("hidden");
            loader.style.display = "inline-block";
            let index = 0;
            
            let interval = setInterval(() => {
                if (index < steps.length) {
                    message.classList.remove("hidden");
                    message.innerText = steps[index];
                    index++;
                } else {
                    clearInterval(interval);
                    loader.style.display = "none";
                    message.innerText = `You thought about number ${number}! 🤯`;
                }
            }, 2000);
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

