# Advanced Soccer Game Analytics

## Overview
Inspired by Sports Analytics Projects whic sense players and ball movements, such as the work by _____ on X. Seeks to improve on this, with formation sension, xG probability every attack, heat maps/momentmu, etc.

## Pipeline
The pipeline that this project uses, will be using the RF-DETR model for player detection, with using Gemini VLM for tactical formation reasoning and statistical calculations.

Metrics: 82.1% mAP@50, 86.9% precision, 78.6% recall, 82.5% F1



## Dataset
Roboflow: https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc

## Model
- Architecture: RF-DETR (Small)
- Training: Roboflow-hosted (Cloud Custom Traning)

## Setup
Commit 1: Model trained and deployed on Roboflow, Roboflow and Gemini API Keys generated. 
          Next: Build workflow pipeline.  

## Usage

## Credits / Acknowledgements