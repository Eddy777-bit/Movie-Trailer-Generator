from googleapiclient.discovery import build

# Fetch YouTube video analytics
def fetch_video_analytics(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(part="statistics", id=video_id)
    response = request.execute()
    stats = response['items'][0]['statistics']
    print(f"Video Stats for {video_id}: {stats}")
    return stats

# Example usage
API_KEY = "YOUR_YOUTUBE_API_KEY"
VIDEO_ID = "YOUR_TRAILER_VIDEO_ID"
fetch_video_analytics(VIDEO_ID, API_KEY)
