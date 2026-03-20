



from collections import defaultdict
class SocialSystem:
    def __init__(self):
        self.user_follow_mp = defaultdict(list) # all ppl the key follows
        self.id = 0
        

    def follow(self, a: int, b: int) -> None:
        # user a follows b
        self.user_follow_mp[a].append((b, self.id)) # store with snapshot (person, snap_id)

    def unfollow(self, a: int, b: int) -> None:
        # user a unfollows b
        i = 0
        while i < len(self.user_follow_mp[a]):
            # iter through everyone a follows
            elem = self.user_follow_mp[a][i]
            if elem[0] == b and elem[1] == self.id: # match current snapshot only
                self.user_follow_mp[a][i] = self.user_follow_mp[a][-1]
                self.user_follow_mp[a].pop() # remove end
                # swap with end delete
            else:
                i += 1

        pass

    def snapshot(self) -> int:
        # take snapshot by copying all existing follows to new snapshot
        curr = self.id
        self.id += 1
        for followings in self.user_follow_mp.values():
            # basically, copy current followings to next 
            # snapshot (havent unfollowed it)
            to_copy = [(person, self.id) for person, snapid in followings if snapid == curr]
            followings.extend(to_copy)



        return curr
    
    def is_following(self, a: int, b: int, snapshot_id: int) -> bool:
        # return if a - b true at id
        for elem in self.user_follow_mp[a]:
            if elem[0] == b and elem[1] == snapshot_id:
                return True
        return False

    def get_followers(self, b: int, snapshot_id: int) -> list[int]:
        # all followers at snap id who r following b
        ans = []
        for a_id, followings in self.user_follow_mp.items():
            for p in followings:
                if p[0] == b and p[1] == snapshot_id:
                    ans.append(a_id)
        return ans
        
    def get_followees(self, a: int, snapshot_id: int) -> list[int]:
        # all followees at snap id who a follows
        return [t[0] for t in self.user_follow_mp[a] if t[1] == snapshot_id]
            
    def recommend_new_follow(self, a: int, snapshot_id: int, k: int = 5) -> list[int]:
        """
        Start from the people this user already follows, then look at who each of those people follow. Among these candidates, we count how many times each person is followed by the user’s followings, and finally select the top k people with the highest counts as the recommendation results.
        """
        candidates = []
        a_followings = self.get_followees(a, snapshot_id)
        for c in a_followings:
            candidates.extend(self.get_followees(c, snapshot_id))
            

        ans = []
        for c in candidates:
            # check how many times c is followed by a's followings
            times = 0
            for a_follow in a_followings:
                if a_follow in self.get_followers(c, snapshot_id):
                    times += 1
            # check if a also follows c, if not ignore:
            if c not in a_followings and c != a:
                ans.append((c, times))
        ans = list(set(ans)) # dedupe
        ans.sort(reverse=True, key=lambda x: x[1])

        return [t[0] for t in ans[:k]]



if __name__ == "__main__":
    s = SocialSystem()
    s.follow(1,2)
    s.follow(2, 3)
    print(s.snapshot())
    print(s.is_following(1,2,0))
    s.unfollow(1, 2)
    print(s.snapshot())
    print(s.is_following(1,2,1))
    print(s.user_follow_mp)
    print(s.is_following(1,2, 2))

    
















