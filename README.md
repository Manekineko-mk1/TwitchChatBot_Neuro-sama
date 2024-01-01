# TwitchChatBot_Neuro-sama

## Overview
This project is a Twitch chatbot designed to interact in Twitch chatrooms. It can respond to commands and has the potential to learn from Twitch streams.

## Features
- Responds to basic chat commands.
- OAuth token management for secure Twitch API interactions.
- Logging of bot activities and interactions.

## Setup
1. Clone the repository.
2. Install dependencies:

pipenv install

3. Set up your `.env` file with the following variables:

TMI_TOKEN=oauth:your_oauth_token
CLIENT_ID=your_client_id
BOT_NICK=your_bot_nick
BOT_PREFIX=!
CHANNEL=your_channel

## Running the Bot
Activate the `pipenv` shell and run the bot:

pipenv shell
python Bot.py

## Code Generation Acknowledgement
This project's code was generated with the assistance of ChatGPT, an AI developed by OpenAI.

## Continuing Development with ChatGPT
To continue developing this project using ChatGPT, provide a prompt that describes the current state of the project, specific tasks to be addressed, and any relevant context or code details. Example prompt:
"Continue developing a Twitch chatbot project stored at [GitHub Repo URL]. The project, worked on with ChatGPT, includes Bot.py for bot functionalities and Utilities.py for OAuth management and logging. It's currently capable of handling basic chat commands. The project roadmap includes [list next milestones or features]. I've been managing the project and need guidance on implementing these next steps. Please review the repo for context and provide code suggestions and development strategies."

## Project Plan with Learning Personality

### Phase 1: Requirements and Setup (Expanded)
1. Extended Bot Features: Develop bot personality based on Twitch stream content. - Completed
2. Research and Plan for Advanced Features: Assess tools for live video processing, speech recognition, NLP, and machine learning. - Completed

### Phase 2: Development Environment Setup (Expanded)
1. Identify Advanced Libraries: Select libraries for video processing, speech-to-text, NLP, and machine learning. - Completed
2. Environment Setup: Configure development environment with selected libraries. - Completed

### Phase 3: Core Bot Development (Expanded)
1. Live Video Processing Module: Create a module to capture and process live video streams. - In Progress
2. Speech Recognition and Text Extraction: Implement functionality to convert stream audio into text. - In Progress
3. NLP and Personality Analysis: Develop a system to analyze text and extract personality traits. - In Progress

### Phase 4: Machine Learning Model Development
1. Dataset Preparation: Collect and prepare a dataset for training the model. - Not Started
2. Model Training: Develop and train a model to adapt chatbot responses based on personality traits. - Not Started
3. Integration with the Chatbot: Integrate the ML model with the chatbot's core functionalities. - Not Started

### Phase 5: Testing, Iteration, and Deployment (Expanded)
1. Extended Testing: Test advanced features, especially the personality learning mechanism. - Pending
2. Deployment with Advanced Capabilities: Deploy the bot with resources to handle advanced processing. - Pending

### Phase 6: Documentation and User Guide (Expanded)
1. Extended Documentation: Document advanced features, instructions, and usage guides. - In Progress

## Contributing
Feedback and contributions are welcome. Please submit pull requests or open an issue for any enhancements you want to propose.

## License
[MIT License](LICENSE.md)
