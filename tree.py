from tags import iter_dict

class Tree(object):
    
    "Generic tree node."

    def __init__(self, name='root', children=None, text=None):
        self.name = name
        self.children = []
        self.text = text

        if children is not None:
            for child in children:
                self.add_child(child)
    
    def __repr__(self):
        return self.name

    def to_string(self):
        return (self.text.format_map(iter_dict))
    
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def get_children(self):
        return self.children