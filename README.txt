ForwardBot

Simple bot I created for setting up forwarding rules for certain channels

This first implementation allows:

Activate bot on server

- Run activatefw to activate the bot and set a guild id

Setup a forwarding rule for a channel

- send the bot a message starting with forwardto followed by a channel name to use

Manually forward a message

- any message sent with fwmsg before it will be forwarded to the channel with a forwarding rule
- Any items with attachments will automatically be forwarded

Please set your discord token in the .env file found in this checked out repository
