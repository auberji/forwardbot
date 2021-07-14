from enum import Enum

class inputs(Enum):
    '''
    Set of Inputs the bot will accept
    Update here as not to add magic strings all over the place
    '''
    FORWARDTO = "forwardto" # Setup forwarding rule
    FWMSG = "fwmsg" # Send to channel with forwarding rules setup
    ACTIVATE = "activatefw" # Activate bot and set guild id