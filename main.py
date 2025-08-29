from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from typing import List, Dict

app = FastAPI(
    title="BFHL API",
    description="Bajaj Finserv API",
    version="4.0.0"
)

class Payload(BaseModel):
    entries: List[str]

class ResponseSchema(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_nums: List[str]
    even_nums: List[str]
    letters: List[str]
    symbols: List[str]
    total: str
    fancy_text: str


def classify_entries(values: List[str]) -> Dict:
    odd_group, even_group, alpha_group, symbol_group = [], [], [], []
    total_sum = 0

    for token in values:
        # Numbers
        try:
            number = int(token)
            total_sum += number
            if number % 2 == 0:
                even_group.append(token)
            else:
                odd_group.append(token)
            continue
        except ValueError:
            pass

        # Alphabets vs specials
        if token.isalpha():
            alpha_group.append(token.upper())
        else:
            symbol_group.append(token)

    reversed_letters = list("".join(alpha_group))[::-1]

    styled_string = "".join(
        ch.lower() if i % 2 == 0 else ch.upper()
        for i, ch in enumerate(reversed_letters)
    )

    return {
        "is_success": True,
        "user_id": "hrishikesh_arun_13052005",
        "email": "hrishikeshvirupakshi@gmail.com",
        "roll_number": "22BCE1817",
        "odd_nums": odd_group,
        "even_nums": even_group,
        "letters": alpha_group,
        "symbols": symbol_group,
        "total": str(total_sum),
        "fancy_text": styled_string
    }


@app.post("/bfhl", response_model=ResponseSchema)
async def analyze_payload(input_data: Payload):
    if not input_data.entries:
        raise HTTPException(status_code=400, detail="No entries provided")
    return ResponseSchema(**classify_entries(input_data.entries))


@app.get("/bfhl")
async def operation_identifier():
    return {"operation_code": 1}


@app.get("/")
async def api_overview():
    return {
        "message": "BFHL API is active",
        "routes": {
            "POST /bfhl": "Analyze input entries",
            "GET /bfhl": "Return operation identifier"
        }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
