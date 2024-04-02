# AI_BOT

**Introduction**

It has to take in voice command and in the back ground the subject should be about Indian states, culture etc 

**Prerequisites**

Before you begin, ensure you have Python 3.9.6 installed on your system. if you do not have ppython install, you can download it from [python.org]()

**Setting Up a Virtual Environment**
Create a Virtual Environment

First, ensure you are in your project's root directory. If you haven't already, create a directory for your project and navigate into it. Then, run the following command to create a virtual environment named 'venv':

`python3 -m venv venv`

**Activate the Virtual Environment**

On Windows:
`.\venv\Scripts\activate`

**On macOS/Linux:**

`source venv/bin/activate`

**Installing Dependencies**

Ensure your virtual environment is activated, then install the required packages using the 'requirements.txt' file with the following command:

`pip install -r requirements.txt`

**Setting Environment Variables**

To run the Flask application correctly, you need to set several environment variables. You can do this on the command line or by creating a .env file in the root directory of your project. If you choose the command line method, ensure your virtual environment is activated, and run the following commands:

**On Windows (Command Prompt):**

`set FLASK_ENV=development`

`set FLASK_RUN_PORT=5001`

`set OPENAI_API_KEY=your_openai_api_key_here`


**On macOS/Linux:**

`export FLASK_ENV=development`

`export FLASK_RUN_PORT=5001`

`export OPENAI_API_KEY=your_openai_api_key_here`


Alternatively, you can create a .env file in the root of your project and add the following lines (replace placeholders with your actual data):

`FLASK_ENV=development`

`FLASK_RUN_PORT=5001`

`OPENAI_API_KEY=your_openai_api_key_here`

**Running the Application**

With the environment variables set, you're ready to run the application. Execute the following command:

`python run.py`

