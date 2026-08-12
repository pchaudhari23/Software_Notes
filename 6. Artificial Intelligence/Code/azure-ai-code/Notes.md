
# Azure AI SDK — Developer Reference (2026)

> Quick reference for Azure AI SDK modules, clients, and methods used in modern Azure AI applications.

---

# Table of Contents

1. Authentication
2. Azure AI Language
3. Azure Translator
4. Azure AI Vision
5. Azure AI Face
6. Azure AI Document Intelligence
7. Azure AI Speech
8. Generative AI — Azure OpenAI
9. Full Import Reference

---

# 1. Authentication

Most Azure AI SDKs support either API keys or Microsoft Entra ID authentication.

## API Key Authentication

```python
from azure.core.credentials import AzureKeyCredential

credential = AzureKeyCredential("<YOUR_API_KEY>")
```

## Microsoft Entra ID (Recommended)

```python
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```

---

# 2. Azure AI Language

```python
from azure.ai.textanalytics import TextAnalyticsClient

client = TextAnalyticsClient(endpoint, credential)
```

## Common Methods

| Method                      | Purpose                   |
| --------------------------- | ------------------------- |
| detect_language()           | Detect language           |
| analyze_sentiment()         | Sentiment analysis        |
| extract_key_phrases()       | Key phrase extraction     |
| recognize_entities()        | Named Entity Recognition  |
| recognize_linked_entities() | Linked entity recognition |

### Conversational Language Understanding

```python
from azure.ai.language.conversations import ConversationAnalysisClient

client = ConversationAnalysisClient(endpoint, credential)

result = client.analyze_conversation(...)
```

### Question Answering

```python
from azure.ai.language.questionanswering import QuestionAnsweringClient

client = QuestionAnsweringClient(endpoint, credential)

answers = client.get_answers(...)
```

> For new AI applications, Microsoft increasingly recommends combining Azure AI Search and Azure OpenAI for Retrieval-Augmented Generation (RAG) scenarios.

---

# 3. Azure Translator

Install:

```bash
pip install azure-ai-translation-text
```

```python
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential

client = TextTranslationClient(
    credential=AzureKeyCredential("<KEY>"),
    region="<REGION>"
)
```

## Common Methods

| Method                       | Purpose              |
| ---------------------------- | -------------------- |
| get_languages()              | Supported languages  |
| translate()                  | Text translation     |
| transliterate()              | Script conversion    |
| lookup_dictionary_entries()  | Dictionary lookup    |
| lookup_dictionary_examples() | Translation examples |

---

# 4. Azure AI Vision

## Image Analysis

```python
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=credential
)
```

### Available Visual Features

| Feature        | Purpose           |
| -------------- | ----------------- |
| READ           | OCR               |
| CAPTION        | Image caption     |
| DENSE_CAPTIONS | Detailed captions |
| TAGS           | Image tags        |
| OBJECTS        | Object detection  |
| PEOPLE         | Person detection  |
| SMART_CROPS    | Crop suggestions  |

### Example

```python
result = client.analyze(
    image_url,
    visual_features=[
        VisualFeatures.CAPTION,
        VisualFeatures.READ
    ]
)
```

---

# 5. Azure AI Face

```python
from azure.ai.vision.face import FaceClient
```

## Common Operations

| Operation      | Purpose               |
| -------------- | --------------------- |
| detect()       | Face detection        |
| identify()     | Face identification   |
| verify()       | Face verification     |
| find_similar() | Similar-face matching |

> Face services are subject to Microsoft's Responsible AI requirements and may require approval depending on the feature used.

---

# 6. Azure AI Document Intelligence

(Previously Azure Form Recognizer)

Install:

```bash
pip install azure-ai-documentintelligence
```

```python
from azure.ai.documentintelligence import DocumentIntelligenceClient

client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=credential
)
```

## Common Methods

| Method                          | Purpose                 |
| ------------------------------- | ----------------------- |
| begin_analyze_document()        | Analyze documents       |
| begin_classify_document()       | Document classification |
| begin_analyze_batch_documents() | Batch processing        |

### Example

```python
poller = client.begin_analyze_document(
    "prebuilt-read",
    document=document_bytes
)

result = poller.result()
```

### Common Prebuilt Models

| Model               | Purpose            |
| ------------------- | ------------------ |
| prebuilt-read       | OCR                |
| prebuilt-layout     | Layout extraction  |
| prebuilt-document   | General documents  |
| prebuilt-invoice    | Invoice extraction |
| prebuilt-receipt    | Receipt extraction |
| prebuilt-idDocument | Identity documents |

---

# 7. Azure AI Speech

## Speech Recognition

```python
from azure.cognitiveservices.speech import (
    SpeechConfig,
    AudioConfig,
    SpeechRecognizer
)

speech_config = SpeechConfig(
    subscription="<KEY>",
    region="<REGION>"
)

recognizer = SpeechRecognizer(
    speech_config=speech_config
)
```

### ResultReason

| Value                      | Meaning               |
| -------------------------- | --------------------- |
| RecognizedSpeech           | Recognition succeeded |
| Cancelled                  | Failed or cancelled   |
| NoMatch                    | No speech detected    |
| SynthesizingAudioCompleted | TTS completed         |

---

## Speech Synthesis

```python
from azure.cognitiveservices.speech import SpeechSynthesizer

synthesizer = SpeechSynthesizer(
    speech_config=speech_config
)

synthesizer.speak_text_async("Hello world")
```

---

## Speech Translation

```python
from azure.cognitiveservices.speech.translation import (
    SpeechTranslationConfig,
    TranslationRecognizer
)

config = SpeechTranslationConfig(
    subscription="<KEY>",
    region="<REGION>"
)

config.add_target_language("fr")

recognizer = TranslationRecognizer(
    translation_config=config
)
```

---

# 8. Generative AI — Azure OpenAI

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="<API_KEY>",
    azure_endpoint="<AZURE_OPENAI_ENDPOINT>",
    api_version="<API_VERSION>"
)
```

## Chat Completions

```python
response = client.chat.completions.create(
    model="<DEPLOYMENT_NAME>",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)
```

## Embeddings

```python
response = client.embeddings.create(
    model="<EMBEDDING_DEPLOYMENT>",
    input="Azure AI"
)
```

## Image Generation

```python
response = client.images.generate(
    model="<DEPLOYMENT_NAME>",
    prompt="A futuristic city"
)
```

### Common Workloads

| Capability       | API                             |
| ---------------- | ------------------------------- |
| Chatbots         | chat.completions                |
| Agents           | Azure AI Foundry + Azure OpenAI |
| RAG              | Azure AI Search + Azure OpenAI  |
| Embeddings       | embeddings                      |
| Image Generation | images                          |
| Function Calling | chat.completions                |

---

# 9. Full Import Reference

```python
# Authentication
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential

# Language
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.ai.language.questionanswering import QuestionAnsweringClient

# Translator
from azure.ai.translation.text import TextTranslationClient

# Vision
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures

# Face
from azure.ai.vision.face import FaceClient

# Document Intelligence
from azure.ai.documentintelligence import DocumentIntelligenceClient

# Speech
from azure.cognitiveservices.speech import (
    SpeechConfig,
    AudioConfig,
    SpeechRecognizer,
    SpeechSynthesizer,
    ResultReason
)

from azure.cognitiveservices.speech.translation import (
    SpeechTranslationConfig,
    TranslationRecognizer
)

# Azure OpenAI
from openai import AzureOpenAI
```
