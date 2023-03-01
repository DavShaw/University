class Todo:
    code_id: int
    title: str
    description: str
    completed: bool
    tags: (list[str])

    def __str__(self):
        return f"{self.code_id} - {self.title}"

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.tags = []
        self.completed = False

    def mark_completed(self):
        self.completed = True
    
    def add_tag(self, tag_to_add: str):
        if tag_to_add not in self.tags:
            self.tags.append(tag_to_add)
    

     

    



class TodoBook:

    todos: dict

    def __init__(self):
        self.todos: dict = {}

    def add_too(self, title: str, description: str):
        generated_id: int = len(self.todos) + 1
        Creating_object: Todo = Todo()
        self.todos[generated_id] = Creating_object
        return generated_id

    
