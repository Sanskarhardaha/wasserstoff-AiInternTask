BAD_WORDS = {"badword1", "badword2"}

def check_profanity(text):
    return any(bad in text.lower() for bad in BAD_WORDS)