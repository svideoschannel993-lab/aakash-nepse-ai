import random

def analyze_stock(stock):

    fundamental = random.randint(40, 95)
    technical = random.randint(40, 95)
    smart_money = random.randint(40, 95)
    macro = random.randint(50, 90)
    sentiment = random.randint(30, 95)

    final_score = (fundamental + technical + smart_money + macro + sentiment) / 5

    if final_score > 75:
        verdict = "STRONG BUY"
    elif final_score > 60:
        verdict = "BUY"
    elif final_score > 45:
        verdict = "HOLD"
    else:
        verdict = "AVOID"

    return {
        "stock": stock,
        "fundamental": fundamental,
        "technical": technical,
        "smart_money": smart_money,
        "macro": macro,
        "sentiment": sentiment,
        "final_score": round(final_score, 2),
        "verdict": verdict,

        "predictions": {
            "1_day": "Neutral",
            "7_day": "Slight Bullish Bias",
            "30_day": "Trend Dependent"
        }
    }
