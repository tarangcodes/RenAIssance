import http.client
import json

# Task 1: Establish a connection to WorqHat's API
conn = http.client.HTTPSConnection("api.worqhat.com")

# New Task : Use If-elif-else for ai to generate 2 types of content - one for text and other for image.

choice = input("Hello, Enter Prompt 'text' for Content generation or 'image' for Image generation : \n")

payload = None

if choice == "text":
    question = input("Please enter your text prompt for Content Generation : \n")

    # text wala payload down here 👇

    payload = json.dumps({
        "question": question,
        "model": "aicon-v4-nano-160824",
        "randomness": 0.7,  # Adjust for creativity (0.1 to 1.0)
        "stream_data": False,  # Set to True for streamed responses
        "training_data": "You are a professional content creator specializing in travel. Write creative, detailed content.",
        "response_type": "text"
    })

elif choice == "image":
    question = input("Please enter your text prompt for graphic generation: \n").strip()

    if not question or len(question) < 5:
        print("Error: prompt must be descriptive and non-empty.")

    else:
        print(f"Question received : {question}")
        payload = json.dumps({
            "question": [question],
            "image_style": "Anime",
            "orientation": "Square",
            "response_type": "url",
            "model": "aicon-v4-alpha-160824"
        })

        # -------------------------------------NEW TASK-------------------------------------------------------
if payload:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-8a30fa76afa84c8493b2938f634d34e4'  # Replace with your actual API key
    }
    # -------------------------------------IGNORE UNTIL PREVIOUS TASKS ARE COMPLETED-------------------------
    try:
        endpoint = "/api/ai/content/v4" if choice == "text" else "/api/ai/images/generate/v2"
        conn.request("POST", "/api/ai/content/v4", payload, headers)
        res = conn.getresponse()
        data = res.read()

        print("\nRespone from Worqhat API :")
        print(data.decode("utf-8"))

    except Exception as e:
        print(f"An error occurred: {e}")

# Step 6: Close the connection
conn.close()