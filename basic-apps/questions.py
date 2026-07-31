"""This file is for the quizz_app"""

QUESTIONS = [
    {
        "question": "What does the regex symbol ^ mean?",
        "options": [
            "A. End of a string",
            "B. Start of a string",
            "C. Any digit",
            "D. Any whitespace"
        ],
        "answer": "B"
    },
    {
        "question": "What does the regex symbol $ mean?",
        "options": [
            "A. Start of a string",
            "B. End of a string",
            "C. Any character",
            "D. One or more occurrences"
        ],
        "answer": "B"
    },
    {
        "question": "Which regex pattern matches one digit?",
        "options": [
            r"A. \w",
            r"B. \s",
            r"C. \d",
            r"D. \D"
        ],
        "answer": "C"
    },
    {
        "question": "Which regex pattern matches one whitespace character?",
        "options": [
            r"A. \s",
            r"B. \d",
            r"C. \w",
            r"D. \b"
        ],
        "answer": "A"
    },
    {
        "question": "What does the * symbol mean in regex?",
        "options": [
            "A. Exactly one occurrence",
            "B. Zero or more occurrences",
            "C. One or more occurrences",
            "D. Exactly two occurrences"
        ],
        "answer": "B"
    },
    {
        "question": "What does the + symbol mean in regex?",
        "options": [
            "A. Zero or more occurrences",
            "B. Zero or one occurrence",
            "C. One or more occurrences",
            "D. End of a string"
        ],
        "answer": "C"
    },
    {
        "question": "Which pattern matches either 'cat' or 'dog'?",
        "options": [
            r"A. cat+dog",
            r"B. cat|dog",
            r"C. cat*dog",
            r"D. cat.dog"
        ],
        "answer": "B"
    },
    {
        "question": "Which pattern matches exactly three digits?",
        "options": [
            r"A. \d+",
            r"B. \d*",
            r"C. \d{3}",
            r"D. \d{1,3}"
        ],
        "answer": "C"
    },
    {
        "question": "What does the dot . usually match in regex?",
        "options": [
            "A. Only a period character",
            "B. Any character except a newline",
            "C. Only letters",
            "D. Only numbers"
        ],
        "answer": "B"
    },
    {
        "question": "Which Python function returns all regex matches?",
        "options": [
            "A. re.match()",
            "B. re.search()",
            "C. re.findall()",
            "D. re.sub()"
        ],
        "answer": "C"
    }
]