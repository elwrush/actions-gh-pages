import os
import subprocess
import glob

AUDIO_DIR = r"c:\PROJECTS\LESSONS AND SLIDESHOWS 2\18-01-26_Fight-or-Flight\audio"

def convert_to_mp3():
    # Find all wav files
    wav_files = glob.glob(os.path.join(AUDIO_DIR, "*.wav"))
    
    if not wav_files:
        print("No WAV files found to convert.")
        return

    print(f"Found {len(wav_files)} WAV files. Starting conversion...")

    for wav_file in wav_files:
        base_name = os.path.splitext(wav_file)[0]
        mp3_file = base_name + ".mp3"
        
        # FFmpeg command
        # -y : overwrite output
        # -i : input
        # -codec:a libmp3lame : use mp3 encoder
        # -qscale:a 2 : high quality variable bitrate (approx 190kbps average)
        cmd = [
            "ffmpeg", "-y",
            "-i", wav_file,
            "-codec:a", "libmp3lame",
            "-qscale:a", "2",
            mp3_file
        ]
        
        try:
            print(f"Converting {os.path.basename(wav_file)}...")
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Verify MP3 exists and is valid size
            if os.path.exists(mp3_file) and os.path.getsize(mp3_file) > 0:
                os.remove(wav_file)
                print(f"✅ Converted and deleted source: {os.path.basename(mp3_file)}")
            else:
                print(f"❌ Failed to create valid MP3 for {os.path.basename(wav_file)}")
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Error converting {os.path.basename(wav_file)}: {e}")
        except FileNotFoundError:
             print("❌ FFmpeg not found. Please verify it is installed and in PATH.")
             break

if __name__ == "__main__":
    convert_to_mp3()
