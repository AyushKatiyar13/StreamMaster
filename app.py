import yt_dlp
import os
from flask import Flask, render_template, request, send_file, redirect, url_for

app = Flask(__name__)

# Directory to temporarily store downloaded videos
DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_link = request.form.get('videoLink')
    video_quality = request.form.get('videoQuality', 'best')  # Default to 'best' if not provided

    if not video_link:
        return redirect(url_for('index'))

    try:
        # Map quality to yt-dlp format codes
        quality_map = {
            '1080p': 'bestvideo[height<=1080]+bestaudio/best',
            '720p': 'bestvideo[height<=720]+bestaudio/best',
            '480p': 'bestvideo[height<=480]+bestaudio/best',
            '360p': 'bestvideo[height<=360]+bestaudio/best',
            'best': 'best'  # Automatically chooses the best format available
        }

        format_code = quality_map.get(video_quality, 'best')

        ydl_opts = {
            # 'proxy': 'http://49.228.131.169',
            'format': format_code,
            'outtmpl': os.path.abspath(os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')),
            'ffmpeg_location': r'C:\Users\Ankita\OneDrive\Desktop\New folder\ffmpeg-7.0.2-full_build\ffmpeg-7.0.2-full_build\bin',  # Set your ffmpeg path here
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(video_link, download=True)
            video_title = result.get('title', 'video')  # Get video title
            video_ext = result.get('ext', 'mp4')  # Get video extension
            video_filename = f"{video_title}.{video_ext}"  # Full filename
            ydl.download([video_link])

            # Print the file path for debugging
            video_filepath = os.path.join(DOWNLOAD_DIR, video_filename)
            print(f"Video saved to: {video_filepath}")

        # Check if the file exists
        if os.path.exists(video_filepath):
            # Send the file to the user for download
            return send_file(video_filepath, as_attachment=True)
        else:
            return "File was not found after downloading."

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
