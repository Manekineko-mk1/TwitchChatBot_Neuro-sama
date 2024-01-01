# Utilities.py
import requests
import configparser
import os
import logging
from datetime import datetime

# Constants
LOG_DIRECTORY = 'log'
ENV_FILE_PATH = '.env'

# Setup logging
def setup_logging():
    os.makedirs(LOG_DIRECTORY, exist_ok=True)
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
    log_filepath = os.path.join(LOG_DIRECTORY, log_filename)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(log_filepath),
                            logging.StreamHandler()
                        ])

# Setup environment file
def setup_env_file(twitch_client_id, twitch_client_secret, bot_nickname, twitch_default_channel, file_path=ENV_FILE_PATH):
    try:
        with open(file_path, 'w') as file:
            file.write(f"TMI_TOKEN=oauth:\n")
            file.write(f"CLIENT_ID={twitch_client_id}\n")
            file.write(f"CLIENT_SECRET={twitch_client_secret}\n")
            file.write(f"BOT_NICK={bot_nickname}\n")
            file.write(f"BOT_PREFIX=!\n")
            file.write(f"CHANNEL={twitch_default_channel}\n")
        logging.info("Environment file setup successfully.")
    except IOError as e:
        logging.error(f"Error setting up environment file: {e}")


# Function to get OAuth token
def get_oauth_token(client_id, client_secret):
    logging.info(f"Attempting to obtain OAuth token ... client_id: {client_id}, client_secret: {client_secret}")
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        token = response.json()['access_token']
        save_token(token)
        logging.info(f"OAuth token obtained successfully: {token}")
        return token
    else:
        logging.error(f"Failed to obtain token. Response: {response}")
        raise Exception(f"Failed to obtain token. Response: {response}")


# Function to save token to a file
def save_token(token, file_path=ENV_FILE_PATH):
    config = configparser.ConfigParser()
    config.read(file_path)  # Read the existing configuration
    
    # if not config.has_section('DEFAULT'):
    #     config.add_section('DEFAULT')

    config.set('DEFAULT', 'TMI_TOKEN', f'oauth:{token}')
    try:
        with open(file_path, 'w') as configfile:
            config.write(configfile)
        logging.info(f"Token saved successfully to {file_path}. Token: {token}")
    except IOError as e:
        logging.error(f"Error saving token to {file_path}: {e}")


# Function to load token from a file
def load_token(file_path=ENV_FILE_PATH):
    config = configparser.ConfigParser()
    if not os.path.exists(file_path):
        logging.warning(f"Config file does not exist: {file_path}")
        return None

    try:
        config.read(file_path)
        token = config.get('DEFAULT', 'TMI_TOKEN')
        if token.startswith('oauth:'):
            token = token.replace('oauth:', '').strip()
        logging.info(f"Token loaded successfully. Token: {token}")
        return token
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        logging.error(f"Error loading token from {file_path}: {e}")
        return None


# Function to check if token is valid
def is_token_valid(token):
    logging.info("Checking if token is valid")
    url = "https://id.twitch.tv/oauth2/validate"
    headers = {"Authorization": f"OAuth {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logging.info(f"Token: {token} is valid")
        return True
    else:
        logging.info(f"Token: {token} is invalid")
        return False


# Function to get valid OAuth token
def get_valid_oauth_token(client_id, client_secret):
    token = load_token()
    if token and is_token_valid(token):
        return token
    else:
        return get_oauth_token(client_id, client_secret)
    

# def validate_and_setup_env():
#     # Define the required keys and their validation functions
#     required_keys = {
#         "TMI_TOKEN": lambda x: x.startswith("oauth:"),
#         "CLIENT_ID": bool,
#         "CLIENT_SECRET": bool,
#         "BOT_NICK": bool,
#         "BOT_PREFIX": lambda x: x == "!",
#         "CHANNEL": bool
#     }

#     # Read the .env file
#     config = configparser.ConfigParser()
#     config.read(ENV_FILE_PATH)

#     # Check if all required keys are present and valid
#     for key, validate in required_keys.items():
#         if key not in config["DEFAULT"] or not validate(config["DEFAULT"][key]):
#             print(f"{key} is missing or invalid. Please enter a new value:")
#             new_value = input()
#             config["DEFAULT"][key] = new_value

#     # Write the updated config back to the .env file
#     with open(ENV_FILE_PATH, 'w') as configfile:
#         config.write(configfile)

#     print("Environment file setup successfully.")


# Call setup_logging at the end of the file so it runs when the module is imported
setup_logging()