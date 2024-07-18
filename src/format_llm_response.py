from api import client

model = "gpt-3.5-turbo-16k"
messages = [
  {
    "role": "user",
    "content":
      "Return a JSON containing " 
      "the primary numbers between 0 and 3."
  },
  {
    "role": "assistant",
    "content": """       
      {
        "data": [2, 3, 5, 7],
        "length": 4,
        "smallest": 2,
        "largest": 7,
      }
    """
  },
  {
    "role": "user",
    "content":
      "Return a JSON containing "
      "the primary numbers between 0 and 6."
  },
  {
    "role": "assistant",
    "content": """       
      {
        "data": [2, 3, 5],
        "length": 3,
        "smallest": 2,
        "largest": 5,
      }
    """
  },
  {
    "role": "user",
    "content":
      "Return a JSON containing "
      "the primary numbers between 11 and 65."
  }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
)

print(response.choices[0].message.content)