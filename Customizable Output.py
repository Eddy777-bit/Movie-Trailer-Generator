import streamlit as st
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Interactive trailer customization
st.title("Movie Trailer Generator")
duration = st.slider("Select Trailer Duration (seconds)", 30, 120)
tone = st.selectbox("Select Trailer Tone", ["Action-packed", "Romantic", "Thriller"])

# Based on user selection, pick scenes
if tone == "Action-packed":
    scene_files = ["action1.mp4", "action2.mp4"]
elif tone == "Romantic":
    scene_files = ["romantic1.mp4", "romantic2.mp4"]
else:
    scene_files = ["thriller1.mp4", "thriller2.mp4"]

scenes = [VideoFileClip(scene).subclip(0, duration // len(scene_files)) for scene in scene_files]
custom_trailer = concatenate_videoclips(scenes)
custom_trailer.write_videofile("custom_trailer.mp4")
st.write("Trailer generated successfully!")
