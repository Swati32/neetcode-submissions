class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)     # user -> list of (time, tweet_id)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        # The user always sees their own tweets too
        authors = set(self.follows[userId])
        authors.add(userId)

        for author in authors:
            posts = self.tweets[author]
            if posts:
                idx = len(posts) - 1
                time, tweet_id = posts[idx]
                heapq.heappush(heap, (-time, tweet_id, author, idx - 1))
        
        while heap and len(feed) < 10:
            _, tweet_id, author, idx = heapq.heappop(heap)
            feed.append(tweet_id)

            if idx >= 0:
                time, prev_tweet_id = self.tweets[author][idx]
                heapq.heappush(heap, (-time, prev_tweet_id, author, idx - 1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
