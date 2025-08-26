# half bit AI

**Tagline:** Offline, Private, Lightweight AI Companion

---

## Project Overview
**half bit AI** is an innovative on-device personal AI companion designed to operate **fully offline** while preserving user privacy. The app intelligently learns from user interactions across multiple modalities—**text, audio, and images**—to build and maintain a dynamic, personalized knowledge base that delivers real-time assistance.

---

## Vision
To create a seamless, privacy-focused AI assistant that understands and adapts to individual user preferences and environments without requiring an internet connection. The system leverages lightweight AI models optimized for mobile devices, ensuring fast and efficient performance.

---

## Features
- Capture and process multimodal inputs: **text**, **images**, and **audio**.
- Utilize **Tesseract Lite** for on-device Optical Character Recognition (OCR).
- Employ **Vosk** for offline Speech-to-Text transcription.
- Integrate lightweight, quantized NLP models (**DistilBERT-mini**, **MiniLM**) for natural language understanding.
- Local storage solutions using **SQLite** and **Hive** for persistent, efficient data management.
- Responsive and intuitive Flutter-based UI with support for camera, audio recording, and notifications.

---

## Technology Stack
- **Frontend:** Flutter (Dart)
- **Storage:** SQLite, Hive, and path_provider for local files
- **AI Models:** On-device TFLite models including Tesseract Lite (OCR), Vosk (Speech-to-Text), DistilBERT-mini, and MiniLM (NLP)
- **Flutter Packages:** camera, flutter_sound, flutter_local_notifications, isolates
