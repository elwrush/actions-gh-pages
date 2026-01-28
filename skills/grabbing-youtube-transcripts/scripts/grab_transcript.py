
import argparse
import sys
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def get_transcript(video_id, output_file=None, include_timestamps=False):
    try:
        ytt_api = YouTubeTranscriptApi()
        
        try:
            fetched_transcript = ytt_api.fetch(video_id, languages=['en', 'en-US', 'en-GB'])
        except Exception:
            fetched_transcript = ytt_api.fetch(video_id)
        
        full_text = []
        for snippet in fetched_transcript:
            if include_timestamps:
                start = snippet.start
                minutes = int(start // 60)
                seconds = int(start % 60)
                timestamp = f"[{minutes:02d}:{seconds:02d}] "
                full_text.append(f"{timestamp}{snippet.text}")
            else:
                full_text.append(snippet.text)
        
        separator = "\n" if include_timestamps else " "
        formatted_text = separator.join(full_text)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(formatted_text)
            print(f"Transcript saved to {output_file}")
        else:
            print(formatted_text)
            
    except TranscriptsDisabled:
        print(f"Error: Transcripts are disabled for video {video_id}", file=sys.stderr)
        sys.exit(1)
    except NoTranscriptFound:
        print(f"Error: No transcript found for video {video_id}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube Transcript")
    parser.add_argument("video_id", help="The YouTube Video ID (e.g., 7vJxJyTWBmc)")
    parser.add_argument("--output", "-o", help="Output text file path")
    parser.add_argument("--timestamps", "-t", action="store_true", help="Include timestamps in the output")
    
    args = parser.parse_args()
    
    get_transcript(args.video_id, args.output, args.timestamps)
