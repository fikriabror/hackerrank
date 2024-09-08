'''
This code is designed to identify paths that are writable and have readable parent paths. Specifically, given two lists of paths (writable and readable), the code identifies paths that:

Are in the writable list.
Have at least one parent path in the readable list.
'''

import os

def get_parent_paths(path):
    parents = []
    while path != "/":
        path = os.path.dirname(path)
        if path != "/":
            parents.append(path)
    parents.append("/")
    return parents


def find_parent_children(writable, readable):
    result = set()
    readable_set = set(readable)
    for path in writable:
        # result.add(path)
        
        for parent in get_parent_paths(path):
            if parent in readable_set:
                result.add(path)
                result.add(parent)
        
    return sorted(result)


readable = ["/a/b/c","/a/b", "/a", "/b/c", "/b","/c/d", "/d" ]
writable = ["/b/c","/c/d","/a/b/c"]

print(find_parent_children(writable, readable))