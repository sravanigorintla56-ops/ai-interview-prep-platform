def evaluate_answer(answer):
    if not answer or len(answer.strip()) < 30:
        return {
            "score": 40,
            "feedback": "Answer is too short. Add specific examples, tools used, and measurable results."
        }

    score = 70
    feedback = []

    keywords = ["project", "result", "improved", "built", "used", "learned", "impact"]

    for keyword in keywords:
        if keyword in answer.lower():
            score += 4

    score = min(score, 100)

    if score >= 85:
        feedback.append("Strong answer. Good detail and impact.")
    else:
        feedback.append("Good start. Add more measurable results and specific tools.")

    return {
        "score": score,
        "feedback": " ".join(feedback)
    }
