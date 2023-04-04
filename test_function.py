if __name__ == '__main__':
    print(f'from code:{__name__}')

    from unittest.mock import patch
    from app import *
    from functions import *

    def test_confirmation_yes():
        with patch('builtins.input', return_value='y'):
            assert confirmation() == 'y'

    def test_confirmation_no():
        with patch('builtins.input', return_value='n'):
            assert confirmation() == 'n'

    