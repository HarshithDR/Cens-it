# Cens-it  
An AI-driven web application for censoring sensitive or inappropriate content in video and audio files, designed to ensure compliance with content guidelines and provide a reliable platform for content moderation across industries.

---

## Overview  
Cens-it is a powerful content moderation tool that leverages machine learning and deep learning techniques to automatically detect and censor inappropriate content in multimedia files. It is capable of processing video and audio files to identify 18+ content, such as nudity, violence, or explicit language, and applying censorship through blackouts, muting, or other techniques. This project was built with a fully functional data pipeline, custom-trained Convolutional Neural Networks (CNNs), and advanced audio filtering methods.

---

## Features  
- **Video Content Censorship:**  
   - Detects and blacks out adult content, including nudity and violent scenes.  
   - Utilizes a custom-trained CNN for high-accuracy content detection.  

- **Audio Content Censorship:**  
   - Filters out explicit language or inappropriate sounds using advanced signal processing techniques.  
   - Mutes or replaces sensitive audio segments to ensure compliance.  

- **End-to-End Data Pipeline:**  
   - Handles data collection, cleaning, filtering, and preprocessing for model training.  
   - Designed from scratch to support varying types of multimedia content.  

- **Automation:**  
   - Automates the censorship process seamlessly for large-scale multimedia processing.  

---

## Technologies Used  

### Backend Technologies  
- **Deep Learning:**  
   - TensorFlow/Keras – Custom-designed Convolutional Neural Network (CNN) for video filtering.  

- **Audio Processing:**  
   - Python signal processing libraries such as `librosa` for audio analysis and filtering.  

### Data Pipeline  
- Custom data collection and preprocessing pipeline designed to fetch relevant visual and audio datasets.  
- Data filtering and augmentation techniques to improve model performance.  

### Web Application Framework  
- Flask/Django (Specify which one is used).  
- REST APIs for uploading media and fetching results.  

### Frontend  
- HTML, CSS, JavaScript for a simple and interactive user interface.  
- Integration with backend APIs for seamless media uploads and results display.  

### Database  
- MongoDB or SQL (Specify which database is used) for logging results and maintaining content metadata.  

---


## Installation

1. Clone the Repository:

```bash
  git clone https://github.com/HarshithDR/Cens-it.git
cd Cens-it
```

2. Install Dependencies:

```bash
  pip install -r requirements.txt
```

3. **Setup the Data Pipeline (Optional):**  
- Use the provided scripts in the `data_pipeline/` folder to collect training data.  
- Run the preprocessing script to filter and clean the data:  
  ```
  python preprocess_data.py
  ```

4. **Train the CNN Model (Optional):**  
- If required, you can retrain the model using the training script:  
  ```
  python train_video_model.py
  ```

5. **Run the Web Application:**  
Start the server by running:  
  ```
  python app.py
  ```
6. **Access the Web Interface:**  
Open your browser and navigate to:
  ```
  http://localhost:5000
  ```
  
---

## Usage Guide  

1. **Upload Media:**  
- Use the file uploader on the application interface to upload video or audio files.  

2. **Censorship Process:**  
- The backend processes the files to detect inappropriate sections using the pretrained CNN for videos and audio filtering methods for audio files.  
- Blackout (for visuals) or muting (for audio) is applied to the detected sections.  

3. **Results:**  
- View or download the censored version of the media file directly from the interface.  

---

## Architecture  

1. **Frontend:**  
- Provides an easy-to-use file uploader and displays results to the user.  

2. **Backend:**  
- Accepts uploaded files and processes them to detect sensitive content.  
- Handles video and audio filtering using pretrained AI models.  

3. **Censorship Models:**  
- A custom-trained CNN for video content detection.  
- Audio filtering models to identify and censor inappropriate language or sounds.  

4. **Output:**  
- Generates and serves a censored version of the uploaded media file.  

---

## Project Contributions  

**Key Contributions:**  
- **Video Filtering:** Developed and trained a CNN from scratch to detect nudity and violent scenes.  
- **Audio Filtering:** Designed efficient audio processing techniques to identify explicit language.  
- **Data Collection:** Built a comprehensive pipeline for collecting, cleaning, and filtering datasets.  
- **Optimization:** Fine-tuned the models for high accuracy and efficiency in censorship processing.  

---

## Future Scope  
- **Scalability:** Extend the platform to handle live streaming content.  
- **Multilingual Audio Filtering:** Improve audio filtering to detect explicit content in multiple languages.  
- **Advanced Detection Models:** Integrate transformer-based models for better accuracy in video filtering.  
- **Custom Filters:** Allow users to define their own censorship criteria.  

---

## Contributors  
- [Harshith Deshalli Ravi](https://github.com/HarshithDR)
- [Amith Ramaswamy](https://github.com/amith-2001)

---

## License  
This project is licensed under the MIT License. See the `LICENSE` file for more details.  

---
