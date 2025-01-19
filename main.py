import http.client
import json

# Necessary modules imported.

# Establising connection with worqhat's api :
conn = http.client.HTTPSConnection("api.worqhat.com")


# Creating a variable choice with input function, so the user can choose text content or image content.

choice = input("Hello, Enter Prompt 'text' for Content generation or 'image' for Image generation : \n")
# Payload assigned in global scope to prevent errors while running the code -
payload = None
# Main code and implementation starts here.
if choice == "text":
    question = input("Please enter your text prompt for Content Generation : \n")

    # text generation payload -

    payload = json.dumps({
        "question": question,
        "model": "aicon-v4-nano-160824",
        "randomness": 0.7,  # Adjusting for creativity (0.1 to 1.0).
        "stream_data": False,  # Set to True for streamed responses or keep it False
        "training_data": "You are a professional content creator specializing in travel. Write creative, detailed content.",
        "response_type": "text"
    })
    

elif choice == "image":
    question = input("Please enter your text prompt for graphic generation: \n").strip()

    if not question or len(question) < 5:
        print("Error: prompt must be descriptive and non-empty.")
        
        # Image generation payload -

    else:
        print(f"Question received : {question}")
        payload = json.dumps({
            "question": [question],
            "image_style": "Anime",
            "orientation": "Square",
            "response_type": "url",
            "model": "aicon-v4-alpha-160824"
        })

        
if payload:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-8a30fa76afa84c8493b2938f634d34e4'  # API key for authorization (imp)
    }
    # try code block, necessary for making request with APIs -
    try:
        endpoint = "/api/ai/content/v4" if choice == "text" else "/api/ai/images/generate/v2"
        conn.request("POST", "/api/ai/content/v4", payload, headers)
        res = conn.getresponse()
        data = res.read()

        print("\nRespone from Worqhat API :")
        print(data.decode("utf-8"))

    except Exception as e:
        print(f"An error occurred: {e}")

# Closing the connection here.
conn.close()