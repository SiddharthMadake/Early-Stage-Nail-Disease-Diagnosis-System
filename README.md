# Nail Disease Detection System

An AI-powered web application for detecting nail diseases using deep learning models (VGG16, ResNet50, InceptionV3, Xception).

## Features

-  Detects 17 different types of nail diseases
-  Uses transfer learning with VGG16 architecture
-  Modern, responsive web interface
-  Confidence score for predictions

## Detected Diseases

1. Darier's disease
2. Muehrcke's lines
3. Alopecia areata
4. Beau's lines
5. Bluish nail
6. Clubbing
7. Eczema
8. Half and half nails (Lindsay's nails)
9. Koilonychia
10. Leukonychia
11. Onycholysis
12. Pale nail
13. Red lunula
14. Splinter hemorrhage
15. Terry's nail
16. White nail
17. Yellow nails

## Project Structure

```
nail-disease-detection/
├── templates/
│   ├── index.html          # Home page with hero section
│   ├── about.html          # About page
│   ├── nailhome.html       # Nail prediction info page
│   └── nailpred.html       # Upload and prediction page
├── static/
│   └── style.css           # Enhanced CSS styling
├── uploads/                # Temporary upload folder (auto-created)
├── main.py                 # Flask application
├── requirements.txt        # Python dependencies
├── vgg-16-nail-disease.h5  # Trained model (add this)
└── README.md              # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
## 📥 Model & Dataset
Download model: https://drive.google.com/file/d/1Vs7AgzN4mJfBYfLYhNXF7AAROq9SPCz1/view?usp=sharing
Download dataset: https://drive.google.com/drive/folders/1vQlPB_a31Ad4wLNQDnJLmK8DagXBcHeG?usp=sharing

### Steps

1. **Clone or download this project**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add your trained model**
   - Place your `vgg-16-nail-disease.h5` model file in the project root directory

4. **Create folder structure**
```bash
mkdir templates static uploads
```

5. **Move files to correct locations**
   - Move all `.html` files to `templates/` folder
   - Move `style.css` to `static/` folder

## Running the Application

1. **Start the Flask server**
```bash
python main.py
```

2. **Access the application**
   - Open your web browser
   - Navigate to: `http://localhost:8080`

3. **Using the application**
   - Click "Explore" or navigate to "NAIL" section
   - Click "Predict" button
   - Upload a nail image (JPG, PNG, JPEG)
   - View the prediction result with confidence score

## Key Improvements

### Backend (main.py)
✅ Fixed preprocessing to use VGG16 instead of InceptionV3
✅ Added comprehensive error handling
✅ Added confidence score to predictions
✅ Better file handling and cleanup
✅ Formatted disease names for better readability

### Frontend
✅ Modern, responsive design with Poppins & Playfair Display fonts
✅ Professional medical color scheme (teal/green)
✅ Hero section with gradient background
✅ Model cards with hover effects
✅ Enhanced footer with newsletter and social links
✅ Drag-and-drop file upload
✅ Image preview before prediction
✅ Smooth animations and transitions
✅ Mobile-responsive layout

## Technologies Used

- **Backend**: Flask, TensorFlow/Keras
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Models**: VGG16, ResNet50, InceptionV3, Xception
- **Icons**: Font Awesome 6.0
- **Fonts**: Google Fonts (Poppins, Playfair Display)

## Configuration

### Changing Port
Edit `main.py`, line at the bottom:
```python
app.run(debug=True, port=8080, host='0.0.0.0')
```

### Using Different Model
1. Replace the model file
2. Update the filename in `main.py`:
```python
model = load_model("your-model-name.h5")
```

### Updating Disease Classes
Edit the `DISEASE_CLASSES` list in `main.py` to match your model's output classes.

## Troubleshooting

### Model not loading
- Ensure `vgg-16-nail-disease.h5` is in the project root
- Check TensorFlow version compatibility
- Verify model file is not corrupted

### CSS not loading
- Ensure `style.css` is in `static/` folder
- Clear browser cache (Ctrl+F5)

### Upload errors
- Check `uploads/` folder exists
- Verify file permissions
- Ensure file is a valid image format

## Future Enhancements

- [ ] Add more detailed disease information
- [ ] Implement user authentication
- [ ] Store prediction history
- [ ] Add batch prediction capability
- [ ] Deploy to cloud platform (Heroku, AWS, etc.)
- [ ] Add API endpoints for mobile apps
- [ ] Implement real-time camera capture

## License

This project is for educational purposes.

## Contact

For questions or support, refer to the contact information in the footer of the website.

---

**Note**: This is a diagnostic assistance tool and should not replace professional medical advice. Always consult with healthcare professionals for proper diagnosis and treatment.
