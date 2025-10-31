import re

def remove_emails(text):
    """Replace all email addresses in text with <EMAIL>."""
    return re.sub(r'\b[\w.-]+?@\w+?\.\w+?\b', '<EMAIL>', text)

def remove_phones(text):
    """Replace phone numbers with <PHONE>."""
    return re.sub(r'\b(\+?\d[\d -]{7,}\d)\b', '<PHONE>', text)

def remove_names_simple(text, names_list):
    """Replace names in names_list with <NAME>."""
    for n in names_list:
        text = re.sub(r'\b' + re.escape(n) + r'\b', '<NAME>', text, flags=re.I)
    return text
