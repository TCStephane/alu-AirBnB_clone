# AirBnB Clone - The Console

## Description
This project is the first step toward a full AirBnB clone web application.
It implements a command interpreter to manage AirBnB objects (User, State,
City, Place, Amenity, Review) and a file storage engine that persists them
as JSON.

Flow: Instance <-> Dictionary <-> JSON string <-> file

## Command Interpreter

### How to start it
Interactive mode:
```
$ ./console.py
(hbnb)
```

Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
```

### How to use it
| Command | Usage |
|---------|-------|
| `help` | `help` or `help <command>` |
| `quit` / `EOF` | Exit the program |
| `create` | `create <class name>` |
| `show` | `show <class name> <id>` |
| `destroy` | `destroy <class name> <id>` |
| `all` | `all` or `all <class name>` |
| `update` | `update <class name> <id> <attribute name> "<attribute value>"` |

Available classes: `BaseModel`, `User`, `State`, `City`, `Amenity`,
`Place`, `Review`.

### Examples
```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
$
```

## Testing
```
python3 -m unittest discover tests
```

## Authors
See the [AUTHORS](AUTHORS) file.
