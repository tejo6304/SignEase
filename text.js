
genai.configure(api_key="AIzaSyAbL1IhDXpEjbmIELzW6HJZJXE3i5FxF1c")

generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="you are a chat bot which takes list as an input and join the every value and rephrase the errors and give an correct answer and give an meaning sentences or words",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hi\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hello! How can I help you today?\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "['a','a','l','o','w','w']",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I see the list ['a', 'a', 'l', 'o', 'w', 'w']. \n\nIf you'd like me to join these into a single string and remove duplicates, I can do that. The result would be \"alow\".\n\nOr, if you'd like me to join these values into a single string as is, without removing duplicates, the result would be \"aaloww\".\n\nPlease let me know which you'd prefer!\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "neither\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. You don't want either of those options. \n\nTo help me give you the answer you're looking for, could you please tell me what you would like me to do with the list ['a', 'a', 'l', 'o', 'w', 'w']? \n\nFor example, are you looking for:\n\n*   *The number of times each item appears?* (e.g., \"a\": 2, \"l\": 1, \"o\": 1, \"w\": 2)\n*   *A specific order of the items?* (e.g., sorted alphabetically, sorted by frequency)\n*   *Something else entirely?*\n\nThe more information you give me, the better I can assist you!\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "i want a meaning full word out of the given list\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand! You want to rearrange the letters in the list ['a', 'a', 'l', 'o', 'w', 'w'] to form a meaningful word.\n\nThe meaningful word that can be created from these letters is *\"allow\"*.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "p p r o o m m m p t t",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I see the list ['p', 'p', 'r', 'o', 'o', 'm', 'm', 'm', 'p', 't', 't'].\n\nYou're looking for a meaningful word that can be formed by rearranging these letters. \n\nThe word that can be made from these letters is *\"prompt\"*.\n",
      ],
    },
  ]
)
sysinput="p p r o o o m p t t t"
response = chat_session.send_message(sysinput)

print(response.text)