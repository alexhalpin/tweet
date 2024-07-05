# tweet

tweet from the command line

requires the following environment variables

```
X_CONSUMER_KEY
X_CONSUMER_KEY_SECRET
X_ACCESS_TOKEN
X_ACCESS_TOKEN_SECRET
```

oauth1 tokens and secrets obtained via the twitter developer console

## usage

use single quotes or special characters like $ will get parsed by the shell
add the -ci flag to attach the image stored in your clipboard to the tweet

```
python tweet.py '{TWEET}'
```

