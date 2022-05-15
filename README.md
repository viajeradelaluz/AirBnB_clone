<h1 align="center"><img src='https://i.ibb.co/TtYYJRm/hbnb-original-colors.png' width='250'><br>Airbnb clone - The console</h1>

<p align="center"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"><img src="https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white"><img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white"><img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white"></p>

The AirBnB clone project starts with the goal of the project is to deploy on your server a simple copy of the AirBnB website. Since this is the first part of the project, only a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging), and a website (the front-end) that shows the final product to everybody are implemented.

## Command Interpreter Features

- Create new instances based on User, Amenity, Place, etc.
- Read the instances from `json` files (database)
- Update the instance attributes
- Delete instances

## Start the Command Interpreter

All the files are interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.9.7).

### Requirements

- _Clone the repository:_

```powershell
~$ git clone "https://github.com/viajeradelaluz/AirBnB_clone.git"
```

- _Run the command interpreter in interactive mode:_

```powershell
~/airbnb_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update

(hbnb) quit
~/airbnb_clone$
```

- _Or run the command interpreter in non-interactive mode:_

```powershell
~/airbnb_clone$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update

(hbnb)
~/airbnb_clone$
```

## How to use it

This is a brief description of the commands enabled in the command interpreter to work with the AirBnb program.

| Command | Description                                     | Usage                                                     |
|:-------:|:-----------------------------------------------:|:---------------------------------------------------------:|
| help    | Displays the documented available commands      | `help [command]`                                          |
| EOF     | Exits the command interpreter                   | `EOF`                                                     |
| quit    | Exits the command interpreter                   | `quit`                                                    |
| all     | Prints instances based or not on the class name | `all [classname]` or `all` or `[classname].all()`         |
| create  | Create new instances based on the class name    | `create [classname]` or `[classname.create()]`            |
| show    | Prints instance based on the class name and id  | `show [classname] [id]` or `[classname.show()]`           |
| count   | Retrieve the number of instances of a class     | `[classname].count()`                                     |
| destroy | Deletes an instance                             | `destroy [classname] [id]` or `[classname.destroy([id])]` |
| update  | Updates an instance based on its attributes     | `update [classname] [id] [attribute] [value]`             |

## Examples

#### Working with User instances

```powershell
~/airbnb_clone$ ./console.py
(hbnb) create User
14076693-b62e-48e8-8fe0-005dad73381a
(hbnb) update User 14076693-b62e-48e8-8fe0-005dad73381a email foo@bar.com
(hbnb) update User 14076693-b62e-48e8-8fe0-005dad73381a first_name "John"
(hbnb) update User 14076693-b62e-48e8-8fe0-005dad73381a last_name "Doe"
(hbnb) create User
9eb0dd12-8938-4b36-affb-754ac04cf09f
(hbnb) User.all()
["[User] (ed07cbd6-df6e-418b-abc6-75dc96983e3c) {'id': 'ed07cbd6-df6e-418b-abc6-75dc96983e3c', 'created_at': datetime.datetime(2022, 3, 6, 23, 24, 41, 394353), 'updated_at': datetime.datetime(2022, 3, 6, 23, 24, 41, 394393), 'email': 'foo@bar.com'}", "[User] (14076693-b62e-48e8-8fe0-005dad73381a) {'id': '14076693-b62e-48e8-8fe0-005dad73381a', 'created_at': datetime.datetime(2022, 3, 6, 23, 26, 26, 312789), 'updated_at': datetime.datetime(2022, 3, 6, 23, 26, 26, 312823), 'email': 'foo@bar.com', 'first_name': 'John', 'last_name': 'Doe'}", "[User] (9eb0dd12-8938-4b36-affb-754ac04cf09f) {'id': '9eb0dd12-8938-4b36-affb-754ac04cf09f', 'created_at': datetime.datetime(2022, 3, 6, 23, 28, 18, 164061), 'updated_at': datetime.datetime(2022, 3, 6, 23, 28, 18, 164095)}"]
(hbnb) User.destroy(9eb0dd12-8938-4b36-affb-754ac04cf09f)
(hbnb) all User
["[User] (ed07cbd6-df6e-418b-abc6-75dc96983e3c) {'id': 'ed07cbd6-df6e-418b-abc6-75dc96983e3c', 'created_at': datetime.datetime(2022, 3, 6, 23, 24, 41, 394353), 'updated_at': datetime.datetime(2022, 3, 6, 23, 24, 41, 394393), 'email': 'foo@bar.com'}", "[User] (14076693-b62e-48e8-8fe0-005dad73381a) {'id': '14076693-b62e-48e8-8fe0-005dad73381a', 'created_at': datetime.datetime(2022, 3, 6, 23, 26, 26, 312789), 'updated_at': datetime.datetime(2022, 3, 6, 23, 26, 26, 312823), 'email': 'foo@bar.com', 'first_name': 'John', 'last_name': 'Doe'}"]
(hbnb)
~/airbnb_clone$
```

#### Working with City instances

```powershell
~/airbnb_clone$ ./console.py
(hbnb) City.create()
7e1c3b5c-c5af-466b-87b0-5b0dad4d570c
(hbnb) update City 7e1c3b5c-c5af-466b-87b0-5b0dad4d570c name Kyiv
(hbnb) City.create()
59e1ae95-e2fd-457b-93c7-505f183bf12d
(hbnb) update City 59e1ae95-e2fd-457b-93c7-505f183bf12d name Moscow
(hbnb) City.show(7e1c3b5c-c5af-466b-87b0-5b0dad4d570c)
[City] (7e1c3b5c-c5af-466b-87b0-5b0dad4d570c) {'id': '7e1c3b5c-c5af-466b-87b0-5b0dad4d570c', 'created_at': datetime.datetime(2022, 3, 6, 23, 43, 30, 473375), 'updated_at': datetime.datetime(2022, 3, 6, 23, 43, 30, 473407), 'name': 'Kyiv'}
(hbnb) City.show(59e1ae95-e2fd-457b-93c7-505f183bf12d)
[City] (59e1ae95-e2fd-457b-93c7-505f183bf12d) {'id': '59e1ae95-e2fd-457b-93c7-505f183bf12d', 'created_at': datetime.datetime(2022, 3, 6, 23, 44, 14, 811220), 'updated_at': datetime.datetime(2022, 3, 6, 23, 44, 14, 811241), 'name': 'Moscow'}
(hbnb)
~/airbnb_clone$
```

## Authors

| [<img src="https://avatars.githubusercontent.com/u/87556519" width="110" style="border-radius: 50%"><br><sub>Johanna Alfonso<br><sup>@viajeradelaluz](https://github.com/viajeradelaluz) | [<img src="https://avatars.githubusercontent.com/u/91083840" width="110" style="border-radius: 50%"><br><sub>Alejandro Pineda<br><sup>@Apinedas](https://github.com/Apinedas) |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|

## More information

[Holberton School](https://www.holbertonschool.com)
