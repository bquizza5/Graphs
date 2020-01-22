import names
import random
from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        # print(user_id, friend_id)
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return "WARNING: You cannot be friends with yourself"
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return "WARNING: Friendship already exists"
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for _ in range(num_users):
            # print(len(self.friendships))
            self.add_user(names.get_first_name())

        # Create friendships
        friendships_added = 0
        while friendships_added < int(avg_friendships/2 * num_users):
            if self.add_friendship(random.randint(1,num_users), random.randint(1,num_users)) == None:
                friendships_added += 1
                # print(friendships_added)
            




    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited = {}  # Note that this is a dictionary, not a set
        # connections = []
        # q = Queue()
        # q.enqueue(user_id)


        # while q.size() > 0:
        #     friend = q.dequeue()
        #     if friend not in connections:
        #         connections.append(friend)
        #         for new_friend in self.friendships[friend]:
        #             q.enqueue(new_friend) 

        # last_connection = user_id
        # for connection in connections:
        #     if connection == connections[0]:
        #         visited[connection] = [connection]
                
        #     else:
        #         visited[connection] = visited[last_connection][:]
            
        #         last_connection = connection

        visited = {}

        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([user_id])

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Look at the last user in the path...
            current_friend = path[-1]
            # If the user has not been visited
            if current_friend not in visited:
                # Mark as visited and add their path
                visited[current_friend] = path
                # Add a path to each neighbor to the queue
                for friend in self.friendships[current_friend]:
                    new_path = path.copy()
                    new_path.append(friend)
                    q.enqueue(new_path)

        # return visited





        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

# for _ in range(0,100):
#     print(names.get_first_name())

# print(random.randint(0,1))