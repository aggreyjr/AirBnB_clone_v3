AirBnB_clone_v3 Readme
Introduction
Welcome to the AirBnB_clone_v3 project! This repository contains the source code for a Flask-based web application that serves as a clone of the Airbnb platform. The project focuses on implementing and testing various features, including improvements to storage, API endpoints, and handling different types of objects such as states, cities, amenities, users, and places.

Why Unit Tests?
In software development, unit tests are crucial for ensuring the stability and reliability of the codebase. The provided statistics showcase the number of assertions in the project's tests, emphasizing the importance of maintaining a comprehensive test suite. All existing tests must pass, and additional tests should be added as needed to cover new features and functionalities.

Project Structure
Repository: AirBnB_clone_v3
Branch: storage_get_count
Files:
models/engine/db_storage.py
models/engine/file_storage.py
tests/test_models/test_engine/test_db_storage.py
tests/test_models/test_engine/test_file_storage.py
Improving Storage
The current task involves enhancing the storage mechanism by adding two new methods: get and count. The details of these methods and usage examples can be found in the provided code snippet.

To contribute, create a pull request on GitHub and request a peer review for merging.

API Development
The project is evolving to include API functionality. The current tasks involve creating endpoints to retrieve the status of the API, fetch statistics, handle 404 errors, and manage objects such as states, cities, amenities, users, and places. Follow the instructions in the provided code snippets to implement and test these features.

Running the API
To run the API locally, set the required environment variables and execute the following command:

HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db 
HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
