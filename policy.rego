package todo

default allow = false

# Allow access if user is an admin
allow {
    input.user.role == "admin"
}

# Allow access to own tasks
allow {
    input.user.id == input.task.owner_id
}
