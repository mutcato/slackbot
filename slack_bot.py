import slack
from dotenv import load_dotenv
import os
load_dotenv()
# SLACK_BOT_TOKEN is xoxb.. token
# DO NOT CHANGE THIS BLOK. EDIT .env FILE
BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
# DO NOT CHANGE THIS BLOK. EDIT .env FILE

web_client = slack.WebClient(token=BOT_TOKEN)
rtm_client = slack.RTMClient(token=BOT_TOKEN)
BOT_NAME = "reinforceme"
BOT_NAME_withAT = f"<@{BOT_NAME}>"

def get_ws_users():
    '''
    Gets workspace users as a list of dict
    '''
    users = web_client.users_list()
    return users["members"]


def get_BotID(bot_name):
    ws_users = get_ws_users()    
    for ws_user in ws_users:
        if ws_user["name"] in bot_name and not ws_user["deleted"]:
            return ws_user["id"]

def post_instant_message(input):
    '''
    input is a dict
    returns a dict
    '''
    result = web_client.chat_postMessage(
        channel=input["channel"],
        text="I will remind you this message after 4, 12 and 48 hours.",
        as_user=True,
        thread_ts=input["ts"]
    )
    return result

def post_scheduled_message(input,duration):
    '''
    Direct message in future time
    input is a dict
    returns a dict
    '''
    after_Xsc = int(input["ts"].split(".", 1)[0])+duration
    text = input["text"].replace(f"<@{get_BotID(BOT_NAME)}>","")
    print("ssss: ",after_Xsc)
    result = web_client.chat_scheduleMessage(
        channel=input["user"],
        text=f"<@{input['user']}>" + text,
        as_user=True,
        post_at=str(after_Xsc)
    )
    return result

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    print("data: ",data)
    print("ts",data["ts"].split(".", 1)[0])
    print("ts+1",int(data["ts"].split(".", 1)[0])+10)
    web_client = payload['web_client']
    try:
        if f"<@{get_BotID(BOT_NAME)}>" in data['text']:
            instant_message = post_instant_message(data) 
            scheduled_1 = post_scheduled_message(data,15)
            scheduled_5 = post_scheduled_message(data,30) 
            scheduled_15 = post_scheduled_message(data,45) 
            print("instant_message: ",instant_message)
    except:
        pass

rtm_client.start()
