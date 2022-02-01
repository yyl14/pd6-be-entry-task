# Entry Task
### Set up

1. git clone
   ```
   git clone https://nas.pdogs.ntu.im:30443/pdogs/pdogs-6/backend-entry-task/entry_test_amber.git
   ```
2. switch directory to `entry_task_amber`
   ```
   cd entry_task_amber
   ```
3. conda env
    - Create a new environment
        ```
        conda create --name my-blog python=3.9
        ```
    - Activate environment
        ```
        conda activate my-blog
        ```
    - Install dependencies
        ```
        pip install -r requirements.txt
        ```
4. set up database
   - install Docker
   - build all needed containers
     ```
     docker-compose up
     ```
   - install DBeaver
5. fastapi framework
    - Run app
        ```
        uvicorn main:app --reload
        ```
    - Open API docs in browser
        ```
        http://127.0.0.1:8000/docs
        ```
