from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter

def fetch_and_save_transcript(video_id, output_path='captions.srt'):
    """
    Function to fetch the English transcript of a YouTube video and save it to a file.
    
    :param video_id: ID of the YouTube video.
    :param output_path: Path where the captions will be saved.
    """
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        
        # Format the transcript to SRT
        formatter = SRTFormatter()
        srt_captions = formatter.format_transcript(transcript)
        
        # Save the captions to a file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(srt_captions)
        print(f"Captions saved to {output_path}")
    except Exception as e:
        print(f"Error fetching captions: {e}")

# https://www.youtube.com/watch?v=pvSL0q6hPfo
VIDEO_ID = "pvSL0q6hPfo"  # Extract the video ID from the URL
OUTPUT_PATH = "captions.srt"  # Specify your desired output path

fetch_and_save_transcript(VIDEO_ID, OUTPUT_PATH)
