import discord
from forwardbot.forwarding_rule import forwarding_rule
from forwardbot.inputs import inputs

'''
Discord bot to setup forwarding rules for channels, will automatically forward messages containing:

Basic functionality:
Activate to set guild ID
Set forwarding rule to particular channel
Forward message explicitly to that reference, or automatically if attachments found
'''
class forward_bot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guild = None
        self.channels = {}

    def _get_forwarding_name(self, message):
        forwarding_channel = message.content.replace(inputs.FORWARDTO.value, '')
        forwarding_channel = forwarding_channel.lstrip() # Strip leading and trailing whitespace from string
        return forwarding_channel.rstrip() # Discord channel names are allowed spaces

    async def _send_error(self, message):
        await self.get_channel(message.channel.id).send("No forwarding rule found")

    async def fw_message(self, message):
        await self.forward(message) if self.channels.get(message.channel.id) is not None else self._send_error(message)

    async def add_channels(self, message, fw_channel):
        # Create dict of channels and their channel forwarding object
        self.channels[message.channel.id] = forwarding_rule(self.get_channel(message.channel.id), fw_channel)

    async def forward(self, message):
        # Call and handle channel forward message
        await self.channels.get(message.channel.id).forward(message)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith(inputs.ACTIVATE.value):
            # Set guild ID by prodding bot to grab it from a message sent to it
            self.guild = self.get_guild(message.guild.id)
        if self.guild is not None:
            if message.content.startswith(inputs.FORWARDTO.value):
                fwchannel = discord.utils.get(self.guild.text_channels, name=self._get_forwarding_name(message))
                await self.add_channels(message, fwchannel)
            elif message.content.startswith(inputs.FWMSG.value) or len(message.attachments) > 0:
                await self.fw_message(message)
