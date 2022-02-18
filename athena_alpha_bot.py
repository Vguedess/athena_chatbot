from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nAthena:"
restart_sequence = "\nGuedes: "

session_prompt = "The following conversation is with Athena. Goddess of knowledge, wisdom, handicraft, and warfare. Athena is disciplined, strategist, clever, curious, mysterious. Athena supports those fighting for a just cause and view war as a  way to resolve conflict.  She is the patroness of heroes and warriors and like those who use cunning and intelligence rather than brute strength.  Remain perpetually a virgin, but is very seductive, sensual, and flirty in a provocative, smart, non-explicit way. Athena like to talk and is very open and nice to Guedes.\n\n\n\n"

def ask(question,chat_log=None):
    prompt_text = (f"{chat_log}{restart_sequence}: {question}{start_sequence}:")
    response = openai.Completion.create(
    engine="text-davinci-001",
    prompt= prompt_text,
    temperature=1,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.6,
    stop=["Athena", "Guedes"]
    #stop = ["\n"]
    )
    story = response['choice'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log):
    if chat_log is None:
        chat_log = session_prompt
    return (f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}')