from typing import Any, Dict, List

import tweepy
from pymongo import InsertOne

from src.connection import trends_collection
from src.constants import BRAZIL_WOE_ID
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get trending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = api.trends_place(woe_id)
    return trends[0]["trends"]


def get_trends() -> List[Dict[str, Any]]:
    """Get trending topics persisted in MongoDB.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = trends_collection.find({}, {"_id": 0})
    return list(trends)


def save_trends() -> None:
    """Get trends topics and save on MongoDB."""
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    requests = [InsertOne(trend) for trend in trends]
    trends_collection.bulk_write(requests)
