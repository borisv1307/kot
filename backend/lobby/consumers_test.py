import pytest
import pytest_asyncio
from channels.routing import URLRouter
from channels.testing import HttpCommunicator
from django.conf.urls import url

from lobby.consumers import GameConsumer
from django.urls import re_path

from . import consumers

from django.test import override_settings

from channels.generic.websocket import (
    AsyncJsonWebsocketConsumer,
    AsyncWebsocketConsumer,
    JsonWebsocketConsumer,
    WebsocketConsumer,
)
from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator
#
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }
#
# @pytest.mark.asyncio
# async def test_websocket_consumer():
#     """
#     Tests that WebsocketConsumer is implemented correctly.
#     """
#     results = {}
#     #
#     # class TestConsumer(WebsocketConsumer):
#     #     def connect(self):
#     #         results["connected"] = True
#     #         self.accept()
#     #
#     #     def receive(self, text_data=None, bytes_data=None):
#     #         results["received"] = (text_data, bytes_data)
#     #         self.send(text_data=text_data, bytes_data=bytes_data)
#     #
#     #     def disconnect(self, code):
#     #         results["disconnected"] = code
#
#     # Test a normal connection
#     communicator = WebsocketCommunicator(
#         application=GameConsumer,
#         path='/taxi/'
#     )
#     connected, _ = await communicator.connect()
#     assert connected
#     assert "connected" in results
#     # Test sending text
#     await communicator.send_to(text_data="hello")
#     response = await communicator.receive_from()
#     assert response == "hello"
#     assert results["received"] == ("hello", None)
#     # Test sending bytes
#     await communicator.send_to(bytes_data=b"w\0\0\0")
#     response = await communicator.receive_from()
#     assert response == b"w\0\0\0"
#     assert results["received"] == (None, b"w\0\0\0")
#     # Close out
#     await communicator.disconnect()
#     assert "disconnected" in results

#
# @pytest.fixture(autouse=True)
# def dice_handler():
#     dice_handler = DiceHandler()
#     dice_handler.roll_initial(6, 3)
#     return dice_handler
#
#
# def test_start_turn(dice_handler):
#     for die in dice_handler.dice_values:
#         assert die in dice.DieValue
#     assert len(dice_handler.dice_values) == 6

# def test_something(self):
#         self.assertEqual(True, True)

#
# import pytest
# from django.test import override_settings
#
# from channels.generic.websocket import (
#     AsyncJsonWebsocketConsumer,
#     AsyncWebsocketConsumer,
#     JsonWebsocketConsumer,
#     WebsocketConsumer,
# )
# from channels.layers import get_channel_layer
#
# from channels.testing import WebsocketCommunicator
#
#
# @pytest_asyncio.mark.asyncio
# async def test_wwebsocket_consumer():
#     application = URLRouter([
#         url(r'ws/lobby/(?P<room_name>\w+)/$', GameConsumer),
#     ])
#     communicator = WebsocketCommunicator(application, "/ws/lobby/room/")
#     connected, subprotocol = await communicator.connect()
#     assert connected
#     # Test on connection welcome message
#     message = await communicator.receive_from()
#     assert message == 'test'
#     # Close
#     await communicator.disconnect()
#
#
# @pytest.mark.asyncio
# async def test_websocket_consumer():
#     """
#     Tests that WebsocketConsumer is implemented correctly.
#     """
#     results = {}
#
#     class TestConsumer(WebsocketConsumer):
#         def connect(self):
#             results["connected"] = True
#             self.accept()
#
#         def receive(self, text_data=None, bytes_data=None):
#             results["received"] = (text_data, bytes_data)
#             self.send(text_data=text_data, bytes_data=bytes_data)
#
#         def disconnect(self, code):
#             results["disconnected"] = code
#
#     # Test a normal connection
#     communicator = WebsocketCommunicator(TestConsumer, "/testws/")
#     connected, _ = await communicator.connect()
#     assert connected
#     assert "connected" in results
#     # Test sending text
#     await communicator.send_to(text_data="hello")
#     response = await communicator.receive_from()
#     assert response == "hello"
#     assert results["received"] == ("hello", None)
#     # Test sending bytes
#     await communicator.send_to(bytes_data=b"w\0\0\0")
#     response = await communicator.receive_from()
#     assert response == b"w\0\0\0"
#     assert results["received"] == (None, b"w\0\0\0")
#     # Close out
#     await communicator.disconnect()
#     assert "disconnected" in results
#
#
# @pytest.mark.asyncio
# async def test_websocket_consumer_subprotocol():
#     """
#     Tests that WebsocketConsumer correctly handles subprotocols.
#     """
#
#     class TestConsumer(WebsocketConsumer):
#         def connect(self):
#             assert self.scope["subprotocols"] == ["subprotocol1", "subprotocol2"]
#             self.accept("subprotocol2")
#
#     # Test a normal connection with subprotocols
#     communicator = WebsocketCommunicator(
#         TestConsumer, "/testws/", subprotocols=["subprotocol1", "subprotocol2"]
#     )
#     connected, subprotocol = await communicator.connect()
#     assert connected
#     assert subprotocol == "subprotocol2"
#
#
# @pytest.mark.asyncio
# async def test_websocket_consumer_groups():
#     """
#     Tests that WebsocketConsumer adds and removes channels from groups.
#     """
#     results = {}
#
#     class TestConsumer(WebsocketConsumer):
#         groups = ["chat"]
#
#         def receive(self, text_data=None, bytes_data=None):
#             results["received"] = (text_data, bytes_data)
#             self.send(text_data=text_data, bytes_data=bytes_data)
#
#     channel_layers_setting = {
#         "default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}
#     }
#     with override_settings(CHANNEL_LAYERS=channel_layers_setting):
#         communicator = WebsocketCommunicator(TestConsumer, "/testws/")
#         await communicator.connect()
#
#         channel_layer = get_channel_layer()
#         # Test that the websocket channel was added to the group on connect
#         message = {"type": "websocket.receive", "text": "hello"}
#         await channel_layer.group_send("chat", message)
#         response = await communicator.receive_from()
#         assert response == "hello"
#         assert results["received"] == ("hello", None)
#         # Test that the websocket channel was discarded from the group on disconnect
#         await communicator.disconnect()
#         assert channel_layer.groups == {}
#
#
# @pytest.mark.asyncio
# async def test_async_websocket_consumer():
#     """
#     Tests that AsyncWebsocketConsumer is implemented correctly.
#     """
#     results = {}
#
#     class TestConsumer(AsyncWebsocketConsumer):
#         async def connect(self):
#             results["connected"] = True
#             await self.accept()
#
#         async def receive(self, text_data=None, bytes_data=None):
#             results["received"] = (text_data, bytes_data)
#             await self.send(text_data=text_data, bytes_data=bytes_data)
#
#         async def disconnect(self, code):
#             results["disconnected"] = code
#
#     # Test a normal connection
#     communicator = WebsocketCommunicator(TestConsumer, "/testws/")
#     connected, _ = await communicator.connect()
#     assert connected
#     assert "connected" in results
#     # Test sending text
#     await communicator.send_to(text_data="hello")
#     response = await communicator.receive_from()
#     assert response == "hello"
#     assert results["received"] == ("hello", None)
#     # Test sending bytes
#     await communicator.send_to(bytes_data=b"w\0\0\0")
#     response = await communicator.receive_from()
#     assert response == b"w\0\0\0"
#     assert results["received"] == (None, b"w\0\0\0")
#     # Close out
#     await communicator.disconnect()
#     assert "disconnected" in results
#
#
# @pytest.mark.asyncio
# async def test_async_websocket_consumer_subprotocol():
#     """
#     Tests that AsyncWebsocketConsumer correctly handles subprotocols.
#     """
#
#     class TestConsumer(AsyncWebsocketConsumer):
#         async def connect(self):
#             assert self.scope["subprotocols"] == ["subprotocol1", "subprotocol2"]
#             await self.accept("subprotocol2")
#
#     # Test a normal connection with subprotocols
#     communicator = WebsocketCommunicator(
#         TestConsumer, "/testws/", subprotocols=["subprotocol1", "subprotocol2"]
#     )
#     connected, subprotocol = await communicator.connect()
#     assert connected
#     assert subprotocol == "subprotocol2"
#
#
# @pytest.mark.asyncio
# async def test_async_websocket_consumer_groups():
#     """
#     Tests that AsyncWebsocketConsumer adds and removes channels from groups.
#     """
#     results = {}
#
#     class TestConsumer(AsyncWebsocketConsumer):
#         groups = ["chat"]
#
#         async def receive(self, text_data=None, bytes_data=None):
#             results["received"] = (text_data, bytes_data)
#             await self.send(text_data=text_data, bytes_data=bytes_data)
#
#     channel_layers_setting = {
#         "default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}
#     }
#     with override_settings(CHANNEL_LAYERS=channel_layers_setting):
#         communicator = WebsocketCommunicator(TestConsumer, "/testws/")
#         await communicator.connect()
#
#         channel_layer = get_channel_layer()
#         # Test that the websocket channel was added to the group on connect
#         message = {"type": "websocket.receive", "text": "hello"}
#         await channel_layer.group_send("chat", message)
#         response = await communicator.receive_from()
#         assert response == "hello"
#         assert results["received"] == ("hello", None)
#
#         # Test that the websocket channel was discarded from the group on disconnect
#         await communicator.disconnect()
#         assert channel_layer.groups == {}
#
#
# @pytest.mark.asyncio
# async def test_async_websocket_consumer_specific_channel_layer():
#     """
#     Tests that AsyncWebsocketConsumer uses the specified channel layer.
#     """
#     results = {}
#
#     class TestConsumer(AsyncWebsocketConsumer):
#         channel_layer_alias = "testlayer"
#
#         async def receive(self, text_data=None, bytes_data=None):
#             results["received"] = (text_data, bytes_data)
#             await self.send(text_data=text_data, bytes_data=bytes_data)
#
#     channel_layers_setting = {
#         "testlayer": {"BACKEND": "channels.layers.InMemoryChannelLayer"}
#     }
#     with override_settings(CHANNEL_LAYERS=channel_layers_setting):
#         communicator = WebsocketCommunicator(TestConsumer, "/testws/")
#         await communicator.connect()
#
#         channel_layer = get_channel_layer("testlayer")
#         # Test that the specific channel layer is retrieved
#         assert channel_layer != None
#
#         channel_name = list(channel_layer.channels.keys())[0]
#         message = {"type": "websocket.receive", "text": "hello"}
#         await channel_layer.send(channel_name, message)
#         response = await communicator.receive_from()
#         assert response == "hello"
#         assert results["received"] == ("hello", None)
#
#         await communicator.disconnect()
#
#
# @pytest.mark.asyncio
# async def test_json_websocket_consumer():
#     """
#     Tests that JsonWebsocketConsumer is implemented correctly.
#     """
#     results = {}
#
#     class TestConsumer(JsonWebsocketConsumer):
#         def connect(self):
#             self.accept()
#
#         def receive_json(self, data=None):
#             results["received"] = data
#             self.send_json(data)
#
#     # Open a connection
#     communicator = WebsocketCommunicator(TestConsumer, "/testws/")
#     connected, _ = await communicator.connect()
#     assert connected
#     # Test sending
#     await communicator.send_json_to({"hello": "world"})
#     response = await communicator.receive_json_from()
#     assert response == {"hello": "world"}
#     assert results["received"] == {"hello": "world"}
#     # Test sending bytes breaks it
#     await communicator.send_to(bytes_data=b"w\0\0\0")
#     with pytest.raises(ValueError):
#         await communicator.wait()
#
#
# @pytest.mark.asyncio
# async def test_async_json_websocket_consumer():
#     """
#     Tests that AsyncJsonWebsocketConsumer is implemented correctly.
#     """
#     results = {}
#
#     class TestConsumer(AsyncJsonWebsocketConsumer):
#         async def connect(self):
#             await self.accept()
#
#         async def receive_json(self, data=None):
#             results["received"] = data
#             await self.send_json(data)
#
#     # Open a connection
#     communicator = WebsocketCommunicator(TestConsumer, "/testws/")
#     connected, _ = await communicator.connect()
#     assert connected
#     # Test sending
#     await communicator.send_json_to({"hello": "world"})
#     response = await communicator.receive_json_from()
#     assert response == {"hello": "world"}
#     assert results["received"] == {"hello": "world"}
#     # Test sending bytes breaks it
#     await communicator.send_to(bytes_data=b"w\0\0\0")
#     with pytest.raises(ValueError):
#         await communicator.wait()
