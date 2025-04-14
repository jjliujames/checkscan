from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import torch
from transformers import DonutProcessor, VisionEncoderDecoderModel

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load processor and model
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(device)
model.to(device)

@app.post("/ask")
async def ask_question(file: UploadFile = File(...), question: str = Form(...)):
    print(question)
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Prepare input
        pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

        # Construct prompt
        task_prompt = f"<s_docvqa><s_question>{question}</s_question><s_answer>"
        decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids.to(device)

        # Run model
        outputs = model.generate(pixel_values=pixel_values, decoder_input_ids=decoder_input_ids, max_length=512)
        result = processor.batch_decode(outputs, skip_special_tokens=True)[0]
        if "<s_answer>" in result:
            result = result.split("<s_answer>")[-1].strip()
        if "</s_answer>" in result:
            result = result.split("</s_answer>")[0].strip()
        result_final=result.replace(question,"")
        print(result_final)
        return {"answer": result_final}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
