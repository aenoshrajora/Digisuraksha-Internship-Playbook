import unicodedata
import re
from urllib.parse import urlparse
from homoglyphs import Homoglyphs
from difflib import SequenceMatcher

homoglyphs = Homoglyphs()

# Normalize Unicode
def normalize_unicode(domain):
    return unicodedata.normalize('NFKC', domain)

# Decode punycode (IDN)
def decode_punycode(domain):
    try:
        return domain.encode("ascii").decode("idna")
    except Exception:
        return domain

# Use string similarity to filter benign diffs
def is_minor_change(original, ascii_version, threshold=0.97):
    ratio = SequenceMatcher(None, original, ascii_version).ratio()
    return ratio >= threshold

# Check for homoglyphs
# def contains_homoglyphs(domain):
#     ascii_version = homoglyphs.to_ascii(domain)

#     # Skip if both are ASCII-only
#     if all(ord(c) < 128 for c in domain + ascii_version):
#         return False

#     # Skip if similarity is too high (likely benign)
#     if is_minor_change(domain, ascii_version):
#         return False

#     if ascii_version != domain:
#         print(f"[DEBUG] Homoglyph diff: {domain} → {ascii_version}")
#         return True

#     return False

def contains_homoglyphs(domain):
    ascii_version_list = homoglyphs.to_ascii(domain)
    ascii_version = ''.join(ascii_version_list)

    # Skip if both are ASCII-only
    if all(ord(c) < 128 for c in domain + ascii_version):
        return False

    # Skip if similarity is too high (likely benign)
    if is_minor_change(domain, ascii_version):
        return False

    if ascii_version != domain:
        print(f"[DEBUG] Homoglyph diff: {domain} → {ascii_version}")
        return True

    return False

# Check for mixed Unicode scripts
def contains_mixed_scripts(domain):
    scripts = set()
    for char in domain:
        if char.isascii():
            continue
        try:
            name = unicodedata.name(char)
            if "LATIN" in name:
                scripts.add("Latin")
            elif "CYRILLIC" in name:
                scripts.add("Cyrillic")
            elif "GREEK" in name:
                scripts.add("Greek")
            elif "ARMENIAN" in name:
                scripts.add("Armenian")
            elif "HEBREW" in name:
                scripts.add("Hebrew")
        except ValueError:
            continue
    return len(scripts) > 1

# Extract clean domain
def extract_domain(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path
    domain = domain.lower()
    domain = re.sub(r"^www\.", "", domain)
    return domain

# Analyze and flag
def is_suspicious(domain):
    raw = domain
    decoded = decode_punycode(raw)
    normalized = normalize_unicode(decoded)

    suspicious_reasons = []

    if raw.startswith("xn--"):
        suspicious_reasons.append("Punycode-encoded (IDN domain)")
    if contains_homoglyphs(normalized):
        suspicious_reasons.append("Contains homoglyphs")
    if contains_mixed_scripts(normalized):
        suspicious_reasons.append("Mixed Unicode scripts (e.g., Cyrillic + Latin)")

    if suspicious_reasons:
        print(f"\n⚠️  Suspicious domain detected: {raw}")
        print(f"↪ Decoded / Normalized: {normalized}")
        for reason in suspicious_reasons:
            print(f"🔎 Reason: {reason}")
        return True
    return False

def main():
    print("🔍 Homoglyph Domain Scanner (Improved)")
    print("Paste domain(s) or URL(s) to scan. Comma or space separated.")
    print("Type 'exit' or 'q' to quit.\n")

    while True:
        user_input = input("💬 Enter domain(s): ").strip()
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("👋 Exiting. Stay safe!")
            break

        inputs = re.split(r'[,\n\s]+', user_input)

        for item in inputs:
            if not item:
                continue
            domain = extract_domain(item)
            is_suspicious(domain)

if __name__ == "__main__":
    main()
