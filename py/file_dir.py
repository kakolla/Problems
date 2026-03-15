"""
# Implement a function called “cd”, which given a PWD and an input path, 
outputs the directory the operating system should switch to:
"""

def resolve_symlink(path: str, symlinkmap: dict[str, str]) -> str:
    visited = set()

    while path in symlinkmap:
        if path in visited:
            raise ValueError("Symlink loop detected")
        visited.add(path)

        path = symlinkmap[path]

    return path


def cd(pwd: str, input: str, symlinkmap: dict[str, str]) -> str:
    if input.startswith("/"):
        paths = []
    else:
        paths = pwd.split("/")

    steps = input.split("/")

    for s in steps:
        if s == "" or s == ".":
            continue
        elif s == "..":
            if paths:
                paths.pop()
        else:
            paths.append(s)

        # normalize current path
        current = "/".join(paths)
        if not current.startswith("/"):
            current = "/" + current

        # resolve symlink fully
        current = resolve_symlink(current, symlinkmap)

        # update paths after resolution
        paths = current.split("/")

    return "/" + "/".join(filter(None, paths))
    


    



# def cd(pwd: str, input: str) -> str:
#     paths = pwd.split("/")
#     steps = input.split("/")
#     for s in steps:
#         if s == '.':
#             continue
#         elif s == '..':
#             paths.pop()
#         else:
#             # folder name
#             paths.append(s)
    
#     return "/".join(paths)
    


# print(cd("/home/bugs", "."))
# print(cd("/home/bugs", "bunny"))
# print(cd("/home/bugs", "../daffy"))
   
print(cd("/home/bugs", "lola/../basketball", {"/home/bugs/lola":"/home/lola"}))
# "/home/lola/basketball"