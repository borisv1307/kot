import pytest
import django
import os
from channels.generic.websocket import WebsocketConsumer
from channels.testing import WebsocketCommunicator

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kot.settings")
django.setup()



@pytest.mark.asyncio
async def test_websocket_consumer():
    """
    Tests that WebsocketConsumer is implemented correctly.
    """
    results = {}

    class TestConsumer(WebsocketConsumer):
        def connect(self):
            results["connected"] = True
            self.accept()

        def receive(self, text_data=None, bytes_data=None):
            results["received"] = (text_data, bytes_data)
            self.send(text_data=text_data, bytes_data=bytes_data)

        def disconnect(self, code):
            results["disconnected"] = code

    # Test a normal connection
    communicator = WebsocketCommunicator(TestConsumer, "/testws/")
    connected, _ = await communicator.connect()
    assert connected
    assert "connected" in results
    # Test sending text
    await communicator.send_to(text_data="hello")
    response = await communicator.receive_from()
    assert response == "hello"
    assert results["received"] == ("hello", None)
    # Test sending bytes
    await communicator.send_to(bytes_data=b"w\0\0\0")
    response = await communicator.receive_from()
    assert response == b"w\0\0\0"
    assert results["received"] == (None, b"w\0\0\0")
    # Close out
    await communicator.disconnect()
    assert "disconnected" in results


# tests to ensure django generally is configured correctly

@pytest.mark.asyncio
async def test_websocket_consumer():
    """
    Tests that WebsocketConsumer is implemented correctly.
    """
    results = {}

    class TestConsumer(WebsocketConsumer):
        def connect(self):
            results["connected"] = True
            self.accept()

        def receive(self, text_data=None, bytes_data=None):
            results["received"] = (text_data, bytes_data)
            self.send(text_data=text_data, bytes_data=bytes_data)

        def disconnect(self, code):
            results["disconnected"] = code

    # Test a normal connection
    communicator = WebsocketCommunicator(TestConsumer, "/testws/")
    connected, _ = await communicator.connect()
    assert connected
    assert "connected" in results
    # Test sending text
    await communicator.send_to(text_data="hello")
    response = await communicator.receive_from()
    assert response == "hello"
    assert results["received"] == ("hello", None)
    # Test sending bytes
    await communicator.send_to(bytes_data=b"w\0\0\0")
    response = await communicator.receive_from()
    assert response == b"w\0\0\0"
    assert results["received"] == (None, b"w\0\0\0")
    # Close out
    await communicator.disconnect()
    assert "disconnected" in results


@pytest.mark.asyncio
async def test_websocket_consumer_subprotocol():
    """
    Tests that WebsocketConsumer correctly handles subprotocols.
    """

    class TestConsumer(WebsocketConsumer):
        def connect(self):
            assert self.scope["subprotocols"] == ["subprotocol1", "subprotocol2"]
            self.accept("subprotocol2")

    # Test a normal connection with subprotocols
    communicator = WebsocketCommunicator(
        TestConsumer, "/testws/", subprotocols=["subprotocol1", "subprotocol2"]
    )
    connected, subprotocol = await communicator.connect()
    assert connected
    assert subprotocol == "subprotocol2"
