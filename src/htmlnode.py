
# tag - string, tag HTML name
# value - string, value of HTML
# children - list of HTMLNode objects representing the children
# props - dictionary representing the attributes of HTML tag 

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    #shows what is in nodes
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        if self.tag is None:
            return self.value
        
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"