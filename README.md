# Steganography Scripts (LSB)

Simple LSB steganography tools to **encode** a text message into an image and **decode** it back.

---

## Files

* `incode.py` — hide a text message in an image.
* `decode.py` — extract a hidden message from a stego image.

---

## Requirements

* Python 3.7+
* [Pillow](https://pillow.readthedocs.io/en/stable/) (Python imaging library)

---

## Install (one-time, on your machine)

```bash
python3 -m pip install --user Pillow
```

---

## Example

### 1. Encode a message into an image

```bash
python incode.py input.png "This is a secret message!" stego.png
```

* `input.png` → the original cover image
* `"This is a secret message!"` → the text to hide
* `stego.png` → the new image with the hidden message

### 2. Decode the message from the stego image

```bash
python decode.py stego.png
```

Output:

```
This is a secret message!
```

---

## Notes

* Works best with lossless formats like **PNG** (JPEG compression may corrupt hidden data).
* Keep input/output images reasonably sized for faster processing.
* Educational purpose only — not secure against advanced steganalysis.
