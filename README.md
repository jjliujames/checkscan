# Image Question Answering

This application uses a Vision-Language model to answer questions about images. It consists of a Vue.js frontend and a Python FastAPI backend.

## Project Structure

```
.
├── backend/           # Python FastAPI backend
│   ├── main.py       # Main FastAPI application
│   └── requirements.txt
└── frontend/         # Vue.js frontend
    └── check_submit/ # Vue project
```

## Setup and Running

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   python main.py
   ```

The backend will start on http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend/check_submit
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

The frontend will start on http://localhost:5173

## Usage

1. Open your browser and navigate to http://localhost:5173
2. Click the "Select Image" button to upload an image
3. Once the image is uploaded, you can type a question about the image in the input field
4. Click "Ask Question" to get an answer about the image

## Notes

- The application uses the ViLT (Vision-and-Language Transformer) model for question answering
- The model can answer questions about various aspects of the image
- For best results, use clear, well-lit images
- The model supports a wide range of questions about the content, objects, and context of the image 