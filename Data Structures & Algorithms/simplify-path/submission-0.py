class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # Split on '/' automatically groups slashes and isolates folder names
        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        # Rebuild canonical path starting with root '/'
        return "/" + "/".join(stack)