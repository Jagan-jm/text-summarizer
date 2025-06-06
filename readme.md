# 📝 AI Text Summarizer (SummaryGenie)

An AI-powered text summarization tool that generates concise summaries from long documents or transcripts. Built using Hugging Face's BART model and Gradio for the user interface.

## 🚀 Features
- Summarize content from:
  - 🧾 PDF files
  - 📋 Pasted text
- Download summary as `.txt` or `.pdf`
- Copy summary to clipboard
- Language auto-detection
- Clean and interactive GUI

## 🧠 Model Used
- 🤗 `facebook/bart-large-cnn` from Hugging Face Transformers

## 🛠️ Tech Stack
- Python
- Hugging Face Transformers
- PyMuPDF (`fitz`) for PDF parsing
- `langdetect` for language detection
- Gradio for frontend UI

## 📦 Installation
```bash
git clone https://github.com/jagan-jm/text-summarizer.git
cd text-summarizer
pip install -r requirements.txt
