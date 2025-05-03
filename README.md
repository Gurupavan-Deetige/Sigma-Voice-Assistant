# 🤖 Sigma - Offline Voice Assistant

**Sigma** is an intelligent offline voice assistant built using Python. It listens to your voice commands, understands them, and performs actions like opening apps, responding with speech, and more — all without needing an internet connection.

---

## 📁 Folder Structure

Sigma/
├── assets/ # For any sound/image assets
├── config/
│ └── settings.json # Assistant settings (activation word, voice, etc.)
├── modules/
│ ├── voice_input.py # Handles voice recognition
│ ├── text_to_speech.py # Handles speech output
│ ├── command_parser.py # Interprets commands
│ ├── system_control.py # Runs actions like open apps
│ ├── security.py # Future security features
│ └── personality.py # Handles assistant personality
├── main.py # Main execution file
├── requirements.txt # List of Python libraries
└── README.md # Project documentation

---

## 🚀 Features

- 🎤 Voice Recognition (Offline)
- 🗣 Text-to-Speech Response
- 💻 System Command Execution
- 🔐 Modular Design for Future Security Features
- 🤖 Configurable Personality
- 📦 Light & Fast – Works on Raspberry Pi and low-end PCs

---

## ⚙️ Technologies Used

- `SpeechRecognition`
- `pyttsx3`
- `os`, `platform`, `json`, `subprocess`
- Python 3.13.3

---

## 🧪 How to Run

1. **Install Python 3.13.3 or higher**
2. **Clone the repository**  
   ```bash
   git clone https://github.com/Gurupavan-Deetige/Sigma.git
   cd Sigma

Install the requirements
pip install -r requirements.txt

Run the assistant
python main.py

👨‍💻 Author
Made with ❤️ by Gurupavan
GitHub: @Gurupavan-Deetige
📜 License
This project is licensed under the MIT License.


