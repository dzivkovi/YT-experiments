""" import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=pvDOnqGbghU')
# yt.bypass_age_gate()
caption = yt.captions['a.en']
print(caption.generate_srt_captions())
"""


from pytube import YouTube


def fetch_transcript(video_url):
    """
    Function to fetch the English transcript of a YouTube video.
    """
    yt = YouTube(video_url)
    caption = yt.captions.get_by_language_code('en')
    return caption.generate_srt_captions()


VIDEO_URL = "https://www.youtube.com/watch?v=pvDOnqGbghU"
transcript = fetch_transcript(VIDEO_URL)
print(transcript)
