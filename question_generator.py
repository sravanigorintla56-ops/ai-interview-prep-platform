TECHNICAL_KEYWORDS = {
    "python": [
        "Explain list comprehension in Python.",
        "What is the difference between a list and a tuple?",
        "How do you handle exceptions in Python?"
    ],
    "machine learning": [
        "What is overfitting?",
        "Explain train-test split.",
        "What is the difference between classification and regression?"
    ],
    "sql": [
        "What is the difference between WHERE and HAVING?",
        "Explain INNER JOIN vs LEFT JOIN.",
        "How do you optimize a SQL query?"
    ],
    "api": [
        "What is REST API?",
        "Explain GET vs POST.",
        "How do you secure an API?"
    ]
}

HR_QUESTIONS = [
    "Tell me about yourself.",
    "Why are you interested in this role?",
    "Tell me about a project you are proud of.",
    "Describe a challenge you faced and how you solved it.",
    "Where do you see yourself in 5 years?"
]

def generate_questions(resume_text, job_description):
    combined = (resume_text + " " + job_description).lower()
    questions = []

    for keyword, keyword_questions in TECHNICAL_KEYWORDS.items():
        if keyword in combined:
            questions.extend(keyword_questions)

    if not questions:
        questions = [
            "Explain your strongest technical project.",
            "What programming language are you most comfortable with?",
            "How do you approach debugging?"
        ]

    return questions[:10], HR_QUESTIONS
