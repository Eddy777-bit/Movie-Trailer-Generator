from transformers import pipeline

# Use sentiment analysis for impactful dialogues
def analyze_dialogues(dialogues):
    sentiment_analyzer = pipeline('sentiment-analysis')
    results = sentiment_analyzer(dialogues)
    impactful_lines = [
        dialogue for dialogue, result in zip(dialogues, results) 
        if result["label"] == "POSITIVE" and result["score"] > 0.9
    ]
    return impactful_lines

# Example usage
dialogues = [
    "This is the moment we fight for our freedom!",
    "Everything will be fine.",
    "The enemy is too strong; we cannot win."
]
selected_dialogues = analyze_dialogues(dialogues)
print("Impactful Dialogues:", selected_dialogues)
