# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:31:28 2025

@author: admin.emo
"""

from youtube_transcript_api import YouTubeTranscriptApi

video_id = "bk626kJ9_OY"
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    for entry in transcript:
        print(f"{entry['start']}: {entry['text']}")
except Exception as e:
    print(f"Error: {e}")
