from slack_bot import *
import pytest
import time;

input = {'text': 'Hello my awesome bot', 'user': 'UH47MU0GN','ts': str(time.time())}
@pytest.mark.skip(reason = "Fully implemented.")
def test_post_instant_message():
    assert post_instant_message(channel_id="UH47MU0GN", text="Naber Lan")

def test_get_ws_users():
    users = get_ws_users()
    for user in users:
        print(user["name"])

def test_get_BotID():
    assert get_BotID("reinforceme") == "UL4UGDCBU"

@pytest.mark.skip(reason = "Not fully implemented.")
def test_slackReadRTM():
    assert slackReadRTM()

def test_post_scheduled_message():
    assert post_scheduled_message(input,20)
