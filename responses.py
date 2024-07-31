from random import randint

def get_response(message_content: str) -> str:
    lowered = message_content.lower()

    if lowered == '':
        return 'I didn\'t quite get that. Could you rephrase your message?'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'roll' in lowered:
        return str(randint(1, 6))
    elif 'weather' in lowered:
        # Add code to fetch and return weather information
        return 'Here is the current weather information: ...'
    elif lowered.startswith(('what', 'why', 'how')):
        return 'I\'m sorry, I don\'t have the capability to answer questions yet.'
    elif lowered == 'abracadabra':
        return 'COMMAND_GIVE_ROLE'
    else:
        return 'I\'m sorry, I didn\'t understand your message.'