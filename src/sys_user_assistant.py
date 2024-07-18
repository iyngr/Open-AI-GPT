# The System Role
from api import client

model = "gpt-3.5-turbo-16k"

messages = [
  {
    "role": "system",
    "content": "You are a smart and creative person."
  }
]

response = client.chat.completions.create(
  model=model,
  messages=messages
)
print("System Role")
print(response.choices[0].message.content)

# The User Role
messages = [
    {
      "role": "system",
      "content": "You are a smart assistant."
    },
    {
      "role": "user",
      "content": "Hi there."
    },
    {
      "role": "user",
      "content": "How is everything going?"
    }
]

response = client.chat.completions.create(
  model=model,
  messages=messages
)

print("User Role")
print(response.choices[0].message.content)

# Assistant Role
messages = [
  {
    "role": "user",
    "content":
      "electrons dance the tango of uncertainty,"
      "entangling bits in a choreography that outpaces"
      "the swiftest supercomputers."
  },
  {
    "role": "assistant",
    "content":
      "Electrons Dance the Tango of Uncertainty, "
      "Entangling Bits in a Choreography That Outpaces "
      "the Swiftest Supercomputers."
  },
  {
    "role": "user",
    "content":
      "cloud architectures whisper across the sky, "
      "weaving a tapestry of data that blankets the digital "
      "landscape in a seamless symphony of bytes."
  },
  {
    "role": "assistant",
    "content":
      "Cloud Architectures Whisper Across the Sky, " 
      "Weaving a Tapestry of Data That Blankets the Digital "
      "Landscape in a Seamless Symphony of Bytes."
  },
  {
    "role": "user",
    "content":
      "artificial Intelligence, the alchemist of the digital "
      "age, transmutes raw data into a golden labyrinth of "
      "insights, charting new territories in the realm of "
      "human thought."
  },
  {
    "role": "assistant",
    "content":
      "Artificial Intelligence, the Alchemist of the Digital "
      "Age, Transmutes Raw Data Into a Golden Labyrinth of "
      "Insights, Charting New Territories in the Realm of "
      "Human Thought."
  },
  {
    "role": "user",
    "content":
      "the internet of things is a vast ocean of data, "
      "a sea of information that ebbs and flows "
      "with the tides of time."
  }
]

response = client.chat.completions.create(
  model=model,
  messages=messages,
  temperature=1.2,
)

print("Assistant Role")
print(response.choices[0].message.content)
