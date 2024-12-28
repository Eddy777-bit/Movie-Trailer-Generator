import ffmpeg

# Automate trimming for specific scenes
def trim_scene(input_file, start_time, duration, output_file):
    ffmpeg.input(input_file, ss=start_time, t=duration).output(output_file).run()
    print(f"Trimmed scene saved as {output_file}")

# Example usage
trim_scene("movie.mp4", start_time=60, duration=15, output_file="trimmed_scene1.mp4")
trim_scene("movie.mp4", start_time=120, duration=20, output_file="trimmed_scene2.mp4")
