import os
from pathlib import Path
import time
import subprocess
import streamlit as st

# Check if the API is running
api_process = None
def start_api():
    global api_process
    if api_process is None:
        # Start the API in a separate process
        api_process = subprocess.Popen(["python", "api.py"])
        # Wait for the API to start
        time.sleep(5)

# Start the API
start_api()

# Import and run the Streamlit app
from app import main

# Run the main function
if __name__ == "__main__":
    main()
