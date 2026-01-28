# Reference: YouTube Transcript Grabber

## CLI Arguments (`grab_transcript.py`)

| Argument | Long Flag | Description | Default |
| :--- | :--- | :--- | :--- |
| `video_id` | N/A | [MANDATORY] The 11-character YouTube video ID. | N/A |
| `-o` | `--output` | [Optional] Path to save the transcript text file. | stdout |
| `-t` | `--timestamps` | [Optional] Include `[MM:SS]` timestamps at paragraph starts. | False |

## API Interaction (`youtube-transcript-api`)

The script uses the `YouTubeTranscriptApi` class. It specifically tries to fetch English (`en`, `en-US`, `en-GB`) before falling back to the first available transcript (which may be auto-generated).

### Object Model
The `fetch()` method returns a list of `FetchedTranscriptSnippet` objects:
- `text`: The textual content of the snippet.
- `start`: The start time in seconds (float).
- `duration`: The duration of the snippet in seconds (float).

## Error Codes

| Code | Label | Meaning |
| :--- | :--- | :--- |
| `1` | `TranscriptsDisabled` | The video owner has turned off subtitles for this video. |
| `1` | `NoTranscriptFound` | No transcript exists in the requested or default languages. |
| `1` | `Exception` | Network error, invalid Video ID, or API change. |

## Troubleshooting
- **Invalid ID**: Ensure you are not passing the full URL. Only the ID (e.g., `7vJxJyTWBmc`) is valid.
- **Connection Errors**: This API scrapes the web client and may be blocked by YouTube if used excessively. Use the `browser_subagent` as a manual fallback if this happens.
