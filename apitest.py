import requests
import json

scenarios = [
    {
        "label": "Sample 1",
        "input_values": ["x", "7", "12", "Q", "#", "99"],
        "expected_odds": ["7", "99"],
        "expected_evens": ["12"],
        "expected_letters": ["X", "Q"],
        "expected_symbols": ["#"],
        "expected_total": "118"
    },
    {
        "label": "Sample 2",
        "input_values": ["M", "42", "88", "13", "n", "@", "%", "0"],
        "expected_odds": ["13"],
        "expected_evens": ["42", "88", "0"],
        "expected_letters": ["M", "N"],
        "expected_symbols": ["@", "%"],
        "expected_total": "143"
    },
    {
        "label": "Sample 3",
        "input_values": ["hello", "WORLD", "25", "50", "&"],
        "expected_odds": ["25"],
        "expected_evens": ["50"],
        "expected_letters": ["HELLO", "WORLD"],
        "expected_symbols": ["&"],
        "expected_total": "75"
    }
]

def run_checks(api_root="http://localhost:8000"):
    """Run scenarios against the API"""
    for case in scenarios:
        print(f"\n=== Running {case['label']} ===")

        request_body = {"data": case["input_values"]}
        try:
            resp = requests.post(f"{api_root}/bfhl", json=request_body)

            if resp.ok:
                output = resp.json()
                print(f"✔ Status: {resp.status_code}")
                print("Sent:", request_body)
                print("Received:", json.dumps(output, indent=2))

                print("Odd →", output.get("odd_numbers"), "Expected:", case["expected_odds"])
                print("Even →", output.get("even_numbers"), "Expected:", case["expected_evens"])
                print("Letters →", output.get("alphabets"), "Expected:", case["expected_letters"])
                print("Symbols →", output.get("special_characters"), "Expected:", case["expected_symbols"])
                print("Total →", output.get("sum"), "Expected:", case["expected_total"])

            else:
                print(f"✘ API returned {resp.status_code}")
                print("Body:", resp.text)

        except requests.exceptions.RequestException as err:
            print("✘ Failed to contact API:", err)

if __name__ == "__main__":
    print("Launching local API tests...")
    run_checks("http://localhost:8000")
