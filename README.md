# Пароль от админки:
#### username - sultan
#### password - root
___

# Инструкция к API для проектов и задач
### Проект
#### 1. Детальный просмотр проекта
+ GET http://127.0.0.1:8000/api/project/detail/1

  + (id 1 для примера)
  
#### 2. Редактирование проекта
+ PUT http://127.0.0.1:8000/api/project/update/1
  + Для этого нужно отправить body:
  
    ```python
    {
      "id": 1,
      "name": "Project-1",
      "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque, distinctio!",
      "start_date": "2023-04-03",
      "expiration_date": "2023-06-22"
    }
    ```
  #### 3. Удаление проекта
  + DELETE http://127.0.0.1:8000/api/project/delete/1
  ___
  
  ## Задача
  #### 1. Детальный просмотр задачи
  + GET http://127.0.0.1:8000/api/project/task/detail/8
  
    + (id 8 для примера)
    
#### 2. Редактирование задачи
+ PUT http://127.0.0.1:8000/api/project/task/update/8
  + Для этого нужно отправить body:
  
     ```python
     {
        "summary": "Task-2",
        "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque, distinctio!",
        "project": 1,
        "status": 2,
        "type": [
            1
        ],
        "created": "2023-03-08T18:54:54.732000Z",
        "updated": "2024-10-27T18:55:25.579000Z"
     }
     ```
#### 3. Удаление задачи
+ DELETE http://127.0.0.1:8000/api/project/task/delete/8
