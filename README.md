# python-discordtokengrabber
Searches for a discord user's token with their user ID
## Usage/Examples

```python
from tokengrabber import search

# Replace with the actual user ID and channel ID
user_id = 123456789012345678
channel_id = 987654321098765432

# Perform the search
token = search(user_id, channel_id)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Disclaimer

This library is nearly useless, as it would take a very long time to find a Token. It is more of a proof of concept.

Use this library responsibly and only for educational purposes.

**Warning:** The usage of this library to retrieve Discord tokens may violate Discord's [Terms of Service](https://discord.com/terms) and [Developer Terms of Service](https://discord.com/developers/docs/legal). Unauthorized access to user data or any actions that violate Discord's policies can result in serious consequences, including but not limited to account suspension or banning.

By using this library, you acknowledge and understand the potential risks associated with it. The developer of this library is not responsible for any actions taken by users that violate Discord's terms. Use this library at your own risk and only for educational purposes.

**Note:** Always ensure that your application complies with the terms and policies of any third-party service you interact with, including Discord. Use responsibly and consider the potential impact on user privacy and platform integrity.
