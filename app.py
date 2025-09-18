# app.py
"""
A simple Python app to demonstrate version control and CI/CD with GitLab.
Later we’ll add tests, Docker, and deployment.
"""

from datetime import datetime

def greet(name: str) -> str:
    """Return a greeting message with the current time."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, {name}! The current time is {now}."

if __name__ == "__main__":
    # Run the app with a default name
    print(greet("Polytechnique"))
≈
