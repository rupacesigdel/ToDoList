# ToDoList

## ToDo List Application

A simple web-based ToDo list application built with Django and Bootstrap. This application allows users to add, view, and delete tasks efficiently.

## Contain

- [Features](#features)
- [Demo Video](#demo-video)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Authorization using OPAL](#authorization-using-opal)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Add new tasks with a title and description
- View a list of all tasks
- Search for tasks
- Delete tasks
- undo task
- edit task
- Authorization using OPAL

## Demo Video

[Watch the demo video](https://github.com/rupacesigdel/ToDoList/assets/159915440/5d2dde3c-ce24-4de7-b256-b1042439eb4c)

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default for Django projects)
- **Authorization**: OPAL (Open Policy Agent)

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Docker
- docker-compose

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/rupacesigdel/ToDoList.git
    cd ToDoList
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

6. **Open your browser and visit**:
    ```
    http://127.0.0.1:8000/
    ```

### Authorization using OPAL

This project uses OPAL (Open Policy Agent) for authorization to ensure that only authorized users can access certain tasks.

#### Middleware Setup

The `OPALAuthorizationMiddleware` class is defined to handle authorization using OPAL.

## Usage

- **Add a Task**: Click on the "Add Task" button on the home page, fill in the title and description, and submit.
- **View Tasks**: The tasks will be listed on the tasks page.
- **Delete a Task**: Click the "Delete" button next to the task you want to remove.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration from various online ToDo list tutorials and projects.
- Thanks to the contributors and the open-source community.

---

Feel free to customize this `README.md` file according to your project's specific details and requirements.
