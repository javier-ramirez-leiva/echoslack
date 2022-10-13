import os
import sys
import slack




def SendNotification (argv,fileecho,output):

    with open(os.path.join(sys.path[0], "Slack_api.txt"), "r") as apiFile:
         lines = apiFile.readlines()
         client_token=lines[0].strip()
         channel_id=lines[1].strip()
    client = slack.WebClient(token=client_token)
    WS = os.path.basename(os.path.normpath(os.getcwd()))
    if (output =="-out"):
        response = client.files_upload(    
        file=fileecho,
        title=argv,
        filetype = '.txt',
        filename = argv,
        initial_comment = WS+"\n```"+argv+"```",
        channels=channel_id  ##notifcation-python channel
        )
    else:
        client.chat_postMessage(
        channel=channel_id,  ##notifcation-python channel
        text=WS+"\n```"+argv+"```"
        )




if __name__ == "__main__":
    SendNotification(sys.argv[1],sys.argv[2],sys.argv[3])