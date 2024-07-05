import os, sys, argparse, io
import PIL.ImageGrab
import tweepy
import PIL


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

    auth = tweepy.OAuth1UserHandler(
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET,
        consumer_key=X_CONSUMER_KEY,
        consumer_secret=X_CONSUMER_KEY_SECRET,
    )
    api = tweepy.API(auth)

    parser = argparse.ArgumentParser(description="send tweets from the terminal")

    parser.add_argument(
        "tweet",
        nargs="?",
        type=str,
        help="the tweet (must be surrounded by single quotes)",
    )
    parser.add_argument(
        "-ci",
        "--clipboard_image",
        action="store_true",
        help="attach clipboard image to tweet",
    )
    args = parser.parse_args()

    # tweet contents
    tweet = args.tweet
    media_ids = None

    # get clipboard image
    if args.clipboard_image:
        image = PIL.ImageGrab.grabclipboard()

        if image is None:
            print(f"no image in clipboard", file=sys.stderr)
            sys.exit(1)

        try:
            image_binary = io.BytesIO()
            image.save(image_binary, format="PNG")
            image_binary.seek(0)

        except Exception as e:
            print(f"error converting image to binary: \n{str(e)}", file=sys.stderr)
            sys.exit(1)

        # upload screenshot
        try:
            media = api.media_upload(
                "screenshot.png",
                file=image_binary,
            )

            media_ids = [media.media_id_string]
            print("image uploaded")

        except Exception as e:
            print(f"error uploading image: \n{str(e)}", file=sys.stderr)
            sys.exit(1)

    # check if tweet is empty
    if tweet is None and media_ids is None:
        print(f"error: empty tweet", file=sys.stderr)
        sys.exit(1)

    # post tweet
    try:
        client.create_tweet(text=tweet, media_ids=media_ids)
        print("done")

    except Exception as e:
        print(f"error creating tweet: \n{str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
