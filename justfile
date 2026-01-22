[default]
@run file="master/main":
    source .venv/bin/activate
    echo "======== MASTER ========"
    python3 src/{{file}}.py

@run-task name:
    source .venv/bin/activate
    echo "======== TASK: {{name}} ========"
    python3 src/tasks/{{name}}/main.py

@create-task name:
    mkdir src/tasks/{{name}}
    cp src/master/main.py src/tasks/{{name}}/main.py
    echo "created task {{name}}"

@open-task name:
    $HOME/bin/nvim-macos-x86_64/bin/nvim src/tasks/{{name}}/main.py

@open-task-doc name:
    $HOME/bin/nvim-macos-x86_64/bin/nvim src/tasks/{{name}}/README.md

@list-tasks:
    ls src/tasks

alias t := run-task
alias r := run-task
alias c := create-task
alias o := open-task
alias d := open-task-doc
alias l := list-tasks
alias list := list-tasks

