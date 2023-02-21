class User:
    def __init__(self,id):
        self.id = id
        self.following = set()
        self.followers = set()  
        
class Tweet:
    def __init__(self,tweetId,userId):
        self.id = tweetId
        self.postedBy = userId


class Twitter:

    def __init__(self):
        self.users = {}
        self.newsFeed = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
            
        user = self.users[userId]
        
        tweet = Tweet(tweetId,userId)
        self.newsFeed.append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
            
        if userId not in self.users:
            return feed
        
        user = self.users[userId]
        counter = 0
        for ind in range(len(self.newsFeed)-1,-1,-1):
            news = self.newsFeed[ind]
            
            if counter==10:
                break
            poster = self.users[news.postedBy]
            
            if  poster == user or poster in user.following:
                feed.append(news.id)
                counter += 1
                
            
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
            
        user1 = self.users[followerId]
        
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
            
        user2 = self.users[followeeId]
        
        user2.followers.add(user1)
            
        user1.following.add(user2)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
            
        user1 = self.users[followerId]

        user2 = self.users[followeeId]
        
        if user1 in user2.followers:
            user2.followers.remove(user1)
            
        if user2 in user1.following:
            user1.following.remove(user2)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)