import torch
from transformers import pipeline
import gradio as gr
from newspaper import Article

# Load the summarization pipeline
print("🌐 Using pre-trained model: facebook/bart-large-cnn")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device set to use {device}")

# 🔹 Function 1: Summarize typed text
def summarize_text(text):
    if len(text.strip()) == 0:
        return "❗ Please enter some text."
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    return summary

# 🔹 Function 2: Summarize from a file
def summarize_from_file(file):
    try:
        with open(file.name, "r", encoding="utf-8") as f:
            text = f.read()
        if len(text.strip()) == 0:
            return "❗ File is empty."
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return f"❌ Error reading file: {e}"

# 🔹 Function 3: Summarize from URL
def summarize_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        if len(text.strip()) == 0:
            return "❗ No text found at this URL."
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return f"❌ Error processing URL: {e}"

# 🧱 UI inside gr.Blocks context
with gr.Blocks() as demo:
    gr.Markdown("## ✂️ Text Summarizer with Hugging Face Transformers")

    # Section 1: Text Input
    gr.Markdown("### 🔹 Enter text manually")
    input_text = gr.Textbox(label="Input Text", lines=8, placeholder="Paste your content here...")
    summarize_btn = gr.Button("Summarize Text")
    output_text = gr.Textbox(label="Summary Output")

    # Section 2: File Upload
    gr.Markdown("### 📁 Upload a .txt File")
    file_input = gr.File(label="Upload .txt file")
    file_btn = gr.Button("Summarize File")
    file_output = gr.Textbox(label="Summary from File")

    # Section 3: URL Input
    gr.Markdown("### 🌐 Paste an Article URL")
    url_input = gr.Textbox(label="Website URL")
    url_btn = gr.Button("Summarize URL")
    url_output = gr.Textbox(label="Summary from URL")

    # 🧠 Button bindings
    summarize_btn.click(fn=summarize_text, inputs=input_text, outputs=output_text)
    file_btn.click(fn=summarize_from_file, inputs=file_input, outputs=file_output)
    url_btn.click(fn=summarize_from_url, inputs=url_input, outputs=url_output)

# 🚀 Launch app
demo.launch()
