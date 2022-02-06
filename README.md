# Entry Task --blog backend
## Set up

1. git clone
   ```
   git clone https://nas.pdogs.ntu.im:30443/pdogs/pdogs-6/backend-entry-task/entry_test_amber.git
   ```
2. switch directory to `entry_task_amber`
   ```
   cd entry_task_amber
   ```
3. conda env
    - create a new environment
        ```
        conda create --name my-blog python=3.9
        ```
    - activate environment
        ```
        conda activate my-blog
        ```
    - install dependencies
        ```
        pip install -r requirements.txt
        ```
    - set up environment
      ```
      cp .env.example .env
      cp docker-compose.yaml.example docker-compose.yaml
      ```
4. set up database
   - install Docker
   - build all needed containers
     ```
     docker-compose up
     ```
   - install DBeaver and connect to database (Optional)
5. fastapi framework
    - Run app
        ```
        uvicorn main:app --reload
        ```
    - Open API docs in browser
        ```
        http://127.0.0.1:8000/docs
        ```
## Database schema

| post    | type    |
|---------|---------|
| id      | integer |
| author  | string  |
| title   | string  |
| content | text    |

| comment | type      |
|---------|-----------|
| id      | integer   |
| post_id | integer   |
| author  | string    |
| content | text      |

## Input and Output Class

### Input Class
#### PostIn 
    author: str
    title: str
    content: str
#### CommentIn
    author: str
    content: str

### Output Class
#### PostOut
    id: int
    author: str
    title: str
    content: str
#### CommentOut
    id: int
    author: str
    content: str
    post_id: int


### APIs

#### browse post `GET /post`
```
input: None
output: list[PostOut]
```

#### delete post `DELETE /post`
```
input: post_id
output: Post id {post_id} is deleted.
```

#### add post `POST /post`
```
input: [PostIn]
output: [PostOut]
```

#### read post `GET /post/{post_id}`
```
input: post_id
output: [PostOut]
```

#### edit post `PATCH /post/{post_id}`
```
input:
   post_id
   title (Optional)
   content (Optional)
output: [PostOut]
```

#### browse comment `GET /post/{post_id}/comment`
```
input: post_id
output: list[CommentOut]
```

#### add comment `POST /post/{post_id}/comment`
```
input: [CommentIn]
output: [CommentOut]
```