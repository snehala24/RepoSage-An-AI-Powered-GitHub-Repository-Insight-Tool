def get_api_key():
    import os
    return os.getenv("GOOGLE_API_KEY") or "AIzaSyAmsW-DHtZlCPvzdAOVdbSlf879N3rHbdU"
