# Custom Helper Bot
[Support server](https://discord.gg/xFZu29t)
![Support Server](https://discord.com/api/guilds/742373263593963614/embed.png)

This bot is currently in development. **BE WARNED**
But feel free to use it now and please tell me about any bugs/issues by opening an issue!

## To Do

- Add emoji look up functionality
- Create docs for users as well as people who want to run the bot themselves.


## General Info

This is a general custom made bot.

Features are:

1. Sending messages in channels and being able to edit them with commands.
2. Server stats displayed on voice channels

## Installation

1. Clone this repo
2. Make sure you have the latest version of python and postgresql
3. Setting up the database and roles
4. Creating a discord application and a bot user at the [discord dev website](https://discord.com/developers/applications), setup guide [here](https://discordpy.readthedocs.io/en/latest/discord.html#creating-a-bot-account)
5. [Setting up config](#config)
6. Running `main.py`
7. Inviting the bot to your server, there will be an invite link in the python shell after you run it.

### Setup Example (linux)

```bash
~$ python3 #check if python is installed.
~$ git clone https://github.com/AnotherCat/custom_helper_bot.git # Clone this github repo
~$ python3 -m venv bot-env # Create the python virtual enviroment bot-env
~$ source bot-env/bin/activate # Activate the python virtual enviroment (will need to do this every time you want to be able to run the bot)
(bot-env) ~$ cd custom_helper_bot # Navigate to the main directory for the project.
(bot-env) ~/custom_helper_bot$ pip install -r requirments.txt # Install the required python packages.
# Now you need to setup the config variables, see Config below
(bot-env) ~/custom_helper_bot$ python3 main.py # Run the bot
```

Note: This assumes that you have the following packages installed:

- The latest version of python with pip and venv installed.
- The latest version of git.
- The latest version of postgresql

Some commands may require sudo privileges depending on your system.

For windows do the same, but replace `python3` with python and replace `source bot-env/bin/activate` with `/bot-env/scripts/activate.bat`

## Config

This bot uses a `config.py` file to store config.

### Setting up PostgreSQL
1. Install PostgreSQL
2. Create a role for the bot to use
3. Create the bot's database

```bash
$sudo -u postgres psql
postgres=# CREATE ROLE bot LOGIN PASSWORD 'password' SUPERUSER; # Create the role for the bot to use. You can do it without superuser, look up the docs to see what's needed.
postgres=# CREATE DATABASE bot OWNER bot; # Create a database with the same name as the role, so that you can login easier
postgres=# CREATE DATABASE message_bot OWNER bot; # Create the database the bot will use
postgres=# \q
```
Then enter the values into the postgres_uri config.


### Setting this up

1. Rename `config_example.py` to `config.py`
2. Set the values as per the table below

#### Config Values

| Field         | Type     | Value                                             | Description                                                  | Required | Default |
| :-------------- | :------------------ | :----------------------------------------------------------- | --------------- | :-------------- | --------------- |
| token | string         | Discord Bot Token  | This is the discord bot token.                               | Yes | `""` |
| default_prefix    | string         | String    | This is the default prefix before commands. <br>If a server prefix this will be overidden. | Yes | `"!"` |
| owner   | string | User ID | This will appear in the info box from the `!info` command. Leave as `None` if you don't want this to appear. | No | `None` |
| bypassed_users | int[] | User ids in an array | By adding a user to this this will bypass all user checks. This is useful for if you have set allowed_server, but want some users to still be able to use it. **Dangerous** permission to grant. | No | `[]` |
| uri | string | postgres uri | This gives the bot access to the database. You'll need to setup a postgres user and database. | Yes | see config file |

## Commands

Note: The message commands will accept both text in code blocks and not. If a code block is sent, the triple backticks will be stripped before sending.

Mentioning the bot as a prefix also works for commands.

`<>` Means that that value is required for the command.

`[]` Means that it is not needed at the initial command but may require further input.

| Command                                         | Description                                                  | Who can use it                        |
| ----------------------------------------------- | ------------------------------------------------------------ | ------------------------------------- |
| `!help`                                         | Displays the help embed                                      | `@everyone`                           |
| `!info`                                         | Displays info about the bot                                  | `@everyone`                           |
| `!ping`                                         | Returns the bot-side latency                                 | `@everyone`                           |
| `!send [channel_id] [message_content]`          | Sends a message to a channel. The channel is the channel which channel_id points to. Bot requires send message permissions in this channel. | Requires the management role (if set) |
| `!edit [channel_id] [message_id] [new_content]` | Edits the message that can be found in the channel which channel_id points to. The message **must** be from the bot. | Requires the management role (if set) |
| `!delete [channel_id] [message_id]`             | Deletes the message. The message **must** be from the bot.   | Requires the management role (if set) |
| `!stats update`             | Update the stats channels | Requires the management role (if set) |


## Important Notes

### Updates

I will be using the standard version naming.

If the first number in the tuple is the same, it will not break if you leave config the same. In this case all you have to do it pull the repo as `config.json` is the only file that is user specific and there is no file named that in the repo.
It is still suggested that you read the update notes and update your config as said, but if you don't nothing will break.

If the first number in the tuple changes, this means that it is no longer backwards compatible.
This means that you **must** update your configuration after pulling the version.

> Note, as i have not finalised development of the first stage, i have not released any versions. You are free to use it, but be warned it's still in development.
>
> Please report any bugs you find in the comments.

## Checklist

- [ ] Created a application and bot user.
- [ ] Cloned the repo
- [ ] Installed the required packages (python 3 with pip, installed requirements.txt)
- [ ] Setup required configuration variables (token and default prefix)
- [ ] Renamed `config_example.py` to `config.py`
- [ ] Run bot
- [ ] Invited the bot to your server, and setup the server permissions for it.
