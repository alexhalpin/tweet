import os, sys
import tweepy


def main():
    X_CONSUMER_KEY = os.environ.get("X_CONSUMER_KEY")
    X_CONSUMER_KEY_SECRET = os.environ.get("X_CONSUMER_KEY_SECRET")
    X_ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN")
    X_ACCESS_TOKEN_SECRET = os.environ.get("X_ACCESS_TOKEN_SECRET")

    client = tweepy.Client(
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET,
        consumer_key=X_CONSUMER_KEY,
        consumer_secret=X_CONSUMER_KEY_SECRET,
    )

    args = sys.argv[1:]
    tweet = " ".join(args)

    try:
        tweet = client.create_tweet(text=tweet)
        print("done")

    except Exception as e:
        print(f"tweepy error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
