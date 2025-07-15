from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from ocr import text_recognition
from AI_req import summarize, generate_Q, Q_explanation, classify_subject
import os
import shutil

app = FastAPI()

@app.post("/ocr")
async def ocr_endpoint(img: UploadFile = File(...)):
  try:
    save_dir = "img"
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, img.filename)

    with open(save_path, "wb") as buffer:
      shutil.copyfileobj(img.file, buffer)

    if not os.path.exists(save_path):
      print("이미지 파일 저장 실패")
      raise HTTPException(status_code=400, detail="이미지 파일 저장 실패")

    try:
      text = text_recognition(save_path)
      if text is None:
        print("이미지를 찾을 수 없음")
        raise HTTPException(status_code=404, detail="이미지를 찾을 수 없음")
    except Exception as e:
      print(f"이미지 파일을 인식할 수 없음. \nError:{e}")
      raise HTTPException(status_code=400, detail="이미지 파일을 인식할 수 없음")
    
    text_summary = summarize(text)

    question = generate_Q(text_summary)

    subject = classify_subject(question)

    explain = Q_explanation(question)

    return {'summary': text_summary, 'question': question, 'explanation': explain, 'subject': subject}
  
  except Exception as e:
    print("서버 에러, 예측 불가")
    raise HTTPException(status_code=500, detail=str(e))
  
# if __name__ == "__main__":
#   import uvicorn
#   uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)