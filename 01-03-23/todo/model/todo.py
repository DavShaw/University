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

    def pending_todos(self):
        return [self.todos[obj_key] for obj_key in self.todos if not(self.todos[obj_key].completed)]

    def completed_todos(self):
        return [self.todos[obj_key] for obj_key in self.todos if (self.todos[obj_key].completed)]

    def tags_todo_count(self):
        
        all_objects = self.todos.values()
        
        all_tags = []

        return_dict = {}

        #Take all tags from all objects
        
        for i in all_objects:
            if not (all_objects.tags in all_tags):
                all_tags.append(all_objects.tags)
        
        
        for j in all_objects:
            counter = 0
            for k in all_tags:
                if j.tags == all_tags[k]:
                    counter += 1
                return_dict[all_tags[k]] = counter

        return return_dict
        
