import openai

# Set your OpenAI API key
api_key = "sk-proj-mH3dmV3Ip8jwHtVrwG7DT3BlbkFJRtcg6UGU8GKD7hdMRh7S"
openai.api_key = api_key

# Define the prompt for the completion of THIS TASK 
prompt = "Once upon a time"

# Call the OpenAI API to generate a completion NEW BRANCH COMMIT ICIN EK SQUASH BU da DIGER EK
response = openai.Completion.create(
  model="davinci-002",
  prompt=prompt,
  max_tokens=50
)

# Print the generated completion
print(response.choices[0].text.strip())

