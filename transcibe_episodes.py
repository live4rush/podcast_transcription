import os
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Create the PodcastTranscriptions directory if it doesn't exist
transcriptions_dir = "PodcastTranscriptions"
if not os.path.exists(transcriptions_dir):
    os.makedirs(transcriptions_dir)

# List all MP3 files in the PodcastEpisodes directory
podcast_dir = "PodcastEpisodes"
mp3_files = [f for f in os.listdir(podcast_dir) if f.endswith('.mp3')]

total_files = len(mp3_files)

# Transcribe each episode
for index, mp3_file in enumerate(mp3_files, start=1):
    title = os.path.splitext(mp3_file)[0]

    # Check if transcription file already exists
    txt_filename = title + ".txt"
    txt_path = os.path.join(transcriptions_dir, txt_filename)
    if os.path.exists(txt_path):
        print(
            f'Skipping "{title}" - {index}/{total_files} (transcription already exists)')
        continue

    print(f'Transcribing "{title}" - {index}/{total_files}')

    mp3_path = os.path.join(podcast_dir, mp3_file)
    result = model.transcribe(audio=mp3_path,
                              fp16=False, task="transcribe")

    # Save the transcription to a .txt file
    with open(txt_path, 'w') as txt_file:
        txt_file.write(result["text"])

print("All episodes transcribed and saved in the PodcastTranscriptions directory!")
