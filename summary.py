from transformers import pipeline, T5Tokenizer
from transcribe import *

"""
The code below loads the T5 tokenizer for the Lithuanian news, then it sets up the summarization pipeline with 
a specific model. After that, it cleans up the transcription text by removing extra spaces and generates a summary. 
Finally, it prints the summary and saves it to a text file.
"""

tokenizer = T5Tokenizer.from_pretrained("LukasStankevicius/t5-base-lithuanian-news-summaries-175",
                                        cache_dir='/Users/simonagelzinyte/Huggin_Face/')

summarizer = pipeline(
    task="text2text-generation",
    model="LukasStankevicius/t5-base-lithuanian-news-summaries-175",
    tokenizer=tokenizer,
    framework="pt",
    model_kwargs={"cache_dir": '/Users/simonagelzinyte/Huggin_Face/'},
)

transcription = ' '.join(transcription.strip().split())

summary = summarizer(transcription)[0]['generated_text']

print("Summary:", summary)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)