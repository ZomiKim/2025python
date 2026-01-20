from dotenv import load_dotenv
import os 
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
import json

load_dotenv(override=True)
app = FastAPI(title="myapi")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class userRequest(BaseModel):
    content: str

@app.get("/")
def root():
    return {"message": "hi"}

@app.post("/generate")
def openai(req: userRequest):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "너는 JSON 생성기이다. "
                    "항상 JSON만 출력해야 한다. "
                    "텍스트 설명, 말머리, 마크다운, 코드블록 없이 출력한다."
                )
            },
            {
                "role": "user",
                "content": (
                    f"{req.content} 여행지 추천.\n"
                    "아래 JSON 배열 형식으로 5개 출력해야 한다.\n"
                    "형식:\n"
                    "[\n"
                    "  {\"name\":\"장소명\",\"type\":\"관광/자연/음식\",\"desc\":\"간단설명\",\"trans\":\"대중교통 팁\"},\n"
                    "  ... 5개\n"
                    "]"
                )
            }
        ]
    )

    try:
        parsed_output = json.loads(response.output_text)
        return {"message": parsed_output}
    except json.JSONDecodeError:
        return {"output": response.output_text, "error": "json decode error"}
