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
    <input type="number" id="userNumber" placeholder="Enter a number from 1 to 99" min="1" max="99">
    <button onclick="startMindReading()">Read My Mind</button>
    <div id="loader" class="loader"></div>
    <p id="message" class="hidden"></p>
    
    <script>
        const insights = {
            1: "You are a natural leader, always ready to take initiative.",
            2: "You have a dual personality—sometimes introverted, sometimes extroverted.",
            3: "You are creative and full of imagination, always thinking outside the box.",
            4: "You value stability and discipline, preferring structure in life.",
            5: "You are adventurous and love experiencing new things.",
            6: "You are a caregiver, always looking after others' well-being.",
            7: "You are a deep thinker, always questioning the mysteries of life.",
            8: "You have a strong sense of ambition and strive for success.",
            9: "You are compassionate and deeply understand emotions.",
            10: "You are optimistic and always see the bright side of life.",
            11: "You are a dreamer, always aiming for the stars.",
            12: "You are practical and make well-thought-out decisions.",
            13: "You are mysterious and often misunderstood.",
            14: "You have a sharp mind and excel in analytical thinking.",
            15: "You bring positivity wherever you go.",
            16: "You are a perfectionist, always striving for the best.",
            17: "You are intuitive and trust your gut feelings.",
            18: "You are a great communicator and express yourself well.",
            19: "You are highly independent and self-reliant.",
            20: "You are empathetic and care deeply for others.",
            21: "You are charming and easily make friends.",
            22: "You are disciplined and value hard work.",
            23: "You are spontaneous and enjoy surprises.",
            24: "You are responsible and take your commitments seriously.",
            25: "You are wise beyond your years.",
            26: "You have a great sense of humor.",
            27: "You are passionate and put your heart into everything.",
            28: "You are a problem solver and think critically.",
            29: "You are full of energy and enthusiasm.",
            30: "You are diplomatic and handle conflicts well.",
            31: "You love solitude and self-reflection.",
            32: "You are innovative and love new ideas.",
            33: "You are nurturing and protective of loved ones.",
            34: "You are a realist who sees things as they are.",
            35: "You are a risk-taker and embrace challenges.",
            36: "You are artistic and have a creative soul.",
            37: "You are methodical and detail-oriented.",
            38: "You have a rebellious spirit.",
            39: "You are adaptable and thrive in change.",
            40: "You are generous and love helping others.",
            41: "You are a deep philosopher, always pondering life's mysteries.",
            42: "You seek knowledge and are always learning.",
            43: "You are fearless and embrace the unknown.",
            44: "You are a strategist and think several steps ahead.",
            45: "You are strong-willed and stand by your beliefs.",
            46: "You are a peacemaker and avoid unnecessary conflicts.",
            47: "You are practical and make logical decisions.",
            48: "You are an optimist, even in tough situations.",
            49: "You are introspective and deeply self-aware.",
            50: "You are trustworthy and loyal.",
            61: "You are resourceful and can make the best of any situation.",
            62: "You are intuitive and can sense things before they happen.",
            63: "You are calm under pressure and think rationally.",
            64: "You are resilient and always bounce back from hardships.",
            65: "You are a great listener and people confide in you.",
            66: "You have a charming personality that attracts others.",
            67: "You are constantly seeking wisdom and self-improvement.",
            68: "You have a competitive spirit and strive for excellence.",
            69: "You are deeply connected with emotions and feelings.",
            70: "You are highly disciplined and goal-oriented.",
            71: "You are insightful and see beyond the surface.",
            72: "You bring harmony and balance wherever you go.",
            73: "You are spontaneous and live in the moment.",
            74: "You are adaptable and learn from every experience.",
            75: "You have a great sense of justice and fairness.",
            76: "You are bold and take calculated risks.",
            77: "You have a deep connection with nature and spirituality.",
            78: "You are strong-minded and determined.",
            79: "You are thoughtful and make decisions carefully.",
            80: "You are imaginative and dream big.",
            81: "You are compassionate and care deeply for others.",
            82: "You are a realist with a practical mindset.",
            83: "You are a natural problem solver and thinker.",
            97: "You have an adventurous spirit and love new experiences.",
            98: "You are insightful and always seek wisdom.",
            99: "You are an enigma—completely unpredictable!"
        };
    </script>
</body>
</html>"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

