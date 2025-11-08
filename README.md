# Intellecta - AI-Powered YouTube Learning Assistant

Intellecta is a Django web application, built for the Dev-Spark Hackathon, that enhances the video learning experience. It allows users to search for YouTube videos, view them, and interact with an AI-powered assistant that can summarize the video content and answer specific questions about it.

## Core Features

* **User Authentication:** A complete, custom-built user registration (`/signup`) and login (`/login`) system using the Django backend.

* **YouTube Video Search:** A search interface (`/`) that queries the YouTube v3 API to find videos relevant to a user's query.

* **AI-Generated Summaries:** When a video is selected, the application fetches its English transcript using `youtube-transcript-api`. This transcript is then sent to the Google Gemini API to generate a concise, easy-to-read summary.

* **Interactive AI Chatbot:** On the video player page, a chat-bot (powered by the Gemini API and JavaScript) is "primed" with the full video transcript, allowing users to ask specific questions about the video's content (e.g., "What did the speaker say about Python decorators?").

## Technology Stack

* **Backend:** Python, Django

* **Frontend:** HTML, CSS, JavaScript

* **Core Python Libraries:**

  * `Django`: For the web framework and user management.

  * `requests`: For making HTTP requests to external APIs.

  * `youtube-transcript-api`: For fetching video transcripts.

* **External APIs:**

  * **Google YouTube Data API v3:** Used in `core/apis.py` to search for videos.

  * **Google Generative AI (Gemini) API:**

    * Used in `core/apis.py` (server-side) to generate the initial video summary.

    * Used in `templates/video_player.html` (client-side) to power the interactive chatbot.
   
