import openai

def gpt3(stext):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=stext,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    content = response["choices"][0].text.split('.')
    print(content)
    return response.choices[0].text

entrada = 'Participação do brasil da segunda guerra mundial'
resposta = gpt3(entrada)
print(resposta)

