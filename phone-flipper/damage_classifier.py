def classify(title):

    title = title.lower()

    if "画面" in title or "液晶" in title:
        return "screen"

    if "バッテリー" in title:
        return "battery"

    if "カメラガラス" in title:
        return "camera_glass"

    if "カメラ" in title:
        return "camera"

    return None