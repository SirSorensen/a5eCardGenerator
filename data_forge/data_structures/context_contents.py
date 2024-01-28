class Text:
    def __init__(self, content: str, is_title : bool = False):
        self.content = content
        self.is_title = is_title

    def __str__(self):
        return self.content



class Link(Text):
    def __init__(self, content: str, link: str, is_title : bool = False):
        super().__init__(content, is_title=is_title)
        self.link = link



class Paragraph:
    def __init__(self):
        self.text_list : list[Text] = []
        self.next = None
    
    def __add(self, text: Text):
        stripped_str = text.content.rstrip()
        if stripped_str != '' or stripped_str is not None:
            self.text_list.append(text)
    
    def add_text(self, text: str):
        text_obj = Text(text)
        self.__add(text_obj)

    def add_link(self, text: str, link: str):
        link_obj = Link(text, link)
        self.__add(link_obj)

    def add_title_text(self, text: str):
        title_obj = Text(text, is_title=True)
        self.__add(title_obj)

    def __str__(self):
        return ' '.join(str(text) for text in self.text_list)

    def empty(self):
        return len(self.text_list) == 0



class Paragraphs:
    def __init__(self):
        self.start : Paragraph | None = None
        self.current : Paragraph | None = self.start
    
    def add_paragraph(self, paragraph: Paragraph):
        if paragraph.empty():
            return
        
        if not isinstance(paragraph, Paragraph):
            raise ValueError(f"Expected Paragraph object, got {str(type(paragraph))}")
        
        if self.start is None:
            self.start = paragraph
            self.current = self.start
        else:
            self.current.next = paragraph
            self.current = self.current.next

    
    def __str__(self):
        acc_str = str(self.start)
        cur = self.start.next

        while cur is not None:
            acc_str += '\n' + str(cur)
            cur = cur.next
        return acc_str

    def to_list(self):
        acc_list = [self.start]
        cur = self.start.next

        while cur is not None:
            acc_list.append(cur)
            cur = cur.next
        return acc_list
