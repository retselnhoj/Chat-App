# Import necessary modules and libraries
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

# Create a Flask app and configure it
app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)

# Dictionary to store rooms and their information
rooms = {}

# Function to generate a unique code for the room
def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
    
    return code

# Route for the home page
@app.route("/", methods=["POST", "GET"])
def home():
    # Clear the session data
    session.clear()

    if request.method == "POST":
        # Get form data from the user
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        # Validate the user input
        if not name:
            return render_template("home.html", error="Please enter a name.", code=code, name=name)

        if join != False and not code:
            return render_template("home.html", error="Please enter a room code.", code=code, name=name)
        
        room = code

        # If the user wants to create a new room, generate a unique code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        # If the user is trying to join an existing room, check if the room exists
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
        
        # Store user data in session and redirect to the room
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))

    return render_template("home.html")

# Route for the room page
@app.route("/room")
def room():
    # Get the room data from the session
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        # If session data is missing or room does not exist, redirect to the home page
        return redirect(url_for("home"))

    # Render the room template with the room data and messages
    return render_template("room.html", code=room, messages=rooms[room]["messages"])

# Event handler for receiving messages from the client
@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return 
    
    # Prepare the message content
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    # Send the message to all clients in the room
    send(content, to=room)
    # Store the message in the room's messages list
    rooms[room]["messages"].append(content)
    # Print the message to the server console
    print(f"{session.get('name')} said: {data['data']}")

# Event handler for client connection
@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        # If the room does not exist, leave the room and return
        leave_room(room)
        return
    
    # Join the room, notify others about the new member, and increment member count
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

# Event handler for client disconnection
@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        # Decrement member count and remove the room if no members left
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    
    # Send a notification to the room about the member leaving
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")

# Start the Flask app with SocketIO
if __name__ == "__main__":
    socketio.run(app, debug=True)
