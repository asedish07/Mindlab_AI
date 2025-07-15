from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client()

def summarize(text):
  summary = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{text}\n\n위 글을 요약만 해줘",
  )

  return summary.text


def generate_Q(summary):
  gen_question = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{summary}\n\n위 글을 보고 예시 문제만 하나 만들어줘. $기호를 쓰지 말고"
  )

  return gen_question.text


def Q_explanation(question):
  explanation = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{question}\n\n위 문제를 보고 해설만 짧게 해줘."
  )

  return explanation.text