
from cleaning_snippets import remove_emails, remove_phones, remove_names_simple

sample_text = """
Hey Manasa,
Please email me the report at manasa.naik@example.com or call me at +91 98765 43210.
Also, loop in Rajesh and Priya on the thread.
Thanks,
Manasa
"""

names = ["Manasa", "Rajesh", "Priya"]


cleaned = remove_emails(sample_text)
cleaned = remove_phones(cleaned)
cleaned = remove_names_simple(cleaned, names)


print("Original Text:\n", sample_text)
print("\nCleaned Text:\n", cleaned)


with open("cleaned_output.txt", "w", encoding="utf-8") as f:
    f.write(cleaned)
