import random

def analyze_stock(stock):
    fundamental = random.randint(40, 95)
    technical = random.randint(40, 95)
    smart_money = random.randint(40, 95)
    macro = random.randint(50, 90)
    sentiment = random.randint(30, 95)

    final_score = (fundamental + technical + smart_money + macro + sentiment) / 5

    verdict = "BUY" if final_score > 70 else "HOLD" if final_score > 50 else "AVOID"

    return {
        "stock": stock,
        "fundamental": fundamental,
        "technical": technical,
        "smart_money": smart_money,
        "macro": macro,
        "sentiment": sentiment,
        "final_score": final_score,
        "verdict": verdict,
        "predictions": {
            "1_day": "Neutral",
            "7_day": "Bullish",
            "30_day": "Strong Bullish"
        }
    }
