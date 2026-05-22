# Lab 52 - Network File Transfers (wget/curl)

## Objectives
- Learn network file transfers
- Use wget and curl commands
- Download files and webpages
- Resume interrupted downloads

---

# Task 1 - Download Files with wget

## Download File

```bash
wget https://example.com/sample-file.txt
```

## Verify Download

```bash
ls
```

## Example Output

```text
sample-file.txt
```

---

# Task 2 - Fetch Webpage with curl

## Display Webpage Source

```bash
curl https://example.com
```

## Save Output to File

```bash
curl https://example.com -o webpage.html
```

## Open File

```bash
nano webpage.html
```

---

# Task 3 - Resume Downloads

## Start Download

```bash
wget https://example.com/large-sample-file.zip
```

Interrupt using:

```text
CTRL + C
```

## Resume Download

```bash
wget -c https://example.com/large-sample-file.zip
```

---

# Useful Commands

## wget Version

```bash
wget --version
```

## curl Version

```bash
curl --version
```

---

# Screenshots

## wget Download
```text
screenshots/01-wget-download.png
```

## curl Output
```text
screenshots/02-curl-output.png
```

## Saved Webpage File
```text
screenshots/03-webpage-file.png
```

## Resumed Download
```text
screenshots/04-resume-download.png
```

---

# Outcome
Successfully learned:
- Downloading files using wget
- Fetching webpages using curl
- Saving webpage source code
- Resuming interrupted downloads
- Basic network file transfer operations
