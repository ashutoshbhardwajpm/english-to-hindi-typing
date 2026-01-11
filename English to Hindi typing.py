import tkinter as tk
from indic_transliteration.sanscript import transliterate, ITRANS, DEVANAGARI

def update_output(event=None):
    # Get text from input field
    input_text = input_entry.get()
    
    # Word-by-word transliteration
    words = input_text.strip().split(' ')
    hindi_words = []ab 

    for word in words:
        if word.strip():
            hindi_word = transliterate(word, ITRANS, DEVANAGARI)
            hindi_words.append(hindi_word)
    
    output_text = ' '.join(hindi_words)
    
    # Set output
    output_var.set(output_text)

# GUI Setup
root = tk.Tk()
root.title("English to Hindi Transliterator")
root.geometry("600x200")

# Input Field
tk.Label(root, text="Type in English:", font=("Arial", 14)).pack(pady=(10, 0))
input_entry = tk.Entry(root, font=("Arial", 16), width=50)
input_entry.pack(pady=(0, 10))
input_entry.bind("<space>", update_output)
input_entry.bind("<KeyRelease>", update_output)  # For live update (optional)

# Output Field
tk.Label(root, text="Hindi Output:", font=("Arial", 14)).pack(pady=(10, 0))
output_var = tk.StringVar()
output_label = tk.Label(root, textvariable=output_var, font=("Arial", 16), fg="blue")
output_label.pack()

root.mainloop()
