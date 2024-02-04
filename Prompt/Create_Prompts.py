# 1. Scene Analysis Prompt
def Generate_Scene_Analysis_Prompt(Source_sentence):
    prompt = f"""
Perform a Scene Analysis on the the following Source Sentence:
Source Sentence: {Source_sentence}
Analyze the context on the following source sentence and consider how this context impacts the translation strategy.
Analysis:"""
    return prompt.strip()

# 2. Target Audience Analysis Prompt
def Generate_Target_Audience_Analysis_Prompt(Source_sentence):
    prompt = f"""
Perform a Target Audience Analysis on the the following Source Sentence:
Source Sentence: {Source_sentence}
Describe and analyze the characteristics of the target audience, discussing how these characteristics influence the translation.
Analysis:"""
    return prompt.strip()

# 3. Key Information Analysis Prompt Prompt
def Generate_Key_Information_Analysis_Prompt(Source_sentence):
    prompt = f"""
Perform a Key Information Analysis on the the following Source Sentence:
Source Sentence: {Source_sentence}
Identify and analyze the key information in the source sentence, discussing how to maintain this information's integrity in the translation.
Analysis:"""
    return prompt.strip()

# 4. Intent Analysis Prompt
def Generate_Intent_Analysis_Prompt(Source_sentence):
    prompt = f"""
Perform a Intent Analysis on the the following Source Sentence:
Source Sentence: {Source_sentence}
Analyze the original intent of the source sentence and its impact on the translation strategy.
Analysis:"""
    return prompt.strip()

# 5. Information Equivalence Analysis Prompt
def Generate_Information_Equivalence_Analysis_Prompt(Source_sentence, tgt):
    prompt = f"""
Perform a Information Equivalence Analysis on the the following Source Sentence:
Source Sentence: {Source_sentence}
Analyze how to convey the same information and emotions of the source sentence in the {tgt}.
Analysis:"""
    return prompt.strip()

# 6. Cultural Equivalence Analysis Prompt
def Generate_Cultural_Equivalence_Analysis_Prompt(Source_sentence, tgt):
    prompt = f"""
Perform a Cultural Equivalence Analysis on the the following Source Sentence:
Source Sentence: {Source_sentence}
Discuss the differences between the source and {tgt} cultures, and analyze how these differences impact the translation.
Analysis:"""
    return prompt.strip()

# 7. Text Type Analysis Prompt
def Generate_Text_Type_Analysis_Prompt(Source_sentence):
    prompt = f"""
Perform a Text Type Analysis on the following Source Sentence:
Source Sentence: {Source_sentence}
Determine the text type of the source sentence (informative, expressive, operative) and analyze how this classification guides the translation strategy.
Analysis:"""
    return prompt.strip()

# T1. Single Analysis Translate Prompt
def Generate_Single_Analysis_Translate_Prompt(Source_sentence, Analysis, src, tgt):
    prompt = f"""
Source sentence: {Source_sentence}
Analysis: {Analysis}
Please give the best translation from {src} to {tgt} based on the above analysis without explanation.
Best Translation:"""
    return prompt.strip()

# T2. Translate Prompt
def Generate_Translate_Prompt(Source_sentence, src, tgt):
    prompt = f"""
Source sentence: {Source_sentence}
Please give the best translation from {src} to {tgt} without explanation.
Best Translation:"""
    return prompt.strip()

