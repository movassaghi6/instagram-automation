# RegEx Patterns for some of Header keys that can be found in the instagram's HTML
header_patterns = {
    "X_BLOKS_VERSION_ID": r'"versioningID"\s*:\s*"([^"]+)"',
    "X_FB_LSD": r',\["LSD",\s*\[\],\s*\{"token":"([^"]+)"\}',
    "X_IG_App_ID": r'"APP_ID"\s*:\s*"([^"]+)"',
}


# RegEx Patterns for some of Data keys that can be found in the instagram's HTML
data_patterns = {
        "av": r'actorID"\s*:\s*"(\d{17})"',
        "spin_t": r'"__spin_t"\s*[:=]\s*(\d+)',
        "jazoest": r'jazoest\s*=\s*(\d+)',
        "spin_b": r'"__spin_b"\s*:\s*"([^"]+)"',
        "spin_r": r'"__spin_r"\s*:\s*(\d+)',
        "hsi": r'"hsi"\s*[:=]\s*"(\d+)"',
        "hs": r'"haste_session"\s*[:=]\s*"([^"]+)"',
        "rev": r'"client_revision"\s*[:=]\s*(\d+)',
        "lsd": r',\["LSD",\s*\[\],\s*\{"token":"([^"]+)"\}',
        "fb_dtsg": r'"f":"([a-zA-Z0-9\-:]+)"',
        "comet_req": r'__comet_req\s*=\s*(\d+)',
        "a": r'__a\s*=\s*(\d+)',
        "user": r'__user\s*=\s*(\d+)'
    }

