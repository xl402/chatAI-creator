import requests
from dataclasses import dataclass

import config


@dataclass
class BotBuilderUserInput:
    bot_name: str
    personalities: str
    categories: str

    def __post_init__(self):
        self._check_string_format(self.personalities)
        self._check_string_format(self.categories)

    @staticmethod
    def _check_string_format(input_string):
        assert isinstance(input_string, str), 'input must be a string'
        assert input_string.islower(), 'input must be all lower case'


USER_INPUT = BotBuilderUserInput('Eliza (therapist)', 'angst, happy, bright, good listener', 'romance, friendship, roleplay')


def get_background(user_input):
    preprompt = config.BACKGROUND_PREPROMPT.format(
        bot_name=user_input.bot_name,
        personalities=user_input.personalities,
        categories=user_input.categories
    )
    background = get_response(preprompt)
    return background


def get_first_message(user_input, background):
    preprompt = config.FIRST_MESSAGE_PREPROMPT.format(
        bot_name=user_input.bot_name,
        personalities=user_input.personalities,
        background=background
    )
    prefix = _get_prefix(preprompt)
    first_message = prefix + get_response(preprompt)
    return first_message


def get_example_conversation(user_input, background, first_message):
    conversations = [first_message]
    for idx in range(6):
        convo_string = _get_formatted_conversations(conversations, user_input.bot_name)
        is_bot = idx % 2
        response = _get_conversation_response(convo_string, user_input, background, is_bot)
        conversations.append(response)
    example_convo = _get_formatted_conversations(conversations, user_input.bot_name)
    return example_convo


def _get_conversation_response(convo_string, user_input, background, is_bot):
    if is_bot:
        response = _get_bot_message(convo_string, user_input, background)
    else:
        response = _get_user_message(convo_string, background)
    return response


def _get_bot_message(convo_string, user_input, background):
    preprompt = config.BOT_MESSAGE_PREPROMPT.format(
        bot_name=user_input.bot_name,
        personalities=user_input.personalities,
        background=background,
        chat_history=convo_string
    )
    prefix = _get_prefix(preprompt)
    response = prefix + get_response(preprompt)
    return response


def _get_user_message(convo_string, background):
    preprompt = config.USER_MESSAGE_PREPROMPT.format(
        background=background,
        chat_history=convo_string
    )
    response = get_response(preprompt)
    return response


def get_response(text, generation_params=None):
    generation_params = generation_params or config.DEFAULT_GENERATION_PARAMS
    payload = {'instances': [{'text': text, 'generation_params': generation_params}]}
    text = _get_endpoint_response_with_fallback(config.ENDPOINT_URL, payload)
    text = _format_response(text)
    return text


def _get_endpoint_response_with_fallback(endpoint_url, payload):
    try:
        resp = requests.post(endpoint_url, json=payload, timeout=15)
        assert resp.status_code == 200
        text = resp.json()['predictions'][0]
    except requests.exceptions.Timeout:
        text = 'S-sorry... server timed out... p-plz write ur own prompt~'
    except AssertionError:
        text = f'S-sorry... server errored with {resp.status_code}... p-plz write ur own prompt~'
    return text


def _get_prefix(prompt):
    prefix = '*' if prompt.endswith('*') else ''
    return prefix


def _format_response(text):
    text = text.replace('\*\*', '*')
    text = text.replace('\*', '*')
    return text.strip()


def _get_formatted_conversations(convo_list, bot_name):
    out = []
    for idx, message in enumerate(convo_list):
        prefix = f'{bot_name}: ' if not idx % 2 else 'You: '
        out.append(prefix + message)
    return '\n'.join(out)
