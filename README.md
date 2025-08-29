# Bajaj Finserv Health Limited | Qualifier 1
This is a simple Python-based API built for the **BFHL Qualifier Round 1**.  
It is designed to process JSON input and return a structured response based on the provided data.

## 📋 Features
- Accepts POST requests with JSON data
- Validates and processes the input
- Returns a structured JSON response
- Lightweight and easy to deploy

---
Separated odd/even numbers
Alphabetic characters (uppercase)
Special characters
Sum of numbers
Concatenated alphabets in reverse order with alternating caps
User information and success status

## 🚀Approach
Tech Stack: FastAPI + Python + Vercel

🛠 Setup & Run
# Create virtual environment (Python 3.11/3.12)
- python -m venv venv
- .\venv\Scripts\Activate


# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
API runs at: http://localhost:8000

🧪 Testing
Method 1: Using cURL
# Test Example A
curl -X POST "http://localhost:8000/bfhl" \
     -H "Content-Type: application/json" \
     -d '{"data": ["a","1","334","4","R","$"]}'

# Response

{
  "is_success": true,
  "user_id": "srinath_kamalakumar",
  "email": "srinath@example.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
--
## 🌐 Deployment
Deployed on Vercel: "https://bfhlqualifier1-qq9ypkzsc-srinath-kamalakumars-projects-de37d6ba.vercel.app/bfhl"
--

# Test deployed API
curl -X POST "https://bfhlqualifier1-qq9ypkzsc-srinath-kamalakumars-projects-de37d6ba.vercel.app/bfhl" \
     -H "Content-Type: application/json" \
     -d '{"data": ["2","a","y","4","&","-","*","5","92","b"]}'

--

## 📁 Files
- main.py - FastAPI application with core logic
- requirements.txt - Python dependencies
- vercel.json - Deployment configuration
- test_api.py - Automated test script
- 
## ⚙️ Implementation Details
- Numbers returned as strings (as per requirements)
- Error handling for invalid inputs
- Mixed string handling (e.g., "ABcD" treated as alphabets)
- Concatenation logic with alternating caps in reverse order
