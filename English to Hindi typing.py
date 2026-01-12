import tkinter as tk
from indic_transliteration.sanscript import transliterate, ITRANS, DEVANAGARI

def update_output(event=None):
    input_text = input_entry.get()

    words = input_text.strip().split(" ")
    hindi_words = []

    for word in words:
        if word.strip():
            hindi_word = transliterate(word, ITRANS, DEVANAGARI)
            hindi_words.append(hindi_word)

    output_text = " ".join(hindi_words)

    # Update Text widget (clear + insert)
    output_textbox.config(state="normal")
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, output_text)
    output_textbox.config(state="disabled")

def copy_to_clipboard():
    text = output_textbox.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()  # keeps clipboard after app close

# GUI setup
root = tk.Tk()
root.title("English to Hindi Transliterator")
root.geometry("700x300")

# Input section
tk.Label(root, text="Type in English:", font=("Arial", 14)).pack(pady=(10, 0))
input_entry = tk.Entry(root, font=("Arial", 16), width=55)
input_entry.pack(pady=(5, 10))

input_entry.bind("<space>", update_output)
input_entry.bind("<KeyRelease>", update_output)

# Output label
tk.Label(root, text="Hindi Output:", font=("Arial", 14)).pack(pady=(10, 5))

# Output textbox (selectable, block background)
output_textbox = tk.Text(
    root,
    height=3,
    width=55,
    font=("Mangal", 16),
    bg="#f2f2f2",      # light block color
    fg="black",
    wrap="word"
)
output_textbox.pack(pady=(0, 10))
output_textbox.config(state="disabled")

# Copy button
copy_button = tk.Button(
    root,
    text="Copy to Clipboard",
    font=("Arial", 12),
    command=copy_to_clipboard
)
copy_button.pack(pady=5)

root.mainloop()

