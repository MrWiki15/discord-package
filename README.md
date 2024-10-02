# Discord Package - Discord Bots Packager

## Description

**Discord Package** is a command line tool for creating and managing Discord bots in Python `(currently in BETA)`. It also includes a simple web monitor to view bot logs in real time, allowing for better visualization and debugging.

## Features

- **Discord bot project generation**: Quickly creates a new bot project with the necessary file and folder structure.
- **Refresh**: The packer is constantly watching for changes in the working directory and will restart the bot if any changes are detected.
- **Real-time log monitoring**: A built-in web server that displays the bot logs in real time in a web interface.
- **Advanced filters**: Filter logs by server name, server ID, user name and date for easy debugging.

## Requirements

- Python 3.6 or higher.
- Additional dependencies: `discord.py`, `watchdog`, `asyncio`, `datetime`, `requests`, `rich`.

## Installation

### 1. Install discord-package

```bash
pip install discord-package
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Create a New Bot Project

To create a new Discord bot project, use the following command:

```bash
dcp create <nombre_del_proyecto>
```

Replace `<project_name>` with the name you want for your new project. This command will create a project structure with all necessary files and folders.

## Project Structure

The `create` command will generate a project structure similar to the following:

```markdown
project_name/
│
├── assets/
│ ├── imagen/
│ │ └── mi_imagen.png
│ └── **init**.py
├── buttons/
│ ├── **init**.py
│ └── buttons_help.py
├── commands/
│ ├── **init**.py
│ └── ping.py
├── config/
│ ├── **init**.py
│ └── bot_config.py
├── functions/
│ ├── **init**.py
│ └── print_logs.py
├── logs/
│ ├── **init**.py
│ └── logs.txt
├── monitor/
│ ├── **init**.py
│ ├── index.html
│ ├── style.css
│ ├── script.js
│ └── monitor.py
├── utils/
│ ├── **init**.py
│ └── error_message.py
├── bot.py
├── dev.py
├── requirements.txt
└── .gitignore
```

## Running the Bot in development mode

```bash
python dev.py
```

## Running the Bot in production mode

```bash
python bot.py
```

# Disclaimer

Discord Package is not an official Discord product. It is a tool created by Polaris Web3 to help developers create and manage Discord bots easily.

For more information: [Documentation](https://docs.polarisweb3.org)

![Polaris](https://cusoft.tech/wp-content/uploads/2024/05/P001.svg)
