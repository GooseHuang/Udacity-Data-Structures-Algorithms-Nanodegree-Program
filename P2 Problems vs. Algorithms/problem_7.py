# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,root_handler,not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = not_found_handler         

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
#         print(path_list)
        node = self.root
        for location in path_list:
            if location in node.children:
#                 print('tata')
                node = node.children[location]
            else:
                return RouteTrieNode(self.not_found_handler)
        if not node.handler:
            return RouteTrieNode(self.not_found_handler)
            
        return node

    def insert(self,path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for location in path_list:
            node.insert(location)
            node = node.children[location]
        node.handler = handler
        

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        self.handler = handler
        self.children = {}


    def insert(self, location):
        # Insert the node as before
        if not location in self.children:
            new_node = RouteTrieNode()
            self.children[location] = new_node      



# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(root_handler,not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
#         print(path_list)
        node = self.root.insert(path_list, handler)
        return node     
        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
#         print(path)
#         print(path_list)
        node = self.root.find(path_list)
        return node.handler
        

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split('/')
        path_list = [x for x in path_list if x]
        return path_list
        


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one