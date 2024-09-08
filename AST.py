TOKENS = {
    "CONDITION" : r"[a-zA-Zа-яА-Я_]+\([^)]*\)|\s*[><=!]+\s*\w+", # регулярка ищет выражение по типу method(a) или method(a) > 1
    "IF" : "если",
    "THEN" : "то",
    "ELSE" : "иначе",
    # "BOOL" : ""
    "TRUE" : "true",
    "FALSE" : "false",
}

class UDMLtoken:
    def __init__(self, type_, value):
            self.type = type_
            self.value = value
    
    def __repr__(self):
          return f"Tokens(type={self.type}, value={self.value})"
    
class Node:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value
        self.child = []

    def add_node(self, node):
        self.child.append(node)

    def __repr__(self):
         return f"Nodes(type={self.type}, value={self.value}, child={self.child})"


     
