
# Chat-App
# Chat App Documentation

## Introduction

The Chat App is a simple real-time chat application built using Python and Flask framework on the backend, and Socket.IO for real-time communication between clients. The app allows users to join existing chat rooms or create new ones, and chat with other participants in the same room.

## Features

- User registration: Users can join the chat app by providing their name and a room code to enter an existing room or create a new one.
- Real-time messaging: Messages sent by users are immediately displayed to all participants in the same chat room.
- Unique room codes: When creating a new room, the app generates a unique room code for identification.
- Timestamps: Each message in the chat room is accompanied by a timestamp showing when it was sent.

## Technologies Used

- Python: Backend server and application logic are written in Python.
- Flask: A micro web framework for building web applications in Python.
- Flask-SocketIO: An extension that enables WebSocket support for Flask applications using Socket.IO.
- Socket.IO: A JavaScript library that enables real-time, bidirectional, and event-based communication between the browser and the server.
- HTML/CSS: Frontend templates and styles for the user interface.

## Installation

To run the Chat App on your local machine, follow these steps:

1. Clone the repository from GitHub:

```
git clone <repository_url>
```

2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

3. Run the application:

```
python main.py
```

The app should now be running at `http://127.0.0.1:5000/`.

## Usage

1. Access the Chat App in your web browser by visiting `http://127.0.0.1:5000/`.

2. Home Page:
   - Enter your name in the "Name" field.
   - To join an existing room, enter the room code in the "Room Code" field and click "Join a Room".
   - To create a new room, click "Create a Room".

3. Chat Room:
   - Once you join a room or create a new one, you will be redirected to the chat room.
   - The chat room displays messages from all participants in the room.
   - To send a message, type your message in the input field and click "Send".

4. Real-Time Messaging:
   - Messages sent by any participant will be instantly displayed to all other participants in the chat room.

5. Leave Room:
   - To leave the current chat room, simply close the browser tab or navigate away from the page.

## Screenshots

<img width="263" alt="image" src="https://github.com/retselnhoj/Chat-App/assets/44377868/38c5b89f-22e1-4ef2-a935-674498de4110">

<img width="258" alt="image" src="https://github.com/retselnhoj/Chat-App/assets/44377868/c9745bda-8cf2-44af-b718-ea624b7bc9f0">

<img width="264" alt="image" src="https://github.com/retselnhoj/Chat-App/assets/44377868/eff76ff9-5142-4701-9119-f84aaaea18d8">

<img width="387" alt="image" src="https://github.com/retselnhoj/Chat-App/assets/44377868/09527e18-9050-4f2d-a913-7387775f7911">

## Future Enhancements

- User authentication: Implement user authentication to provide a more personalized experience and avoid duplicate names in the chat rooms.
- Message history: Store and display message history for users joining an existing chat room, allowing them to see previous messages.
- Improved UI: Enhance the user interface with more attractive and responsive design elements.

## Contributors

[List of contributors and their contributions]

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments


