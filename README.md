# GitHub File Uploader 🚀

This Python script uses the GitHub REST API to upload files to a specified repository. It's useful for automating content updates or deploying assets from local storage.

## Features
- ✅ Upload any local file to a GitHub repo
- 🔐 Secure authentication using personal access tokens
- 🌿 Supports custom upload paths and branch selection

## How to Use
1. Replace placeholders in the script:
   - `TOKEN`: your GitHub personal access token
   - `USERNAME`: your GitHub username
   - `REPO`: name of the target repository
   - `FILEPATH`: local file path
   - `TARGET_PATH`: path inside GitHub repo

2. Run the script using:
bash
python upload_to_github.py

*Generate Token*
Go to [GitHub Tokens](https://github.com/settings/tokens) → Generate token with `repo` scope.

*Author*
Made with ❤ by [ShakirDev32](https://github.com/ShakirDev32)


---

### 🛡 How to Handle Errors in Code
Your script already checks response.status_code. You could expand that by:
- ✅ Printing the error message if the upload fails.
- ✅ Catching exceptions using try-except around your API call.
- ✅ Saving failed uploads to a log file for later review.
