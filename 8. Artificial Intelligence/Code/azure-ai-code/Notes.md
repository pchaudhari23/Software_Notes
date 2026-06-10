SDK Modules, classes, methods:

- azure (root module)

  - core (sub module)

    - credentials
      - AzureKeyCredential (class) => input: Resource key

  - ai

    - language (sub sub module)
      - conversations (sub sub sub module)
        - ConversationAnalysisClient (class) => input: Resource key, credentials object
          1. analyze_conversation()
      - questionanswering
        - QuestionAnsweringClient (class) => input: Resource key, credentials object
          1. get_answers()
    - textanalytics
      - TextAnalyticsClient (class) => input: Resource key, credentials object
        1. detect_language()
        2. analyze_sentiment()
        3. extract_key_phrases()
        4. recognize_entities()
        5. recognize_linked_entities()
        6. begin_single_label_classify(): Custom text classification
        7. begin_recognize_custom_entities(): Custom named entity recognition
    - translation
      - TranslatorCredential (class)
        1. get_languages()
        2. translate()
    - vision
      - imageanalysis
        - ImageAnalysisClient (class)
          1. analyze()
        - models => VisualFeatures => READ, CAPTION, DENSE_CAPTIONS, TAGS, OBJECTS, PEOPLE
      - VisionServiceOptions, ImageAnalysisOptions, ImageAnalysisFeature.PEOPLE, ImageAnalysisResultReason.ANALYZED
    - formrecognizer
      - DocumentAnalysisClient
        1. begin_analyze_document_from_url()

  - congnitiveservices

    - speech

      - SpeechConfig (class) => input: Resource key, credentials object
      - AudioConfig (class) => input: Speaker/microphone
      - SpeechRecognizer (class) => input: SpeechConfig, AudioConfig
      - ResultReason (class) => RecognizedSpeech, Cancelled, SynthesizingAudioCompleted
      - SpeechSynthesizer (class) => input: SpeechConfig

        1. speak_ssml_async()

        - translation
          - SpeechTranslationConfig (class) => input: Resource key, credentials object
          - TranslationRecognizer

    - vision

      - face
        - FaceClient
          1. face.detect_with_stream()
        - models => FaceAttributeType (class) => occlusion, blur, glasses

  - common
  - profiles
  - search

eg: Import namespaces

from azure.core.credentials import AzureKeyCredential

from azure.ai.textanalytics import TextAnalyticsClient

---

GEN AI SDK

AzureOpenAI (class) => input: OPEN AI KEY, OPEN AI ENDPOINT, API VERSION => client

client.chat.completions.create( model=model, messages=messages, temperature=0.7, max_tokens=1000 )

Eg: from openai import AzureOpenAI
