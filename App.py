import tkinter as tk
import speech_recognition as sr

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data)
            output_text.delete(1.0, tk.END)  # Clear previous text
            output_text.insert(tk.END, text)  # Insert transcribed text
            status_label.config(text="Transcription successful!")
        except sr.UnknownValueError:
            status_label.config(text="Could not understand audio")
        except sr.RequestError:
            status_label.config(text="Service is down")

# Tkinter GUI setup
root = tk.Tk()
root.title("Speech-to-Text Converter")

# Label and Button
status_label = tk.Label(root, text="Click 'Start' to begin.")
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start", command=speech_to_text)
start_button.pack(pady=10)

# Text box for displaying output
output_text = tk.Text(root, height=10, width=40)
output_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
