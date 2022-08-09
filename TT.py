import os, time, signal, functools, uuid
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import AbstractEvent, ViewerCountUpdateEvent, CommentEvent, LiveEndEvent, GiftEvent, QuestionEvent, UnknownEvent, ConnectEvent, DisconnectEvent, EmoteEvent, EnvelopeEvent, ShareEvent, SubscribeEvent, WeeklyRankingEvent, MicBattleEvent, MicArmiesEvent, JoinEvent

os.system('clear')

print('Enter TT Live to Connect to ')
"""ttu = ('dad..tech')"""
ttu = input()
print('Word to start Playlist 1 (case-sensitive)')
dtkey1 = input()
print('Word to start Playlist 2 (case-sensitive)')
dtkey2 = input()
print('Word to start Playlist 3 (case-sensitive)')
dtkey3 = input()
print('Word to start Playlist 4 (case-sensitive)')
dtkey4 = input()
print('Word to start Playlist 5 (case-sensitive)')
dtkey5 = input()

print('Connecting to ' + ttu)
client = TikTokLiveClient(ttu, timeout_ms=None)

@client.on("viewerCount",)
async def on_join(event: ViewerCountUpdateEvent):
	print(event.viewCount, "bottles of beer on the wall")

@client.on("share")
async def on_share(event: ShareEvent):
	os.system('/opt/fpp/src/fpp -P 3')
	print(f"{event.user.uniqueId} knows sharing is caring")
	
# Connected
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)
    
# Comment command
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

@client.on("comment")
async def on_comment(event: CommentEvent):
	print(f"{event.user.nickname} -> {event.comment}")
	
	dtcom = (event.comment)
		
		
	if dtcom == (dtkey1):
		os.system('/opt/fpp/src/fpp -P 1')
		print('Playlist 1')

	if dtcom == (dtkey2):
		os.system('/opt/fpp/src/fpp -P 2')
		print('Playlist 2')

	if dtcom == (dtkey3):
		os.system('/opt/fpp/src/fpp -P 3')
		print('Playlist 3')

	if dtcom == (dtkey4):
		os.system('/opt/fpp/src/fpp -P 4')
		print('Playlist 4')

	if dtcom == (dtkey5):
		os.system('/opt/fpp/src/fpp -P 5')
		print('Playlist 5')


# Define handling an event via "callback"
client.add_listener("comment", on_comment)

@client.on("join")
async def on_join(event: JoinEvent):
	print(f"{event.user.nickname} has joined")

@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
	print("Disconnected")
	os.system('/opt/fpp/src/fpp -P 6')
	os.system('python3 TikTok/TT.py')

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
