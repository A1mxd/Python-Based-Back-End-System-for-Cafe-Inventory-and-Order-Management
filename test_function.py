from unittest.mock import patch, mock_open
import pytest
# from app import *
from functions import *
from db_app import *

def mock_get_int_input(text_input, num_options):
    while True:
        try:
            clear_screen()
            int_input =int(input(text_input))
            if int_input> num_options or int_input < 0:
                clear_screen()
                print('\t***That was an invalid option***')
                short_pause()
                return '\t***That was an invalid option***' 
            else:
                return int_input
        except ValueError:
            value_error()
            return ValueError

@patch('builtins.input')
def test_confirmation_yes(mock_input):
    mock_input.return_value = 'y'
    expected =  'y'
    result =    confirmation()
    assert result == expected

@patch('builtins.input')
def test_confirmation_no(mock_input):
    mock_input.return_value = 'n'
    expected =  'n'
    result =    confirmation()
    assert result == expected

@patch('builtins.input')    
def test_get_int_input_valid(mock_input):
    mock_input.return_value = '1'
    expected =  1
    result = get_int_input('Enter a number:', 2)    
    assert expected == result


@patch('builtins.input') 
def test_get_int_input_invalid_high(mock_input):
    mock_input.return_value = '3'
    expected =  '\t***That was an invalid option***'
    result = mock_get_int_input('Enter a number:', 2)    
    assert expected == result

@patch('builtins.input') 
def test_get_int_input_invalid_low(mock_input):
    mock_input.return_value = '-1'
    expected =  '\t***That was an invalid option***' 
    result = mock_get_int_input('Enter a number:', 2)    
    assert expected == result


@patch('builtins.input') 
def test_get_int_input_invalid_input(mock_input):
        mock_input.side_effect = ['abc', ValueError]
        expected =  ValueError
        result = mock_get_int_input('Enter a number:', 2)    
        assert expected == result


def test_customer_text_options():
    result = customer_text_options()

    assert isinstance(result, str)


