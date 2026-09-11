from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="hello, recommend for lunch?"
)

print(response.output_text)