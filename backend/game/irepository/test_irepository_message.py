import pytest

from game.irepository.irepository_message import IRepositoryMessage


@pytest.mark.django_db(transaction=True)
def test_save_message():
    irepositorymessage = IRepositoryMessage()
    irepositorymessage.save_message_db("Test_Save", "error")
    assert irepositorymessage.get_message_db("Test_Save", "error").message_string == "Test_Save"


@pytest.mark.django_db(transaction=True)
def test_get_message():
    irepositorymessage = IRepositoryMessage()
    irepositorymessage.save_message_db("Test_Get", "error")
    assert irepositorymessage.get_message_db("Test_Get", "error").message_string == 'Test_Get'


@pytest.mark.django_db(transaction=True)
def test_update_message():
    irepositorymessage = IRepositoryMessage()
    irepositorymessage.save_message_db("Test_Update1", "error")
    irepositorymessage.update_message_db("Test_Update1", "error")
    assert irepositorymessage.get_message_db("Test_Update1", "error").message_string == "Test_Update1"


@pytest.mark.django_db(transaction=True)
def test_delete_message():
    irepositorymessage = IRepositoryMessage()
    irepositorymessage.save_message_db("Test_Delete", "error")
    assert irepositorymessage.delete_message_db("Test_Delete", "error") == None
