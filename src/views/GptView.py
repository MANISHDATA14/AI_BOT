from flask import Blueprint, request
from src.SharedServices.MainService import StatusType, MainService
from src.SharedServices.TaskAiAssistantService import AIAssistantService

chatGptApi = Blueprint('ChatGPT view version 1', __name__)


@chatGptApi.route('/conversation', methods=['POST'])
def conversation():
    data = request.json
    print(f"data --> {data}")
    userInput = data.get('input', '')

    try:
        # Run the agent with an input
        aiAssistantService = AIAssistantService(userInput)
        response = aiAssistantService.response
    except Exception as e:
        print("Error executing task:", e)
        response = ''

    # Send response
    data = {
        "status": StatusType.success.value,
        "data": {
            "answer": response
        },
        "message": "AI Message Successfully Sent!"
    }
    return MainService.response(data=data, status_code=200)
