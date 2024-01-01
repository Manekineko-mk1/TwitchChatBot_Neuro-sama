import sys
import unittest
from unittest.mock import patch, mock_open
import Utilities

class TestUtilities(unittest.TestCase):

    @patch('builtins.input', side_effect=['oauth:token', 'client_id', 'client_secret', 'bot_nick', '!', 'channel'])
    @patch('builtins.open', new_callable=mock_open, read_data="[DEFAULT]\n")
    def test_validate_and_setup_env(self, mock_file, mock_input):
        Utilities.validate_and_setup_env()
        mock_file().write.assert_any_call("TMI_TOKEN=oauth:token\n")
        mock_file().write.assert_any_call("CLIENT_ID=client_id\n")
        mock_file().write.assert_any_call("CLIENT_SECRET=client_secret\n")
        mock_file().write.assert_any_call("BOT_NICK=bot_nick\n")
        mock_file().write.assert_any_call("BOT_PREFIX=!\n")
        mock_file().write.assert_any_call("CHANNEL=channel\n")

    @patch('requests.post')
    def test_get_oauth_token(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'access_token': 'token'}
        self.assertEqual(Utilities.get_oauth_token('client_id', 'client_secret'), 'token')

    @patch('requests.get')
    def test_is_token_valid(self, mock_get):
        mock_get.return_value.status_code = 200
        self.assertTrue(Utilities.is_token_valid('token'))

    @patch('builtins.open', new_callable=mock_open, read_data="[DEFAULT]\nTMI_TOKEN=oauth:token\n")
    def test_load_token(self, mock_file):
        self.assertEqual(Utilities.load_token(), 'token')

    @patch('Utilities.is_token_valid', return_value=True)
    @patch('Utilities.load_token', return_value='token')
    def test_get_valid_oauth_token(self, mock_load_token, mock_is_token_valid):
        self.assertEqual(Utilities.get_valid_oauth_token('client_id', 'client_secret'), 'token')

if __name__ == '__main__':
    unittest.main()