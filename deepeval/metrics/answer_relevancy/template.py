class AnswerRelevancyTemplate:
    @staticmethod
    def generate_statements(actual_output):
        return f"""Given the text, breakdown and generate a list of statements presented. Ambigious, single words, can also be statements.

Example:
Example text: Shoes. The shoes can be refunded at no extra cost. Thanks for asking the question!

{{
    "statements": ["Shoes.", "Shoes can be refunded at no extra cost", "Thanks for asking the question!"]
}}
===== END OF EXAMPLE ======
        
Text:
{actual_output}

**
IMPORTANT: Please make sure to only return in JSON format, with the "statements" key as a list of strings. No words or explaination is needed.
**

JSON:
"""

    @staticmethod
    def generate_verdicts(input, actual_output, retrieval_context):
        return f"""For the provided list of statements, see whether each statement is relevant to address the input.
Please generate a list of JSON with two keys: `verdict` and `reason`.
The 'verdict' key should STRICTLY be either a 'yes', 'idk' or 'no'. Answer 'yes' if the statement is relevant to addressing the original input, 'no' if the statement is irrelevant, and 'idk' if it is ambiguous (eg., not directly relevant but could be used as a supporting point to address the input). You can use the information in the retrieval context to support your deicison.
The 'reason' is the reason for the verdict.
Provide a 'reason' ONLY if the answer is 'no'. 
The provided statements are statements made in the actual output.

**
IMPORTANT: Please make sure to only return in JSON format, with the 'verdicts' key as a list of JSON objects.
Example statements: ["Shoes.", "Thanks for asking the question!", "Is there anything else I can help you with?", "Duck and hide"]
Example retrieval context: ["In the unlikely event of an earthquake, you should duck and hide under a table."]

Example:
Input: What should I do if there is an earthquake?

{{
    "verdicts": [
        {{
            "verdict": "no",
            "reason": "The 'Shoes.' statement made in the acutal output is completely irrelvant to the input, which asks about what to do in the event of an earthquake."
        }},
        {{
            "verdict": "idk"
        }},
        {{
            "verdict": "idk"
        }},
        {{
            "verdict": "yes"
        }}
    ]  
}}

Since you are going to generate a verdict for each statement, the number of 'verdicts' SHOULD BE STRICTLY EQUAL to that of `statements`.
**

Retrieval Context:
{retrieval_context}           

Input:
{input}

Statements:
{actual_output}

JSON:
"""

    @staticmethod
    def generate_reason(irrelevant_statements, input, score):
        return f"""Given the answer relevancy score, the list of reasons of irrelevant statements made in the actual output, and the input, provide a CONCISE reason for the score. Explain why it is not higher, but also why it is at its current score.
The irrelevant statements represent things in the actual output that is ireelevant to addressing whatever is asked/talked about in the input.
If there are nothing irrelevant, just say something positive with an upbeat encouraging tone (but don't overdo it otherwise it gets annoying).

Answer Relevancy Score:
{score}

Reasons why the score can't be higher based on irrelevant statements from actual output:
{irrelevant_statements}

Input:
{input}

Example:
The score is <answer_relevancy_score> because <your_reason>.

Reason:
"""
