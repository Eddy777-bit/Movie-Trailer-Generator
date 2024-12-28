from moviepy.editor import VideoFileClip, concatenate_videoclips

# Define the key scenes based on time stamps
def generate_trailer(scene_clips):
    clips = []
    for scene in scene_clips:
        clip = VideoFileClip(scene["path"]).subclip(scene["start"], scene["end"])
        clips.append(clip)
    
    # Concatenate selected clips
    trailer = concatenate_videoclips(clips)
    trailer.write_videofile("automated_trailer.mp4", codec="libx264")
    print("Trailer generated successfully!")

# Example input data for scenes
scene_data = [
    {"path": "scene1.mp4", "start": 0, "end": 10},
    {"path": "scene2.mp4", "start": 5, "end": 15},
    {"path": "scene3.mp4", "start": 2, "end": 12},
]

generate_trailer(scene_data)
