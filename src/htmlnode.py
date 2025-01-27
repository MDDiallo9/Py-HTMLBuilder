class HTMLNode():
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        result = ""
        for key,value in self.props.items() :
            result += f'{key}="{value}" '
        return result.strip()
    
    def __repr__(self):
        print(f"HTMLNode({self.tag},{self.value},{self.children},{self.props})")


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value,None, props)
       

    def to_html(self):
        super().props_to_html()
        if self.value == None :
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None :
            return self.value
        return f'<{self.tag}{" " if self.props else ""}{self.props_to_html()}>{self.value}</{self.tag}>'
        

class ParentNode(HTMLNode):
    def __init__(self, tag=None,children = None , props=None):
        super().__init__(tag,None, children, props)

    def to_html(self):
        children = ""
        if self.tag == None :
            raise ValueError("No tag")
        if self.children == None :
            raise ValueError("no children")
        for child in self.children:
            if isinstance(child,ParentNode):
                children  += child.to_html()
            else:    
                children += child.to_html()
        return f'<{self.tag}{" " if self.props else ""}{self.props_to_html()}>{children}</{self.tag}>'