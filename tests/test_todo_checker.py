from lib.todo_checker import *
import pytest

def test_empty_string():
    assert todo_checker('') == False

def test_if_todo_is_lowercase():
    assert todo_checker("#todo buy milk") == True

def test_if_not_string():
    with pytest.raises(Exception) as e:
        todo_checker(2000)
    error_message = str(e.value)
    assert error_message == "Please entry a string"

def test_if_given_only_todo():
    with pytest.raises(Exception) as e:
            todo_checker('#TODO')
    error_message = str(e.value)
    assert error_message == "Please also include task"

def test_if_given_todo():
    assert todo_checker("#TODO buy milk") == True

def test_if_given_no_todo():
    assert todo_checker("buy milk") == False