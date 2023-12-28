# chat-ui-dashboard

## Overview
This project provides a web-based interface to view and manage chat logs from [HuggingFace's ChatUI](https://github.com/huggingface/chat-ui). It is designed to interact seamlessly with the ChatUI, offering an intuitive way to access and analyze conversation data. The application includes a backend server for data handling and a responsive frontend built with Svelte.

## Features
- **User-Centric Log Viewing:** Allows users to view conversation lists and details per user.
- **Future Developments:**
  - Filter options to search and sort logs.
  - Log analysis features including usage trends and more.

## Getting Started

### Prerequisites
- An instance of [HuggingFace's ChatUI](https://github.com/huggingface/chat-ui) up and running.
- Node.js
- Svelte

### Installation

1. **Clone the Repository:**
   ```bash
   git clone [repository URL]
   ```

2. Set Up Backend Server:
- Navigate to the backend directory.
- Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Start the backend server:
  ```
  python server.py mongo://[your-mongodb-url]
  ```

3. Set Up Frontend Application:
- Navigate to the frontend directory.
- Install the required dependencies:
  ```
  npm install
  ```
- Start the frontend application:
  ```
  npm run dev
  ```

## Usage
After starting both the backend and frontend, access the web application through your browser at http://localhost:5000 (or the configured port). Navigate through the interface to view chat logs per user.

## Contributing
We welcome contributions! Please fork the repository and create a pull request with your changes. For major changes, open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
