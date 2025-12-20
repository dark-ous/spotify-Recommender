# 🎧 Spotify Song Similarity Engine

A **content-based song recommender** that finds similar tracks based on their **audio features** such as `acousticness`, `danceability`, `energy`, `loudness`, `speechiness`, and more.  
This project uses **cosine similarity** to measure how close songs are in feature space — **no machine learning model is trained**.

---

## 🧩 Overview

This project analyzes pre-existing audio features from the [`SpotifyFeatures.csv`](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db) dataset (or your own extracted dataset) and recommends songs that are most similar to a given query track.

It’s simple, fast, and fully interpretable — powered by **feature scaling** and **vector similarity**.
## NOTE : This was a weekend project, so I didn’t add major error handling or extensive optimizations.The goal was to explore how audio features and cosine similarity can be used for simple song recommendation without machine learning.
---

## ⚙️ How It Works

1. The dataset (`SpotifyFeatures.csv`) is loaded into a pandas DataFrame.  
2. Selected features (like energy, danceability, valence, etc.) are standardized using `StandardScaler`.  
3. For a chosen song (the **query track**), its feature vector is compared with every other song using **cosine similarity**.  
4. The top 10 most similar songs are returned — excluding the query itself.  

No ML model training is done; it’s a **mathematical similarity engine**.

---

## 🧠 Feature Extractor (optional)

If you don’t already have precomputed features, use `featureExtractor.py` to generate them from your own audio files.  
This script extracts useful musical features using **Librosa**, allowing you to build your own dataset.

### 🧾 Features Extracted
| Feature | Description |
|----------|-------------|
| `rms` | Loudness (root-mean-square energy) |
| `centroid` | Spectral centroid (brightness) |
| `flatness` | Spectral flatness (noisiness) |
| `tempo` | Tempo / rhythm estimation |
| `mfcc` | MFCC delta (timbre variation) |
| `zcr` | Zero-crossing rate (roughness) |
| `bandwidth` | Spectral bandwidth (range of frequencies) |
| `rolloff` | Spectral rolloff (where energy drops off) |

### 💽 Output
All features are saved into an Excel file (`audio_features.xlsx`), ready for use in your recommender.

---

## 🗂️ Folder Structure
```
Spotify-Recommender/
├── data # Dataset (Kaggle or your own)
│ ├──SpotifyFeatures.csv
├── main.py # Main similarity engine
├── featureExtractor.py # Audio feature extraction script
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
## Installation
```
pip install -r requirements.txt
python main.py 
```
