def get_emotion(text):
    return 'happy' if ':-)' in text and ':-(' not in text else 'sad' if ':-(' in text else 'unsure' if ':-)' in text or ':-(' in text else 'none'
sample_inputs = [
    "How are you :-) doing :-( today :-)?",
    ":)",
    "This:-(is str:-(:-(ange te:-)xt."
]
for input_str in sample_inputs:
    result = get_emotion(input_str)
    print("Input:", input_str)
    print("Output:", result)
    print()