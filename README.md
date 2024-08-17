# StreamMaster 🎥

Welcome to **StreamMaster**! 🌟 StreamMaster is a sleek and intuitive web application designed to help you download YouTube videos, shorts, and playlists with ease. 

[![StreamMaster](https://img.shields.io/badge/Visit-StreamMaster-brightgreen)](https://streammaster.onrender.com)

## Table of Contents 📋

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Running Locally](#running-locally)
- [Usage Instructions](#usage-instructions)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features 🚀

- **User-Friendly Interface**: Easily input YouTube links and select video quality.
- **Quality Selection**: Choose from various video qualities such as 1080p.
- **Dark Theme**: Modern dark-themed design for a comfortable viewing experience.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used 🛠️

- **Python**: Backend development with Flask.
- **Flask**: Web framework for handling requests and routing.
- **yt-dlp**: Tool for downloading videos from YouTube.
- **HTML/CSS/JavaScript**: Frontend technologies for creating a responsive user interface.
- **Nginx**: Proxy server configuration for handling requests.
- **Vercel**: Deployment platform for hosting the application.

## Installation & Setup 🛠️

To run StreamMaster on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/streammaster.git
   cd streammaster
   ```

2. **Create a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up `ffmpeg`**:
   - Download and extract `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html).
   - Update the `ffmpeg_location` in `app.py` with the path to your `ffmpeg` binary. Example:
     ```python
     'ffmpeg_location': r'C:\Program Files\ffmpeg-7.0.2-full_build\ffmpeg-7.0.2-full_build\bin'
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your browser and go to [http://localhost:5000](http://localhost:5000).

## Running Locally 🖥️

1. Ensure all dependencies are installed.
2. Start the Flask application by running `python app.py`.
3. Visit `http://localhost:5000` in your web browser to use the application.

## Usage Instructions 📥

1. **Open StreamMaster** in your web browser.
2. **Enter** the YouTube video, Shorts, or playlist link in the input field.
3. **Select** the desired video quality from the dropdown menu.
4. **Click** the "Download" button to start the download process.
5. **Wait** for the download to complete. The downloaded file will be saved to your local storage.

## Troubleshooting 🛠️

- **Error: Precondition Check Failed**: This may occur if YouTube blocks access. Try using a VPN to bypass restrictions.
- **Download Issues**: Ensure `ffmpeg` is correctly installed and the path is properly set in `app.py`.

## See the Interface 🌐

Check out the live interface of StreamMaster here: [StreamMaster Live](https://streammaster.onrender.com).

## Contributing 🤝

We welcome contributions to improve StreamMaster! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Thankyou 😊
