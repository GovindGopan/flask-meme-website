# Random Meme Website

A Flask web application that displays random memes from Reddit with auto-refresh functionality.

## Features
- Fetches random memes from Reddit via API
- Auto-refreshes every 30 seconds
- Responsive design
- Accessible across local network devices

## Technologies Used
- Python 3
- Flask
- HTML/CSS
- REST API integration

## Setup Instructions

1. Clone the repository
2. Create virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install flask requests
```
4. Run the application:
```bash
   python3 memeflask.py
```
5. Open browser to `http://localhost:5000`

## What I Learned
- Setting up Python virtual environments
- Working with Flask routing and templates
- Making HTTP requests to external APIs
- Debugging and troubleshooting
- Network configuration and port forwarding in WSL2

## Future Improvements
- Add ability to select specific subreddits
- Implement favorites/save functionality
- Add user voting system
- Deploy to cloud platform
