def get_todos():
  with open("todo.txt",'r') as file_local:
      todos_local=file_local.readlines()
  return todos_local

def write_todos(todo_arg,file_path="todo.txt"):
  with open(file_path,"w") as file_local:
      file_local.writelines(todo_arg)
if __name__ == "__main  __":
    print(get_todos())
