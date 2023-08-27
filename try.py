import pyperclip

text_to_copy = "This is the text you want to copy."
pyperclip.copy(text_to_copy)

# Check if the clipboard content matches the text that was copied
clipboard_content = pyperclip.paste()
if clipboard_content == text_to_copy:
    print("Text has been successfully copied to the clipboard.")
else:
    print("Text was not copied to the clipboard.")

# Print the current clipboard content for verification
print("Clipboard content:", clipboard_content)
