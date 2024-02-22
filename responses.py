
def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return 'Silent'
    elif 'hello' in lowered:
        return 'Hello there'