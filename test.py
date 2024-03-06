import requests

if __name__ == '__main__':
    english_text = (
        "It was the best of times, it was the worst of times, it was the age "
        "of wisdom, it was the age of foolishness, it was the epoch of belief"
    )
    response = requests.post("http://127.0.0.1:8000/text_ml/", json=english_text)
    french_text = response.text

    print(french_text)