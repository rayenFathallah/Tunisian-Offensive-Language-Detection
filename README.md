# Tunisian Offensive Language Detection

This project aims to address the challenges of detecting offensive language in the Tunisian dialect, a task complicated by multilingual code-switching and informal online communication styles. By leveraging advanced Natural Language Processing (NLP) models, the system detects hate speech and abusive language in real-time, providing insights into the dynamics of content moderation for under-resourced languages.

## Features
- **Multilingual Support:** Handles code-switching between Tunisian Arabic, French, and Classical Arabic.
- **Real-Time Processing:** Implements a real-time classification pipeline using a Streamlit application.
- **Advanced NLP Models:** Includes TunBERT, Tunibert, and Sequence-to-Sequence models for transliteration and classification.
- **Custom Datasets:** Combines scraped data, T-HSAB, and transliteration datasets for comprehensive training.

## Requirements
- Python 3.8+
- Libraries: TensorFlow, PyTorch, Streamlit, `facebook-scraper`, and others listed in `requirements.txt`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/Tunisian-Offensive-Language-Detection.git
   cd Tunisian-Offensive-Language-Detection
2. Run the streamlit app :
   ```bash
     streamlit run streamlit.py
