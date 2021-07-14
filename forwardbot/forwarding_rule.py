'''
Represent a set of related Channels, the original channel and the channel to forward to
'''
class forwarding_rule(object):
    
    def __init__(self, channel, fwchannel):
        self.original_channel = channel
        self.fw_channel = fwchannel

    async def _send_files(self, message):
        '''
        Take list of attachments and converto discord.File objects
        Forward files to fw_channel
        :param message:
        :return: void
        '''
        for item in message.attachments:
            attachment = await item.to_file()
            await self.fw_channel.send(content=f"Original post by {message.author}\n", file=attachment)

    async def _send_message(self, message):
        '''
        Forward message with original ownership and content
        :param message:
        :return: void
        '''
        if message.content != "":
            await self.fw_channel.send(f"Original posted by {message.author}\n {message.content}")

    async def _send_error(self):
        '''
        Send a message informing that the forwarding rule channel does not exist
        :return: void
        '''
        await self.channelid.send(f"Channel not found {self.fw_channel.name}")

    async def forward(self, message):
        '''
        Posts message to forwarding channel (fw_channel) using stored channel object
        If fails sends error message to original channel to say that channel has not been found
        E.g. an incorrect forwarding rule has been setup.
        :param message:
        :return: void
        '''
        if self.fw_channel is not None:
            await self._send_message(message)
            await self._send_files(message)
        else:
            await self._send_error()



