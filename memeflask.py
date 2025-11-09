#!/usr/bin/env python3
from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_meme():
    try:
        # Using meme-api.com (different from the Heroku one)
        url = "https://meme-api.com/gimme"
        response = requests.get(url, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Error response: {response.text[:200]}")
            return None, None
            
        data = response.json()
        meme_pic = data['url']
        subreddit = data['subreddit']
        
        print(f"Meme URL: {meme_pic}")
        print(f"Subreddit: {subreddit}")
        
        return meme_pic, subreddit
    except Exception as e:
        print(f"Error in get_meme: {e}")
        import traceback
        traceback.print_exc()
        return None, None

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    
    if meme_pic is None:
        return "Error: Could not fetch meme. Check terminal for details."
    
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
