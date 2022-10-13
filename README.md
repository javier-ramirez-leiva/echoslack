Script to output files to a Slack Channel. 
It was conceived to plugin into an terminal app with alias features (such as cmder) and output terminals outputs that takes too long for you to wait.

1. Create a "Clipboard" folder on your local git repo
2. Create a file "Slack_api.txt" on your local git repo with two lines
  * SLACK_API_TOKEN. 
  * SLACK_CHANNEL_ID. 
3. Add the following alias to cmder:
  * slack = $* | tee [GIT_LOCAL_REPO]\ClipBoard\%timeformat%.txt & python [GIT_LOCAL_REPO]\echoslack_cmd.py "$*" [GIT_LOCAL_REPO]\ClipBoard\%timeformat%.txt -nout
  * slacko = $* | tee [GIT_LOCAL_REPO]\ClipBoard\%timeformat%.txt & python [GIT_LOCAL_REPO]\slack\echoslack_cmd.py "$*"[GIT_LOCAL_REPO]\ClipBoard\%timeformat%.txt -out. 

Usage:
  * slack: Message when command is finished 
  * slacko: Message when command is finished and send result


